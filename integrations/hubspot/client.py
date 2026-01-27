"""HubSpot CRM API client with retry logic and rate limiting."""

import time
from typing import Any

import httpx

from ..common.config import get_hubspot_access_token
from ..common.utils import APIError

BASE_URL = "https://api.hubapi.com"


class HubSpotClient:
    """REST client for HubSpot CRM API with automatic retry on rate limits."""

    def __init__(self, token: str | None = None):
        """
        Initialize HubSpot client.

        Args:
            token: HubSpot Private App access token.
                   If not provided, reads from HUBSPOT_ACCESS_TOKEN env var.
        """
        self.token = token or get_hubspot_access_token()
        self.client = httpx.Client(
            base_url=BASE_URL,
            headers={
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json",
            },
            timeout=30.0,
        )

    def get(
        self,
        endpoint: str,
        params: dict[str, Any] | None = None,
        max_retries: int = 3,
    ) -> dict[str, Any]:
        """
        Make a GET request to HubSpot API with retry on rate limit.

        Args:
            endpoint: API endpoint (e.g., '/crm/v3/properties/contacts').
            params: Query parameters.
            max_retries: Maximum number of retries on 429 errors.

        Returns:
            API response data.

        Raises:
            APIError: If the request fails after retries.
        """
        for attempt in range(max_retries + 1):
            response = self.client.get(endpoint, params=params)

            if response.status_code == 429:
                if attempt < max_retries:
                    # HubSpot rate limit: 5 requests/second
                    # Retry-After header may be present
                    retry_after = int(response.headers.get("Retry-After", 1))
                    time.sleep(retry_after)
                    continue
                # Fall through to error handling after max retries

            return self._handle_response(response)

        # Should not reach here, but just in case
        raise APIError(
            "HubSpot API rate limit exceeded after max retries",
            status_code=429,
        )

    def post(
        self,
        endpoint: str,
        data: dict[str, Any],
        max_retries: int = 3,
    ) -> dict[str, Any]:
        """
        Make a POST request to HubSpot API with retry on rate limit.

        Args:
            endpoint: API endpoint (e.g., '/crm/v3/objects/contacts/search').
            data: JSON body data.
            max_retries: Maximum number of retries on 429 errors.

        Returns:
            API response data.

        Raises:
            APIError: If the request fails after retries.
        """
        for attempt in range(max_retries + 1):
            response = self.client.post(endpoint, json=data)

            if response.status_code == 429:
                if attempt < max_retries:
                    retry_after = int(response.headers.get("Retry-After", 1))
                    time.sleep(retry_after)
                    continue

            return self._handle_response(response)

        raise APIError(
            "HubSpot API rate limit exceeded after max retries",
            status_code=429,
        )

    def _handle_response(self, response: httpx.Response) -> dict[str, Any]:
        """Handle HubSpot API response and check for errors."""
        if response.status_code >= 400:
            try:
                error_data = response.json()
                message = error_data.get("message", f"HTTP {response.status_code}")
                raise APIError(
                    f"HubSpot API error: {message}",
                    status_code=response.status_code,
                    response=error_data,
                )
            except ValueError:
                raise APIError(
                    f"HubSpot API request failed: {response.status_code}",
                    status_code=response.status_code,
                    response=response.text,
                )

        return response.json()

    def close(self):
        """Close the HTTP client."""
        self.client.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


# Default client instance (lazy initialization)
_default_client: HubSpotClient | None = None


def get_client() -> HubSpotClient:
    """Get or create the default HubSpot client."""
    global _default_client
    if _default_client is None:
        _default_client = HubSpotClient()
    return _default_client

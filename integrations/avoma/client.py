"""Avoma REST API client."""

from typing import Any
import httpx

from ..common.config import get_avoma_api_key
from ..common.utils import APIError

BASE_URL = "https://api.avoma.com/v1"


class AvomaClient:
    """REST client for Avoma API."""

    def __init__(self, api_key: str | None = None):
        """
        Initialize Avoma client.

        Args:
            api_key: Avoma API key. If not provided, reads from AVOMA_API_KEY env var.
        """
        self.api_key = api_key or get_avoma_api_key()
        self.client = httpx.Client(
            base_url=BASE_URL,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            timeout=30.0,
            follow_redirects=True,  # Avoma API uses trailing slash redirects
        )

    def get(self, endpoint: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Make a GET request to Avoma API.

        Args:
            endpoint: API endpoint (e.g., '/meetings').
            params: Query parameters.

        Returns:
            API response data.

        Raises:
            APIError: If the request fails.
        """
        response = self.client.get(endpoint, params=params)
        return self._handle_response(response)

    def _handle_response(self, response: httpx.Response) -> dict[str, Any]:
        """Handle Avoma API response and check for errors."""
        if response.status_code >= 400:
            try:
                error_data = response.json()
                message = error_data.get("message", f"HTTP {response.status_code}")
                raise APIError(
                    f"Avoma API error: {message}",
                    status_code=response.status_code,
                    response=error_data,
                )
            except ValueError:
                raise APIError(
                    f"Avoma API request failed: {response.status_code}",
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
_default_client: AvomaClient | None = None


def get_client() -> AvomaClient:
    """Get or create the default Avoma client."""
    global _default_client
    if _default_client is None:
        _default_client = AvomaClient()
    return _default_client

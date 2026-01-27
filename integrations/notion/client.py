"""Notion REST API client."""

import time
from typing import Any
import httpx

from ..common.config import get_notion_token
from ..common.utils import APIError

BASE_URL = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"
MAX_RETRIES = 3


class NotionClient:
    """REST client for Notion API."""

    def __init__(self, token: str | None = None):
        """
        Initialize Notion client.

        Args:
            token: Notion integration token. If not provided, reads from NOTION_TOKEN env var.
        """
        self.token = token or get_notion_token()
        self.client = httpx.Client(
            base_url=BASE_URL,
            headers={
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json",
                "Notion-Version": NOTION_VERSION,
            },
            timeout=30.0,
        )

    def get(self, endpoint: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Make a GET request to Notion API.

        Args:
            endpoint: API endpoint (e.g., '/pages/{id}').
            params: Query parameters.

        Returns:
            API response data.

        Raises:
            APIError: If the request fails.
        """
        return self._request_with_retry("GET", endpoint, params=params)

    def post(self, endpoint: str, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Make a POST request to Notion API.

        Args:
            endpoint: API endpoint.
            data: Request body.

        Returns:
            API response data.

        Raises:
            APIError: If the request fails.
        """
        return self._request_with_retry("POST", endpoint, data=data)

    def patch(self, endpoint: str, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Make a PATCH request to Notion API.

        Args:
            endpoint: API endpoint.
            data: Request body.

        Returns:
            API response data.

        Raises:
            APIError: If the request fails.
        """
        return self._request_with_retry("PATCH", endpoint, data=data)

    def delete(self, endpoint: str) -> dict[str, Any]:
        """
        Make a DELETE request to Notion API.

        Args:
            endpoint: API endpoint.

        Returns:
            API response data.

        Raises:
            APIError: If the request fails.
        """
        return self._request_with_retry("DELETE", endpoint)

    def _request_with_retry(
        self,
        method: str,
        endpoint: str,
        params: dict[str, Any] | None = None,
        data: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Make a request with automatic retry on rate limiting (429)."""
        for attempt in range(1, MAX_RETRIES + 1):
            if method == "GET":
                response = self.client.get(endpoint, params=params)
            elif method == "POST":
                response = self.client.post(endpoint, json=data or {})
            elif method == "PATCH":
                response = self.client.patch(endpoint, json=data or {})
            elif method == "DELETE":
                response = self.client.delete(endpoint)
            else:
                raise ValueError(f"Unsupported method: {method}")

            if response.status_code == 429:
                # Notion uses Retry-After header (in seconds)
                retry_after = int(response.headers.get("Retry-After", "1"))
                if attempt == MAX_RETRIES:
                    raise APIError(
                        f"Notion API rate limited after {MAX_RETRIES} retries",
                        status_code=429,
                        response=response.text,
                    )
                time.sleep(retry_after)
                continue

            return self._handle_response(response)

        # Should not reach here, but just in case
        raise APIError(f"Notion API request failed after {MAX_RETRIES} retries")

    def _handle_response(self, response: httpx.Response) -> dict[str, Any]:
        """Handle Notion API response and check for errors."""
        if response.status_code >= 400:
            try:
                error_data = response.json()
                message = error_data.get("message", f"HTTP {response.status_code}")
                code = error_data.get("code", "unknown_error")
                raise APIError(
                    f"Notion API error ({code}): {message}",
                    status_code=response.status_code,
                    response=error_data,
                )
            except ValueError:
                raise APIError(
                    f"Notion API request failed: {response.status_code}",
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
_default_client: NotionClient | None = None


def get_client() -> NotionClient:
    """Get or create the default Notion client."""
    global _default_client
    if _default_client is None:
        _default_client = NotionClient()
    return _default_client

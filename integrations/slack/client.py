"""Slack REST API client."""

from typing import Any
import httpx

from ..common.config import get_slack_token
from ..common.utils import APIError

BASE_URL = "https://slack.com/api"


class SlackClient:
    """REST client for Slack Web API."""

    def __init__(self, token: str | None = None):
        """
        Initialize Slack client.

        Args:
            token: Slack user token (xoxp-). If not provided, reads from SLACK_USER_TOKEN env var.
        """
        self.token = token or get_slack_token()
        self.client = httpx.Client(
            base_url=BASE_URL,
            headers={
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json; charset=utf-8",
            },
            timeout=30.0,
        )

    def get(self, endpoint: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Make a GET request to Slack API.

        Args:
            endpoint: API endpoint (e.g., 'conversations.list').
            params: Query parameters.

        Returns:
            API response data.

        Raises:
            APIError: If the request fails.
        """
        response = self.client.get(f"/{endpoint}", params=params)
        return self._handle_response(response)

    def post(self, endpoint: str, data: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Make a POST request to Slack API.

        Args:
            endpoint: API endpoint (e.g., 'chat.postMessage').
            data: Request body.

        Returns:
            API response data.

        Raises:
            APIError: If the request fails.
        """
        response = self.client.post(f"/{endpoint}", json=data or {})
        return self._handle_response(response)

    def _handle_response(self, response: httpx.Response) -> dict[str, Any]:
        """Handle Slack API response and check for errors."""
        if response.status_code != 200:
            raise APIError(
                f"Slack API request failed: {response.status_code}",
                status_code=response.status_code,
                response=response.text,
            )

        data = response.json()

        if not data.get("ok"):
            error = data.get("error", "Unknown error")
            raise APIError(f"Slack API error: {error}", response=data)

        return data

    def close(self):
        """Close the HTTP client."""
        self.client.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


# Default client instance (lazy initialization)
_default_client: SlackClient | None = None


def get_client() -> SlackClient:
    """Get or create the default Slack client."""
    global _default_client
    if _default_client is None:
        _default_client = SlackClient()
    return _default_client

"""Linear GraphQL API client."""

from typing import Any
import httpx

from ..common.config import get_linear_api_key
from ..common.utils import APIError

GRAPHQL_ENDPOINT = "https://api.linear.app/graphql"


class LinearClient:
    """GraphQL client for Linear API."""

    def __init__(self, api_key: str | None = None):
        """
        Initialize Linear client.

        Args:
            api_key: Linear API key. If not provided, reads from LINEAR_API_KEY env var.
        """
        self.api_key = api_key or get_linear_api_key()
        self.client = httpx.Client(
            base_url=GRAPHQL_ENDPOINT,
            headers={
                "Authorization": self.api_key,  # No Bearer prefix for personal keys
                "Content-Type": "application/json",
            },
            timeout=30.0,
        )

    def query(self, query: str, variables: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Execute a GraphQL query.

        Args:
            query: GraphQL query string.
            variables: Optional query variables.

        Returns:
            The 'data' portion of the GraphQL response.

        Raises:
            APIError: If the request fails or returns errors.
        """
        payload = {"query": query}
        if variables:
            payload["variables"] = variables

        response = self.client.post("", json=payload)

        if response.status_code != 200:
            raise APIError(
                f"Linear API request failed: {response.status_code}",
                status_code=response.status_code,
                response=response.text,
            )

        data = response.json()

        if "errors" in data:
            error_messages = [e.get("message", str(e)) for e in data["errors"]]
            raise APIError(
                f"GraphQL errors: {'; '.join(error_messages)}",
                response=data,
            )

        return data.get("data", {})

    def mutate(self, mutation: str, variables: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Execute a GraphQL mutation.

        Args:
            mutation: GraphQL mutation string.
            variables: Optional mutation variables.

        Returns:
            The 'data' portion of the GraphQL response.
        """
        return self.query(mutation, variables)

    def close(self):
        """Close the HTTP client."""
        self.client.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


# Default client instance (lazy initialization)
_default_client: LinearClient | None = None


def get_client() -> LinearClient:
    """Get or create the default Linear client."""
    global _default_client
    if _default_client is None:
        _default_client = LinearClient()
    return _default_client

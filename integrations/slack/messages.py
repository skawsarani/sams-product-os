"""Slack Messages read operations."""

from typing import Any
from .client import get_client


def list_messages(
    channel: str,
    limit: int = 100,
    cursor: str | None = None,
    oldest: str | None = None,
    latest: str | None = None,
    inclusive: bool = True,
) -> dict[str, Any]:
    """
    List messages in a channel.

    Args:
        channel: Channel ID.
        limit: Number of messages to return (max 1000).
        cursor: Pagination cursor.
        oldest: Only messages after this timestamp.
        latest: Only messages before this timestamp.
        inclusive: Include messages with oldest/latest timestamps.

    Returns:
        Dict with 'messages' list and pagination info.
    """
    params: dict[str, Any] = {
        "channel": channel,
        "limit": limit,
        "inclusive": inclusive,
    }
    if cursor:
        params["cursor"] = cursor
    if oldest:
        params["oldest"] = oldest
    if latest:
        params["latest"] = latest

    result = get_client().get("conversations.history", params)
    return {
        "messages": result.get("messages", []),
        "has_more": result.get("has_more", False),
        "response_metadata": result.get("response_metadata", {}),
    }

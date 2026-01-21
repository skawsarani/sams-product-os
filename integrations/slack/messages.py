"""Slack Messages read operations."""

from typing import Any
from .client import get_client
from .users import get_user, get_user_display_name


def _resolve_user_names_on_demand(user_ids: list[str]) -> dict[str, str]:
    """
    Resolve user IDs to display names on demand (no caching).

    Args:
        user_ids: List of user IDs to resolve.

    Returns:
        Dict mapping user_id -> display_name.
    """
    unique_ids = list(set(uid for uid in user_ids if uid))
    result: dict[str, str] = {}

    for user_id in unique_ids:
        try:
            user = get_user(user_id)
            result[user_id] = get_user_display_name(user)
        except Exception:
            result[user_id] = user_id

    return result


def list_messages(
    channel: str,
    limit: int = 100,
    cursor: str | None = None,
    oldest: str | None = None,
    latest: str | None = None,
    inclusive: bool = True,
    resolve_users: bool = False,
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
        resolve_users: If True, resolve user IDs to display names.

    Returns:
        Dict with 'messages' list, pagination info,
        and optionally 'user_names' dict mapping user_id -> display_name.
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
    messages = result.get("messages", [])

    response: dict[str, Any] = {
        "messages": messages,
        "has_more": result.get("has_more", False),
        "response_metadata": result.get("response_metadata", {}),
    }

    if resolve_users:
        user_ids = [m.get("user") for m in messages if m.get("user")]
        response["user_names"] = _resolve_user_names_on_demand(user_ids)

    return response

"""Slack Thread read operations."""

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


def get_thread_replies(
    channel: str,
    thread_ts: str,
    limit: int = 200,
    cursor: str | None = None,
    inclusive: bool = True,
    resolve_users: bool = False,
) -> dict[str, Any]:
    """
    Get all replies in a thread.

    Args:
        channel: Channel ID containing the thread.
        thread_ts: Timestamp of the parent message (thread root).
        limit: Number of replies to return per page (max 1000).
        cursor: Pagination cursor.
        inclusive: Include the parent message in results.
        resolve_users: If True, resolve user IDs to display names.

    Returns:
        Dict with 'messages' list (parent + replies), pagination info,
        and optionally 'user_names' dict mapping user_id -> display_name.
    """
    params: dict[str, Any] = {
        "channel": channel,
        "ts": thread_ts,
        "limit": limit,
        "inclusive": inclusive,
    }
    if cursor:
        params["cursor"] = cursor

    result = get_client().get("conversations.replies", params)
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


def get_all_thread_replies(
    channel: str,
    thread_ts: str,
    include_parent: bool = True,
    resolve_users: bool = False,
) -> dict[str, Any]:
    """
    Get all replies in a thread, handling pagination automatically.

    Args:
        channel: Channel ID containing the thread.
        thread_ts: Timestamp of the parent message (thread root).
        include_parent: Include the parent message in results.
        resolve_users: If True, resolve user IDs to display names.

    Returns:
        Dict with 'messages' list (sorted by timestamp),
        and optionally 'user_names' dict mapping user_id -> display_name.
    """
    all_messages: list[dict[str, Any]] = []
    cursor = None

    while True:
        result = get_thread_replies(channel, thread_ts, cursor=cursor)
        messages = result.get("messages", [])
        all_messages.extend(messages)

        cursor = result.get("response_metadata", {}).get("next_cursor")
        if not cursor or not result.get("has_more"):
            break

    # Sort by timestamp
    all_messages.sort(key=lambda m: float(m.get("ts", "0")))

    # Optionally remove parent message
    if not include_parent and all_messages:
        all_messages = [m for m in all_messages if m.get("ts") != thread_ts]

    response: dict[str, Any] = {"messages": all_messages}

    if resolve_users:
        user_ids = [m.get("user") for m in all_messages if m.get("user")]
        response["user_names"] = _resolve_user_names_on_demand(user_ids)

    return response

"""Slack Messages read operations."""

import time
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


def find_unanswered_messages(
    channel: str,
    hours_old: int = 48,
    max_results: int = 50,
    resolve_users: bool = False,
) -> dict[str, Any]:
    """
    Find messages with no thread replies AND no emoji reactions.

    "Unanswered" is defined as:
    - reply_count == 0 (or missing)
    - reactions is empty or missing

    Args:
        channel: Channel ID to search.
        hours_old: Only include messages older than this many hours.
        max_results: Maximum messages to return.
        resolve_users: Resolve user IDs to display names.

    Returns:
        Dict with 'messages' list of unanswered messages,
        and optionally 'user_names' dict mapping user_id -> display_name.
    """
    # Calculate oldest timestamp (messages must be AT LEAST this old)
    oldest_ts = str(time.time() - (hours_old * 3600))

    # Fetch messages from channel
    all_messages: list[dict[str, Any]] = []
    cursor: str | None = None
    has_more = True

    while has_more and len(all_messages) < max_results * 3:
        result = list_messages(
            channel=channel,
            limit=200,
            cursor=cursor,
            latest=oldest_ts,  # Only messages BEFORE this time (older than hours_old)
            resolve_users=False,
        )

        messages = result.get("messages", [])
        all_messages.extend(messages)

        has_more = result.get("has_more", False)
        cursor = result.get("response_metadata", {}).get("next_cursor")

        if not cursor:
            break

    # Filter unanswered messages
    unanswered: list[dict[str, Any]] = []
    for msg in all_messages:
        # Skip bot messages, join/leave messages, etc.
        if msg.get("subtype"):
            continue

        # Check for no replies
        reply_count = msg.get("reply_count", 0)
        if reply_count > 0:
            continue

        # Check for no reactions
        reactions = msg.get("reactions", [])
        if reactions:
            continue

        unanswered.append(msg)

        if len(unanswered) >= max_results:
            break

    response: dict[str, Any] = {
        "messages": unanswered,
        "total_checked": len(all_messages),
    }

    if resolve_users:
        user_ids = [m.get("user") for m in unanswered if m.get("user")]
        response["user_names"] = _resolve_user_names_on_demand(user_ids)

    return response

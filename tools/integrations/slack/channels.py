"""Slack Channels read operations."""

from typing import Any
from .client import get_client
from .mapping import get_channel_id, set_channel_mapping


def resolve_channel(channel_input: str) -> dict[str, Any]:
    """
    Resolve a channel name or ID to full channel info.

    The Slack conversations.list API sometimes doesn't return all channels,
    even when the user has access. This function provides a reliable way to
    resolve channels by:
    1. Check mappings.json cache first (via get_channel_id)
    2. If input looks like a channel ID, verify it directly via conversations.info
    3. Fall back to searching conversations.list (and cache if found)

    Args:
        channel_input: Channel name (with or without #) or channel ID.

    Returns:
        Dict with 'ok', 'channel' (info), and 'method' (how it was resolved).
        If not found, returns {'ok': False, 'error': '...'}.
    """
    # Clean input
    clean_input = channel_input.strip().lstrip("#")

    # Check cache first (handles both IDs and cached names)
    cached_id = get_channel_id(clean_input)
    if cached_id:
        try:
            info = get_channel_info(cached_id)
            if info.get("id"):
                return {"ok": True, "channel": info, "method": "cache"}
        except Exception:
            pass

    # If it looks like a channel ID but wasn't in cache, try direct lookup
    if clean_input.startswith("C") and len(clean_input) >= 9:
        try:
            info = get_channel_info(clean_input)
            if info.get("id"):
                return {"ok": True, "channel": info, "method": "direct_lookup"}
        except Exception:
            pass
        return {"ok": False, "error": f"Channel ID {clean_input} not found or not accessible"}

    # Search in conversations.list (paginated) and cache if found
    cursor = None
    for _ in range(20):  # Max 20 pages
        result = list_channels(limit=200, cursor=cursor)
        channels = result.get("channels", [])

        for ch in channels:
            if ch.get("name", "").lower() == clean_input.lower():
                # Cache for next time
                set_channel_mapping(ch["name"], ch["id"])
                return {"ok": True, "channel": ch, "method": "conversations_list"}

        cursor = result.get("response_metadata", {}).get("next_cursor")
        if not cursor:
            break

    return {
        "ok": False,
        "error": f"Channel '{clean_input}' not found. Try providing the channel ID directly (right-click channel in Slack → 'Copy link' → extract ID from URL).",
    }


def list_channels(
    types: str = "public_channel,private_channel",
    exclude_archived: bool = True,
    limit: int = 100,
    cursor: str | None = None,
) -> dict[str, Any]:
    """
    List channels the user has access to.

    Args:
        types: Comma-separated channel types (public_channel, private_channel, mpim, im).
        exclude_archived: Exclude archived channels.
        limit: Number of channels to return (max 1000).
        cursor: Pagination cursor.

    Returns:
        Dict with 'channels' list and pagination info.
    """
    params: dict[str, Any] = {
        "types": types,
        "exclude_archived": exclude_archived,
        "limit": limit,
    }
    if cursor:
        params["cursor"] = cursor

    result = get_client().get("conversations.list", params)
    return {
        "channels": result.get("channels", []),
        "response_metadata": result.get("response_metadata", {}),
    }


def get_channel_info(channel: str, include_num_members: bool = False) -> dict[str, Any]:
    """
    Get information about a channel.

    Args:
        channel: Channel ID.
        include_num_members: Include member count.

    Returns:
        Channel information.
    """
    params: dict[str, Any] = {"channel": channel}
    if include_num_members:
        params["include_num_members"] = True

    result = get_client().get("conversations.info", params)
    return result.get("channel", result)

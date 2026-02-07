"""Slack Channels read operations."""

from typing import Any
from .client import get_client


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

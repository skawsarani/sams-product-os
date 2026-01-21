"""Slack Users read operations."""

from typing import Any
from .client import get_client


def get_user(user_id: str) -> dict[str, Any]:
    """
    Get information about a user by ID.

    Args:
        user_id: Slack user ID (e.g., 'U0123ABC').

    Returns:
        User information including profile, display name, etc.
    """
    result = get_client().get("users.info", {"user": user_id})
    return result.get("user", result)


def list_users(
    include_bots: bool = False,
    limit: int = 200,
    cursor: str | None = None,
) -> dict[str, Any]:
    """
    List all users in the workspace.

    Args:
        include_bots: Include bot users in results.
        limit: Number of users to return per page (max 200).
        cursor: Pagination cursor.

    Returns:
        Dict with 'members' list and pagination info.
    """
    params: dict[str, Any] = {"limit": limit}
    if cursor:
        params["cursor"] = cursor

    result = get_client().get("users.list", params)
    members = result.get("members", [])

    if not include_bots:
        members = [m for m in members if not m.get("is_bot") and m.get("id") != "USLACKBOT"]

    return {
        "members": members,
        "response_metadata": result.get("response_metadata", {}),
    }


def find_user_by_handle(
    handle: str,
    contains: bool = False,
    include_bots: bool = False,
) -> dict[str, Any] | None:
    """
    Find a user by their Slack handle (@username).

    Args:
        handle: User handle to search for (with or without @).
        contains: If True, match handles containing the search term.
                  If False, match exact handle only.
        include_bots: Include bot users in search.

    Returns:
        User information if found, None otherwise.
    """
    # Normalize handle (remove @ prefix if present)
    search_handle = handle.strip().lstrip("@").lower()

    cursor = None
    while True:
        result = list_users(include_bots=include_bots, cursor=cursor)
        members = result.get("members", [])

        for member in members:
            member_handle = (member.get("name") or "").lower()
            if contains:
                if search_handle in member_handle:
                    return member
            else:
                if member_handle == search_handle:
                    return member

        # Check for more pages
        cursor = result.get("response_metadata", {}).get("next_cursor")
        if not cursor:
            break

    return None


def get_user_display_name(user: dict[str, Any]) -> str:
    """
    Extract the best display name from a user object.

    Args:
        user: User object from Slack API.

    Returns:
        Display name (prefers display_name > real_name > name > id).
    """
    profile = user.get("profile", {})
    return (
        profile.get("display_name", "").strip()
        or profile.get("real_name", "").strip()
        or user.get("real_name", "").strip()
        or user.get("name", "").strip()
        or user.get("id", "unknown")
    )

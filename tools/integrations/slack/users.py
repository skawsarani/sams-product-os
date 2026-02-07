"""Slack Users read operations with automatic caching.

User mappings (handle->ID, ID->display_name) are cached by default.
To disable caching, set integrations.slack.cache_user_mappings: false in config.yaml.
"""

from typing import Any
from .client import get_client
from .mapping import (
    is_caching_enabled,
    get_user_id,
    upsert_user_cache,
)


def get_user(user_id: str, cache: bool | None = None) -> dict[str, Any]:
    """
    Get information about a user by ID.

    Args:
        user_id: Slack user ID (e.g., 'U0123ABC').
        cache: Override caching behavior. None uses config default.

    Returns:
        User information including profile, display name, etc.
    """
    result = get_client().get("users.info", {"user": user_id})
    user = result.get("user", result)

    # Cache the user mapping if caching is enabled
    should_cache = cache if cache is not None else is_caching_enabled()
    if should_cache and user.get("id"):
        upsert_user_cache([{
            "id": user["id"],
            "handle": user.get("name"),
            "display_name": get_user_display_name(user),
        }])

    return user


def list_users(
    include_bots: bool = False,
    limit: int = 200,
    cursor: str | None = None,
    cache: bool | None = None,
) -> dict[str, Any]:
    """
    List all users in the workspace.

    Args:
        include_bots: Include bot users in results.
        limit: Number of users to return per page (max 200).
        cursor: Pagination cursor.
        cache: Override caching behavior. None uses config default.

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

    # Cache all returned users if caching is enabled
    should_cache = cache if cache is not None else is_caching_enabled()
    if should_cache and members:
        cache_updates = [
            {
                "id": m["id"],
                "handle": m.get("name"),
                "display_name": get_user_display_name(m),
            }
            for m in members
            if m.get("id")
        ]
        if cache_updates:
            upsert_user_cache(cache_updates)

    return {
        "members": members,
        "response_metadata": result.get("response_metadata", {}),
    }


def find_user_by_handle(
    handle: str,
    contains: bool = False,
    include_bots: bool = False,
    cache: bool | None = None,
) -> dict[str, Any] | None:
    """
    Find a user by their Slack handle (@username).

    Checks cache first for exact matches (when contains=False).
    Results are cached automatically when caching is enabled.

    Args:
        handle: User handle to search for (with or without @).
        contains: If True, match handles containing the search term.
                  If False, match exact handle only.
        include_bots: Include bot users in search.
        cache: Override caching behavior. None uses config default.

    Returns:
        User information if found, None otherwise.
    """
    # Normalize handle (remove @ prefix if present)
    search_handle = handle.strip().lstrip("@").lower()

    should_cache = cache if cache is not None else is_caching_enabled()

    # For exact matches, check cache first
    if not contains and should_cache:
        cached_user_id = get_user_id(search_handle)
        if cached_user_id:
            try:
                # Fetch full user info using cached ID
                return get_user(cached_user_id, cache=should_cache)
            except Exception:
                # Cache may be stale, fall through to API search
                pass

    # Search via API (list_users handles caching internally)
    cursor = None
    while True:
        result = list_users(include_bots=include_bots, cursor=cursor, cache=should_cache)
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

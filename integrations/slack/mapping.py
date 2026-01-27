"""Slack ID/name mapping cache for channels and users.

The cache is built incrementally as API calls are made - it checks cache first,
only calls API for uncached items, then stores new results. No upfront bulk fetch.

Caching is enabled by default. To disable, add to config.yaml:

    integrations:
      slack:
        cache_user_mappings: false
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Any

import yaml

# Cache file location (same directory as this module)
MAPPINGS_FILE = Path(__file__).parent / "mappings.json"

# Config file location (project root)
CONFIG_FILE = Path(__file__).parent.parent.parent / "config.yaml"


def is_caching_enabled() -> bool:
    """
    Check if user mapping caching is enabled in config.

    Reads integrations.slack.cache_user_mappings from config.yaml.
    Returns True by default if config is missing or malformed.

    Returns:
        True if caching is enabled (default), False if explicitly disabled.
    """
    if not CONFIG_FILE.exists():
        return True

    try:
        with open(CONFIG_FILE) as f:
            config = yaml.safe_load(f) or {}
        return config.get("integrations", {}).get("slack", {}).get(
            "cache_user_mappings", True
        )
    except (yaml.YAMLError, OSError):
        return True


def _normalize_channel_name(name: str) -> str:
    """Normalize channel name for cache lookup (remove # prefix, lowercase)."""
    return name.strip().lstrip("#").lower()


def _normalize_user_handle(handle: str) -> str:
    """Normalize user handle for cache lookup (remove @ prefix, lowercase)."""
    return handle.strip().lstrip("@").lower()


def _is_channel_id(value: str) -> bool:
    """Check if value is already a channel ID (C.../G.../D...)."""
    import re
    return bool(re.match(r"^[CGD][A-Z0-9]+$", value.strip()))


def _is_user_id(value: str) -> bool:
    """Check if value is already a user ID (U...)."""
    import re
    return bool(re.match(r"^U[A-Z0-9]+$", value.strip()))


def load_mappings() -> dict[str, Any]:
    """
    Load mappings from the cache file.

    Returns:
        Dict with structure:
        {
            "version": 1,
            "updated_at": "2026-01-20T...",
            "channels": {"general": "C123...", ...},
            "users": {"jsmith": "U123...", ...},
            "user_id_to_name": {"U123...": "John Smith", ...}
        }
    """
    if not MAPPINGS_FILE.exists():
        return {
            "version": 1,
            "updated_at": datetime.now().isoformat(),
            "channels": {},
            "users": {},
            "user_id_to_name": {},
        }

    try:
        with open(MAPPINGS_FILE) as f:
            data = json.load(f)
        return {
            "version": 1,
            "updated_at": data.get("updated_at", datetime.now().isoformat()),
            "channels": data.get("channels", {}),
            "users": data.get("users", {}),
            "user_id_to_name": data.get("user_id_to_name", {}),
        }
    except (json.JSONDecodeError, OSError):
        return {
            "version": 1,
            "updated_at": datetime.now().isoformat(),
            "channels": {},
            "users": {},
            "user_id_to_name": {},
        }


def save_mappings(mappings: dict[str, Any]) -> None:
    """
    Save mappings to the cache file.

    Args:
        mappings: Mappings dict to save.
    """
    mappings["updated_at"] = datetime.now().isoformat()
    mappings["version"] = 1

    with open(MAPPINGS_FILE, "w") as f:
        json.dump(mappings, f, indent=2)
        f.write("\n")


def get_channel_id(name_or_id: str) -> str | None:
    """
    Get channel ID from cache, or return as-is if already an ID.

    Args:
        name_or_id: Channel name (with or without #) or channel ID.

    Returns:
        Channel ID if found in cache or already an ID, None otherwise.
    """
    value = name_or_id.strip()
    if _is_channel_id(value):
        return value

    mappings = load_mappings()
    return mappings["channels"].get(_normalize_channel_name(value))


def set_channel_mapping(name: str, channel_id: str) -> None:
    """
    Cache a channel name -> ID mapping.

    Args:
        name: Channel name (with or without #).
        channel_id: Channel ID.
    """
    mappings = load_mappings()
    mappings["channels"][_normalize_channel_name(name)] = channel_id
    save_mappings(mappings)


def get_user_id(handle_or_id: str) -> str | None:
    """
    Get user ID from cache, or return as-is if already an ID.

    Args:
        handle_or_id: User handle (with or without @) or user ID.

    Returns:
        User ID if found in cache or already an ID, None otherwise.
    """
    value = handle_or_id.strip()
    if _is_user_id(value):
        return value

    mappings = load_mappings()
    return mappings["users"].get(_normalize_user_handle(value))


def set_user_mapping(handle: str, user_id: str) -> None:
    """
    Cache a user handle -> ID mapping.

    Args:
        handle: User handle (with or without @).
        user_id: User ID.
    """
    mappings = load_mappings()
    mappings["users"][_normalize_user_handle(handle)] = user_id
    save_mappings(mappings)


def get_user_display_name(user_id: str) -> str | None:
    """
    Get cached display name for a user ID.

    Args:
        user_id: User ID.

    Returns:
        Display name if cached, None otherwise.
    """
    mappings = load_mappings()
    return mappings["user_id_to_name"].get(user_id)


def set_user_display_name(user_id: str, display_name: str) -> None:
    """
    Cache a user ID -> display name mapping.

    Args:
        user_id: User ID.
        display_name: Display name.
    """
    mappings = load_mappings()
    mappings["user_id_to_name"][user_id] = display_name
    save_mappings(mappings)


def upsert_user_cache(
    updates: list[dict[str, str | None]],
) -> None:
    """
    Batch update user cache with multiple mappings.

    Args:
        updates: List of dicts with keys:
            - id: User ID (required)
            - handle: User handle (optional)
            - display_name: Display name (optional)
    """
    if not updates:
        return

    mappings = load_mappings()

    for update in updates:
        user_id = update.get("id")
        if not user_id:
            continue

        handle = update.get("handle")
        if handle:
            mappings["users"][_normalize_user_handle(handle)] = user_id

        display_name = update.get("display_name")
        if display_name:
            mappings["user_id_to_name"][user_id] = display_name

    save_mappings(mappings)


def clear_mappings() -> None:
    """Clear all cached mappings."""
    save_mappings({
        "version": 1,
        "updated_at": datetime.now().isoformat(),
        "channels": {},
        "users": {},
        "user_id_to_name": {},
    })

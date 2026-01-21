"""Slack channel daily summary - fetch messages and compute stats."""

from dataclasses import dataclass, field
from datetime import datetime, date
from typing import Any

from .client import get_client
from .channels import list_channels, get_channel_info
from .messages import list_messages
from .threads import get_all_thread_replies
from .users import get_user, get_user_display_name
from .mapping import (
    get_channel_id,
    set_channel_mapping,
    get_user_display_name as get_cached_display_name,
    upsert_user_cache,
)


@dataclass
class ChannelSummary:
    """Summary of a channel's activity for a specific day."""

    channel_id: str
    channel_name: str | None
    date: str  # YYYY-MM-DD
    message_count: int
    participant_count: int
    top_participants: list[dict[str, Any]]  # [{"who": "John", "count": 15}, ...]
    thread_count: int
    total_replies: int
    messages: list[dict[str, Any]] = field(default_factory=list)


def _day_window_local(target_date: str) -> tuple[float, float]:
    """
    Get Unix timestamps for start/end of a local day.

    Args:
        target_date: Date string in YYYY-MM-DD format.

    Returns:
        Tuple of (start_timestamp, end_timestamp).
    """
    year, month, day = map(int, target_date.split("-"))
    start = datetime(year, month, day, 0, 0, 0)
    end = datetime(year, month, day, 23, 59, 59, 999999)
    return start.timestamp(), end.timestamp()


def _resolve_channel(
    channel: str,
    include_private: bool = False,
    update_cache: bool = True,
) -> str | None:
    """
    Resolve channel name to ID, checking cache first.

    Args:
        channel: Channel name or ID.
        include_private: Include private channels in lookup.
        update_cache: Update cache with found mapping.

    Returns:
        Channel ID or None if not found.
    """
    # Check if already an ID or in cache
    cached_id = get_channel_id(channel)
    if cached_id:
        return cached_id

    # Search via API
    target = channel.strip().lstrip("#").lower()
    types = "public_channel,private_channel" if include_private else "public_channel"

    cursor = None
    for _ in range(50):  # Max pages to search
        result = list_channels(types=types, cursor=cursor)
        channels = result.get("channels", [])

        for ch in channels:
            if (ch.get("name") or "").lower() == target:
                if update_cache and ch.get("name"):
                    set_channel_mapping(ch["name"], ch["id"])
                return ch["id"]

        cursor = result.get("response_metadata", {}).get("next_cursor")
        if not cursor:
            break

    return None


def _resolve_user_names(
    user_ids: list[str],
    update_cache: bool = True,
) -> dict[str, str]:
    """
    Resolve user IDs to display names, using cache when possible.

    Args:
        user_ids: List of user IDs to resolve.
        update_cache: Update cache with resolved names.

    Returns:
        Dict mapping user_id -> display_name.
    """
    unique_ids = list(set(uid for uid in user_ids if uid))
    result: dict[str, str] = {}
    cache_updates: list[dict[str, str | None]] = []

    for user_id in unique_ids:
        # Check cache first
        cached_name = get_cached_display_name(user_id)
        if cached_name:
            result[user_id] = cached_name
            continue

        # Fetch from API
        try:
            user = get_user(user_id)
            display_name = get_user_display_name(user)
            result[user_id] = display_name
            cache_updates.append({
                "id": user_id,
                "handle": user.get("name"),
                "display_name": display_name,
            })
        except Exception:
            result[user_id] = user_id

    if update_cache and cache_updates:
        upsert_user_cache(cache_updates)

    return result


def _compute_top_participants(
    messages: list[dict[str, Any]],
    names: dict[str, str] | None = None,
    limit: int = 15,
) -> list[dict[str, Any]]:
    """Compute top participants by message count."""
    counts: dict[str, int] = {}

    for msg in messages:
        actor = msg.get("user") or msg.get("username") or msg.get("bot_id") or "unknown"
        counts[actor] = counts.get(actor, 0) + 1

    sorted_participants = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:limit]

    return [
        {"who": names.get(uid, uid) if names else uid, "count": count}
        for uid, count in sorted_participants
    ]


def _compute_thread_stats(messages: list[dict[str, Any]]) -> tuple[int, int]:
    """Compute thread count and total replies."""
    thread_count = 0
    total_replies = 0

    for msg in messages:
        thread_ts = msg.get("thread_ts")
        ts = msg.get("ts")
        if thread_ts and thread_ts == ts:  # This is a thread root
            thread_count += 1
            total_replies += msg.get("reply_count", 0)

    return thread_count, total_replies


def get_channel_day_summary(
    channel: str,
    target_date: str | None = None,
    include_thread_replies: bool = False,
    max_threads: int = 25,
    include_bots: bool = False,
    resolve_users: bool = True,
    include_private: bool = False,
) -> ChannelSummary:
    """
    Fetch all messages from a channel for a specific day and compute summary stats.

    Args:
        channel: Channel ID or name (with or without #).
        target_date: Date in YYYY-MM-DD format. Defaults to today.
        include_thread_replies: Fetch and include thread replies.
        max_threads: Maximum number of threads to traverse (when include_thread_replies=True).
        include_bots: Include bot messages.
        resolve_users: Resolve user IDs to display names.
        include_private: Include private channels in name lookup.

    Returns:
        ChannelSummary with stats and messages.

    Raises:
        ValueError: If channel cannot be resolved.
    """
    # Resolve channel
    channel_id = _resolve_channel(channel, include_private=include_private)
    if not channel_id:
        raise ValueError(f"Could not resolve channel: {channel}")

    # Get channel name for display
    try:
        channel_info = get_channel_info(channel_id)
        channel_name = channel_info.get("name")
    except Exception:
        channel_name = None

    # Default to today
    if not target_date:
        target_date = date.today().isoformat()

    # Get day window
    oldest, latest = _day_window_local(target_date)

    # Fetch all messages for the day
    all_messages: list[dict[str, Any]] = []
    cursor = None

    for _ in range(50):  # Max pages
        result = list_messages(
            channel=channel_id,
            oldest=str(oldest),
            latest=str(latest),
            cursor=cursor,
        )
        all_messages.extend(result.get("messages", []))

        cursor = result.get("response_metadata", {}).get("next_cursor")
        if not cursor or not result.get("has_more"):
            break

    # Filter bots if needed
    if not include_bots:
        all_messages = [
            m for m in all_messages
            if not m.get("bot_id") and m.get("subtype") != "bot_message"
        ]

    # Sort by timestamp (Slack returns newest first)
    all_messages.sort(key=lambda m: float(m.get("ts", "0")))

    # Optionally fetch thread replies
    if include_thread_replies:
        thread_roots = [
            m for m in all_messages
            if m.get("thread_ts") == m.get("ts") and m.get("reply_count", 0) > 0
        ][:max_threads]

        for root in thread_roots:
            replies = get_all_thread_replies(
                channel_id,
                root["ts"],
                include_parent=False,
            )
            if not include_bots:
                replies = [
                    r for r in replies
                    if not r.get("bot_id") and r.get("subtype") != "bot_message"
                ]
            all_messages.extend(replies)

        # Re-sort after adding replies
        all_messages.sort(key=lambda m: float(m.get("ts", "0")))

    # Resolve user names
    names: dict[str, str] | None = None
    if resolve_users:
        user_ids = [m.get("user") for m in all_messages if m.get("user")]
        names = _resolve_user_names(user_ids)

    # Compute stats
    thread_count, total_replies = _compute_thread_stats(all_messages)
    top_participants = _compute_top_participants(all_messages, names)
    unique_participants = set(
        m.get("user") or m.get("username") or m.get("bot_id") or "unknown"
        for m in all_messages
    )

    return ChannelSummary(
        channel_id=channel_id,
        channel_name=channel_name,
        date=target_date,
        message_count=len(all_messages),
        participant_count=len(unique_participants),
        top_participants=top_participants,
        thread_count=thread_count,
        total_replies=total_replies,
        messages=all_messages,
    )

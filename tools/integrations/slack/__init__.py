"""Slack API integration - REST client and resource functions (read-only)."""

from .messages import (
    list_messages,
    find_unanswered_messages,
)
from .channels import (
    list_channels,
    get_channel_info,
)
from .search import (
    search_messages,
    search_files,
)
from .users import (
    get_user,
    list_users,
    find_user_by_handle,
    get_user_display_name,
)
from .threads import (
    get_thread_replies,
    get_all_thread_replies,
)
from .links import (
    parse_slack_message_link,
    build_slack_message_url,
    is_slack_url,
    SlackMessageLink,
)
from .mapping import (
    load_mappings,
    save_mappings,
    get_channel_id,
    set_channel_mapping,
    get_user_id,
    set_user_mapping,
    get_user_display_name as get_cached_user_display_name,
    set_user_display_name,
    upsert_user_cache,
    clear_mappings,
    is_caching_enabled,
)
from .channel_summary import (
    get_channel_day_summary,
    ChannelSummary,
)

__all__ = [
    # Messages
    "list_messages",
    "find_unanswered_messages",
    # Channels
    "list_channels",
    "get_channel_info",
    # Search
    "search_messages",
    "search_files",
    # Users
    "get_user",
    "list_users",
    "find_user_by_handle",
    "get_user_display_name",
    # Threads
    "get_thread_replies",
    "get_all_thread_replies",
    # Links
    "parse_slack_message_link",
    "build_slack_message_url",
    "is_slack_url",
    "SlackMessageLink",
    # Mapping cache
    "load_mappings",
    "save_mappings",
    "get_channel_id",
    "set_channel_mapping",
    "get_user_id",
    "set_user_mapping",
    "get_cached_user_display_name",
    "set_user_display_name",
    "upsert_user_cache",
    "clear_mappings",
    "is_caching_enabled",
    # Channel summary
    "get_channel_day_summary",
    "ChannelSummary",
]

"""CLI interface for Slack integration.

Usage:
    uv run python -m integrations.slack <command> [options]

Commands:
    search-messages     Search for messages
    search-files        Search for files
    get-thread          Get thread replies
    list-channels       List channels
    get-channel         Get channel info
"""

import argparse
import json
import sys

from . import (
    search_messages,
    search_files,
    get_thread_replies,
    get_all_thread_replies,
    list_channels,
    get_channel_info,
)


def cmd_search_messages(args: argparse.Namespace) -> None:
    """Search for messages."""
    result = search_messages(
        query=args.query,
        count=args.count,
        page=args.page,
        sort=args.sort,
        sort_dir=args.sort_dir,
    )
    print(json.dumps(result, indent=2, default=str))


def cmd_search_files(args: argparse.Namespace) -> None:
    """Search for files."""
    result = search_files(
        query=args.query,
        count=args.count,
        page=args.page,
        sort=args.sort,
        sort_dir=args.sort_dir,
    )
    print(json.dumps(result, indent=2, default=str))


def cmd_get_thread(args: argparse.Namespace) -> None:
    """Get thread replies."""
    if args.all:
        result = get_all_thread_replies(
            channel=args.channel,
            thread_ts=args.thread_ts,
            include_parent=args.include_parent,
            resolve_users=args.resolve_users,
        )
    else:
        result = get_thread_replies(
            channel=args.channel,
            thread_ts=args.thread_ts,
            limit=args.limit,
            resolve_users=args.resolve_users,
        )
    print(json.dumps(result, indent=2, default=str))


def cmd_list_channels(args: argparse.Namespace) -> None:
    """List channels."""
    result = list_channels(
        types=args.types,
        limit=args.limit,
        exclude_archived=not args.include_archived,
    )
    print(json.dumps(result, indent=2, default=str))


def cmd_get_channel(args: argparse.Namespace) -> None:
    """Get channel info."""
    result = get_channel_info(channel=args.channel)
    print(json.dumps(result, indent=2, default=str))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Slack integration CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # search-messages
    p_search = subparsers.add_parser("search-messages", help="Search for messages")
    p_search.add_argument("--query", "-q", required=True, help="Search query")
    p_search.add_argument("--count", "-c", type=int, default=20, help="Results per page (max 100)")
    p_search.add_argument("--page", "-p", type=int, default=1, help="Page number")
    p_search.add_argument("--sort", default="timestamp", choices=["timestamp", "score"])
    p_search.add_argument("--sort-dir", default="desc", choices=["asc", "desc"])
    p_search.set_defaults(func=cmd_search_messages)

    # search-files
    p_files = subparsers.add_parser("search-files", help="Search for files")
    p_files.add_argument("--query", "-q", required=True, help="Search query")
    p_files.add_argument("--count", "-c", type=int, default=20, help="Results per page")
    p_files.add_argument("--page", "-p", type=int, default=1, help="Page number")
    p_files.add_argument("--sort", default="timestamp", choices=["timestamp", "score"])
    p_files.add_argument("--sort-dir", default="desc", choices=["asc", "desc"])
    p_files.set_defaults(func=cmd_search_files)

    # get-thread
    p_thread = subparsers.add_parser("get-thread", help="Get thread replies")
    p_thread.add_argument("--channel", "-c", required=True, help="Channel ID")
    p_thread.add_argument("--thread-ts", "-t", required=True, help="Thread timestamp")
    p_thread.add_argument("--limit", "-l", type=int, default=200, help="Max replies")
    p_thread.add_argument("--all", "-a", action="store_true", help="Get all replies (paginated)")
    p_thread.add_argument("--include-parent", action="store_true", default=True, help="Include parent message")
    p_thread.add_argument("--resolve-users", action="store_true", help="Resolve user IDs to names")
    p_thread.set_defaults(func=cmd_get_thread)

    # list-channels
    p_channels = subparsers.add_parser("list-channels", help="List channels")
    p_channels.add_argument("--types", default="public_channel,private_channel", help="Channel types")
    p_channels.add_argument("--limit", "-l", type=int, default=100, help="Max channels")
    p_channels.add_argument("--include-archived", action="store_true", help="Include archived")
    p_channels.set_defaults(func=cmd_list_channels)

    # get-channel
    p_channel = subparsers.add_parser("get-channel", help="Get channel info")
    p_channel.add_argument("--channel", "-c", required=True, help="Channel ID")
    p_channel.set_defaults(func=cmd_get_channel)

    args = parser.parse_args()

    try:
        args.func(args)
        return 0
    except Exception as e:
        print(json.dumps({"error": str(e)}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

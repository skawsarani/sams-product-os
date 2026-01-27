"""CLI interface for Avoma integration.

Usage:
    uv run python -m integrations.avoma <command> [options]

Commands:
    list-meetings       List meetings
    search-meetings     Search meetings by subject (client-side filtering)
    get-meeting         Get meeting by ID
    get-transcript      Get transcript for a meeting
"""

import argparse
import json
import sys

from . import (
    list_meetings,
    search_meetings,
    get_meeting,
    get_transcript,
)


def cmd_list_meetings(args: argparse.Namespace) -> None:
    """List meetings."""
    result = list_meetings(
        limit=args.limit,
        offset=args.offset,
        from_date=args.from_date,
        to_date=args.to_date,
        status=args.status,
        scope=args.scope,
    )
    print(json.dumps(result, indent=2, default=str))


def cmd_search_meetings(args: argparse.Namespace) -> None:
    """Search meetings by subject."""
    result = search_meetings(
        query=args.query,
        max_results=args.max_results,
        from_date=args.from_date,
        to_date=args.to_date,
        scope=args.scope,
    )
    print(json.dumps(result, indent=2, default=str))


def cmd_get_meeting(args: argparse.Namespace) -> None:
    """Get meeting by ID."""
    result = get_meeting(args.id)
    print(json.dumps(result, indent=2, default=str))


def cmd_get_transcript(args: argparse.Namespace) -> None:
    """Get transcript for a meeting."""
    result = get_transcript(args.meeting_id)
    print(json.dumps(result, indent=2, default=str))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Avoma integration CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # list-meetings
    p_list = subparsers.add_parser("list-meetings", help="List meetings")
    p_list.add_argument("--limit", "-l", type=int, default=20, help="Max results (max 100)")
    p_list.add_argument("--offset", type=int, default=0, help="Offset for pagination")
    p_list.add_argument("--from-date", help="Start date (YYYY-MM-DD)")
    p_list.add_argument("--to-date", help="End date (YYYY-MM-DD)")
    p_list.add_argument("--status", help="Filter by status (completed, scheduled)")
    p_list.add_argument("--scope", default="all", choices=["all", "team", "mine"])
    p_list.set_defaults(func=cmd_list_meetings)

    # search-meetings
    p_search = subparsers.add_parser("search-meetings", help="Search meetings by subject")
    p_search.add_argument("--query", "-q", required=True, help="Search term")
    p_search.add_argument("--max-results", "-m", type=int, default=10, help="Max results")
    p_search.add_argument("--from-date", help="Start date (YYYY-MM-DD)")
    p_search.add_argument("--to-date", help="End date (YYYY-MM-DD)")
    p_search.add_argument("--scope", default="all", choices=["all", "team", "mine"])
    p_search.set_defaults(func=cmd_search_meetings)

    # get-meeting
    p_get = subparsers.add_parser("get-meeting", help="Get meeting by ID")
    p_get.add_argument("--id", required=True, help="Meeting ID")
    p_get.set_defaults(func=cmd_get_meeting)

    # get-transcript
    p_transcript = subparsers.add_parser("get-transcript", help="Get transcript for a meeting")
    p_transcript.add_argument("--meeting-id", "-m", required=True, help="Meeting UUID")
    p_transcript.set_defaults(func=cmd_get_transcript)

    args = parser.parse_args()

    try:
        args.func(args)
        return 0
    except Exception as e:
        print(json.dumps({"error": str(e)}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

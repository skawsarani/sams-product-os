"""CLI interface for Google Calendar integration.

Usage:
    uv run python -m tools.integrations.google_calendar <command> [options]

Commands:
    list-events         List events with date range filtering
    list-calendars      List accessible calendars
    get-event           Get event details by ID
"""

import argparse
import json
import sys
from datetime import datetime, timedelta, timezone

from .events import get_event, list_events
from .calendars import get_calendar, list_calendars


def _resolve_date(date_str: str) -> tuple[str, str]:
    """Resolve a date string to (time_min, time_max) ISO strings for a full day.

    Supports 'today', 'tomorrow', 'yesterday', or YYYY-MM-DD.
    """
    today = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)

    if date_str == "today":
        start = today
    elif date_str == "tomorrow":
        start = today + timedelta(days=1)
    elif date_str == "yesterday":
        start = today - timedelta(days=1)
    else:
        start = datetime.strptime(date_str, "%Y-%m-%d").replace(tzinfo=timezone.utc)

    end = start + timedelta(days=1)
    return start.isoformat(), end.isoformat()


def cmd_list_events(args: argparse.Namespace) -> None:
    """List events in a calendar."""
    time_min = None
    time_max = None

    if args.date:
        time_min, time_max = _resolve_date(args.date)
    elif args.days:
        now = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
        time_min = now.isoformat()
        time_max = (now + timedelta(days=args.days)).isoformat()

    result = list_events(
        calendar_id=args.calendar_id,
        time_min=time_min,
        time_max=time_max,
        max_results=args.max_results,
        q=args.query,
        page_token=args.page_token,
    )
    print(json.dumps(result, indent=2, default=str))


def cmd_list_calendars(args: argparse.Namespace) -> None:
    """List accessible calendars."""
    result = list_calendars(
        max_results=args.max_results,
        show_hidden=args.show_hidden,
        page_token=args.page_token,
    )
    print(json.dumps(result, indent=2, default=str))


def cmd_get_event(args: argparse.Namespace) -> None:
    """Get event details by ID."""
    result = get_event(
        calendar_id=args.calendar_id,
        event_id=args.id,
    )
    if result is None:
        print(json.dumps({"error": "Event not found"}), file=sys.stderr)
        sys.exit(1)
    print(json.dumps(result, indent=2, default=str))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Google Calendar integration CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Date examples:
  --date today              Today's events
  --date tomorrow           Tomorrow's events
  --date yesterday          Yesterday's events
  --date 2026-02-10         Events on a specific date
  --days 7                  Events for the next 7 days
""",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # list-events
    p_events = subparsers.add_parser("list-events", help="List events with date range filtering")
    p_events.add_argument("--calendar-id", "-c", default="primary", help="Calendar ID (default: primary)")
    p_events.add_argument("--date", "-d", help="Date filter: 'today', 'tomorrow', 'yesterday', or YYYY-MM-DD")
    p_events.add_argument("--days", type=int, help="Number of days from today to fetch")
    p_events.add_argument("--query", "-q", help="Free text search query")
    p_events.add_argument("--max-results", "-l", type=int, default=100, help="Maximum events to return")
    p_events.add_argument("--page-token", help="Pagination token")
    p_events.set_defaults(func=cmd_list_events)

    # list-calendars
    p_cals = subparsers.add_parser("list-calendars", help="List accessible calendars")
    p_cals.add_argument("--max-results", "-l", type=int, default=100, help="Maximum calendars to return")
    p_cals.add_argument("--show-hidden", action="store_true", help="Include hidden calendars")
    p_cals.add_argument("--page-token", help="Pagination token")
    p_cals.set_defaults(func=cmd_list_calendars)

    # get-event
    p_get = subparsers.add_parser("get-event", help="Get event details by ID")
    p_get.add_argument("--id", required=True, help="Event ID")
    p_get.add_argument("--calendar-id", "-c", default="primary", help="Calendar ID (default: primary)")
    p_get.set_defaults(func=cmd_get_event)

    args = parser.parse_args()

    try:
        args.func(args)
        return 0
    except Exception as e:
        print(json.dumps({"error": str(e)}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

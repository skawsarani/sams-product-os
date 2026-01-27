"""CLI interface for Notion integration.

Usage:
    uv run python -m integrations.notion <command> [options]

Commands:
    search              Search pages and databases
    get-page            Get page by ID
    get-database        Get database by ID
"""

import argparse
import json
import sys

from .search import search
from .pages import get_page
from .databases import get_database


def cmd_search(args: argparse.Namespace) -> None:
    """Search pages and databases."""
    result = search(
        query=args.query or "",
        filter_type=args.filter_type,
        sort_direction=args.sort_direction,
        page_size=args.page_size,
        start_cursor=args.cursor,
    )
    print(json.dumps(result, indent=2, default=str))


def cmd_get_page(args: argparse.Namespace) -> None:
    """Get page by ID."""
    result = get_page(args.id)
    print(json.dumps(result, indent=2, default=str))


def cmd_get_database(args: argparse.Namespace) -> None:
    """Get database by ID."""
    result = get_database(args.id)
    print(json.dumps(result, indent=2, default=str))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Notion integration CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # search
    p_search = subparsers.add_parser("search", help="Search pages and databases")
    p_search.add_argument("--query", "-q", help="Search query")
    p_search.add_argument("--filter-type", "-t", choices=["page", "database"], help="Filter by type")
    p_search.add_argument("--sort-direction", "-s", default="descending", choices=["ascending", "descending"])
    p_search.add_argument("--page-size", "-l", type=int, default=100, help="Results per page (max 100)")
    p_search.add_argument("--cursor", "-c", help="Pagination cursor")
    p_search.set_defaults(func=cmd_search)

    # get-page
    p_page = subparsers.add_parser("get-page", help="Get page by ID")
    p_page.add_argument("--id", required=True, help="Page ID")
    p_page.set_defaults(func=cmd_get_page)

    # get-database
    p_db = subparsers.add_parser("get-database", help="Get database by ID")
    p_db.add_argument("--id", required=True, help="Database ID")
    p_db.set_defaults(func=cmd_get_database)

    args = parser.parse_args()

    try:
        args.func(args)
        return 0
    except Exception as e:
        print(json.dumps({"error": str(e)}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

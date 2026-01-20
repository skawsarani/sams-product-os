"""Notion Search operations."""

from typing import Any, Literal
from .client import get_client


def search(
    query: str = "",
    filter_type: Literal["page", "database"] | None = None,
    sort_direction: Literal["ascending", "descending"] = "descending",
    sort_timestamp: Literal["last_edited_time"] = "last_edited_time",
    start_cursor: str | None = None,
    page_size: int = 100,
) -> dict[str, Any]:
    """
    Search across the workspace by title.

    Args:
        query: Search query string. Empty string returns all accessible pages/databases.
        filter_type: Filter to only 'page' or 'database' objects.
        sort_direction: Sort by timestamp ('ascending' or 'descending').
        sort_timestamp: Timestamp to sort by (currently only 'last_edited_time').
        start_cursor: Pagination cursor.
        page_size: Results per page (max 100).

    Returns:
        Dict with 'results' (pages/databases), 'has_more', and 'next_cursor'.

    Example:
        # Search for pages containing "roadmap"
        search(query="roadmap", filter_type="page")

        # List all databases
        search(filter_type="database")

        # Get recently edited pages
        search(
            filter_type="page",
            sort_direction="descending",
            page_size=10
        )
    """
    data: dict[str, Any] = {
        "page_size": page_size,
        "sort": {
            "direction": sort_direction,
            "timestamp": sort_timestamp,
        },
    }

    if query:
        data["query"] = query

    if filter_type:
        data["filter"] = {"property": "object", "value": filter_type}

    if start_cursor:
        data["start_cursor"] = start_cursor

    return get_client().post("/search", data)

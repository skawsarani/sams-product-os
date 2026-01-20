"""Notion Databases read operations."""

from typing import Any
from .client import get_client


def get_database(database_id: str) -> dict[str, Any]:
    """
    Get a database by ID.

    Args:
        database_id: Database ID (UUID, with or without dashes).

    Returns:
        Database data including schema.
    """
    return get_client().get(f"/databases/{database_id}")


def query_database(
    database_id: str,
    filter: dict[str, Any] | None = None,
    sorts: list[dict[str, Any]] | None = None,
    start_cursor: str | None = None,
    page_size: int = 100,
) -> dict[str, Any]:
    """
    Query a database for pages matching filters.

    Args:
        database_id: Database ID to query.
        filter: Filter conditions (see Notion API docs for filter syntax).
        sorts: Sort conditions.
        start_cursor: Pagination cursor.
        page_size: Results per page (max 100).

    Returns:
        Dict with 'results' (pages), 'has_more', and 'next_cursor'.

    Example:
        # Query for active tasks
        query_database(
            database_id="abc123",
            filter={
                "property": "Status",
                "select": {"equals": "Active"}
            },
            sorts=[{"property": "Due Date", "direction": "ascending"}]
        )

        # Compound filter
        query_database(
            database_id="abc123",
            filter={
                "and": [
                    {"property": "Status", "select": {"equals": "Active"}},
                    {"property": "Priority", "select": {"equals": "High"}}
                ]
            }
        )
    """
    data: dict[str, Any] = {"page_size": page_size}
    if filter is not None:
        data["filter"] = filter
    if sorts is not None:
        data["sorts"] = sorts
    if start_cursor is not None:
        data["start_cursor"] = start_cursor

    return get_client().post(f"/databases/{database_id}/query", data)

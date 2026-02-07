"""Shared utilities for API integrations."""

from typing import Any, Callable, TypeVar
import json

T = TypeVar("T")


def paginate(
    fetch_page: Callable[[str | None], tuple[list[T], str | None]],
    max_pages: int | None = None,
) -> list[T]:
    """
    Generic pagination helper.

    Args:
        fetch_page: Function that takes a cursor and returns (items, next_cursor).
                   next_cursor is None when there are no more pages.
        max_pages: Optional limit on number of pages to fetch.

    Returns:
        All items collected across pages.
    """
    all_items: list[T] = []
    cursor: str | None = None
    pages_fetched = 0

    while True:
        items, next_cursor = fetch_page(cursor)
        all_items.extend(items)
        pages_fetched += 1

        if next_cursor is None:
            break
        if max_pages and pages_fetched >= max_pages:
            break

        cursor = next_cursor

    return all_items


def format_output(data: Any, indent: int = 2) -> str:
    """Format data as pretty-printed JSON string."""
    return json.dumps(data, indent=indent, default=str)


class APIError(Exception):
    """Base exception for API errors."""

    def __init__(self, message: str, status_code: int | None = None, response: Any = None):
        super().__init__(message)
        self.status_code = status_code
        self.response = response

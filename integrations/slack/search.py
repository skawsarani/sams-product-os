"""Slack Search operations."""

from typing import Any
from .client import get_client


def search_messages(
    query: str,
    count: int = 20,
    page: int = 1,
    sort: str = "timestamp",
    sort_dir: str = "desc",
) -> dict[str, Any]:
    """
    Search for messages matching a query.

    Args:
        query: Search query (supports Slack search modifiers like from:, in:, has:).
        count: Number of results per page (max 100).
        page: Page number (1-indexed).
        sort: Sort field ('timestamp' or 'score').
        sort_dir: Sort direction ('asc' or 'desc').

    Returns:
        Search results with messages and pagination info.
    """
    params: dict[str, Any] = {
        "query": query,
        "count": count,
        "page": page,
        "sort": sort,
        "sort_dir": sort_dir,
    }

    result = get_client().get("search.messages", params)
    messages = result.get("messages", {})
    return {
        "matches": messages.get("matches", []),
        "total": messages.get("total", 0),
        "pagination": messages.get("pagination", {}),
    }


def search_files(
    query: str,
    count: int = 20,
    page: int = 1,
    sort: str = "timestamp",
    sort_dir: str = "desc",
) -> dict[str, Any]:
    """
    Search for files matching a query.

    Args:
        query: Search query (supports Slack search modifiers like from:, in:, type:).
        count: Number of results per page (max 100).
        page: Page number (1-indexed).
        sort: Sort field ('timestamp' or 'score').
        sort_dir: Sort direction ('asc' or 'desc').

    Returns:
        Search results with files and pagination info.
    """
    params: dict[str, Any] = {
        "query": query,
        "count": count,
        "page": page,
        "sort": sort,
        "sort_dir": sort_dir,
    }

    result = get_client().get("search.files", params)
    files = result.get("files", {})
    return {
        "matches": files.get("matches", []),
        "total": files.get("total", 0),
        "pagination": files.get("pagination", {}),
    }

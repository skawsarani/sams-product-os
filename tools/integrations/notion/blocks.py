"""Notion Blocks read operations."""

from typing import Any
from .client import get_client


def get_block(block_id: str) -> dict[str, Any]:
    """
    Get a block by ID.

    Args:
        block_id: Block ID (UUID, with or without dashes).

    Returns:
        Block data including type and content.
    """
    return get_client().get(f"/blocks/{block_id}")


def get_block_children(
    block_id: str,
    start_cursor: str | None = None,
    page_size: int = 100,
) -> dict[str, Any]:
    """
    Get child blocks of a block or page.

    Args:
        block_id: Parent block or page ID.
        start_cursor: Pagination cursor.
        page_size: Results per page (max 100).

    Returns:
        Dict with 'results' (blocks), 'has_more', and 'next_cursor'.
    """
    params: dict[str, Any] = {"page_size": page_size}
    if start_cursor:
        params["start_cursor"] = start_cursor

    return get_client().get(f"/blocks/{block_id}/children", params)

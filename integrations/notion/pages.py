"""Notion Pages read operations."""

from typing import Any
from .client import get_client


def get_page(page_id: str) -> dict[str, Any]:
    """
    Get a page by ID.

    Args:
        page_id: Page ID (UUID, with or without dashes).

    Returns:
        Page data including properties.
    """
    return get_client().get(f"/pages/{page_id}")

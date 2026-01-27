"""HubSpot CRM Line Items API."""

from typing import Any

from .search import search_objects, get_object


def search_line_items(
    query: str | None = None,
    filters: list[dict[str, Any]] | None = None,
    associated_deal: str | None = None,
    associated_quote: str | None = None,
    include_all_properties: bool = True,
    properties: list[str] | None = None,
    sorts: list[dict[str, str]] | None = None,
    limit: int = 100,
    after: str | None = None,
) -> dict[str, Any]:
    """
    Search line items with all properties and association support.

    Args:
        query: Text search across default searchable properties.
        filters: Filter objects with propertyName, operator, and value.
        associated_deal: Filter by associated deal ID.
        associated_quote: Filter by associated quote ID.
        include_all_properties: Fetch all properties including custom (default True).
        properties: Specific properties to return (overrides include_all_properties).
        sorts: Sort objects with propertyName and direction.
        limit: Maximum results (max 200).
        after: Pagination cursor.

    Returns:
        Search results with total, results list, and paging info.

    Example:
        # Find line items for a deal
        line_items = search_line_items(associated_deal="12345")
    """
    association_filters = {}
    if associated_deal:
        association_filters["deal"] = associated_deal
    if associated_quote:
        association_filters["quote"] = associated_quote

    return search_objects(
        object_type="line_items",
        query=query,
        filters=filters,
        association_filters=association_filters or None,
        properties=properties,
        include_all_properties=include_all_properties,
        sorts=sorts,
        limit=limit,
        after=after,
    )


def get_line_item(line_item_id: str) -> dict[str, Any] | None:
    """
    Get a single line item by ID with all properties.

    Args:
        line_item_id: The line item's HubSpot ID.

    Returns:
        Line item object with id, properties, createdAt, updatedAt, or None if not found.
    """
    return get_object("line_items", line_item_id)

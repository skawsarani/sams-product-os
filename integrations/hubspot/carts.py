"""HubSpot CRM Carts API."""

from typing import Any

from .search import search_objects, get_object


def search_carts(
    query: str | None = None,
    filters: list[dict[str, Any]] | None = None,
    associated_contact: str | None = None,
    include_all_properties: bool = True,
    properties: list[str] | None = None,
    sorts: list[dict[str, str]] | None = None,
    limit: int = 100,
    after: str | None = None,
) -> dict[str, Any]:
    """
    Search carts with all properties and association support.

    Args:
        query: Text search across default searchable properties.
        filters: Filter objects with propertyName, operator, and value.
        associated_contact: Filter by associated contact ID.
        include_all_properties: Fetch all properties including custom (default True).
        properties: Specific properties to return (overrides include_all_properties).
        sorts: Sort objects with propertyName and direction.
        limit: Maximum results (max 200).
        after: Pagination cursor.

    Returns:
        Search results with total, results list, and paging info.
    """
    association_filters = {}
    if associated_contact:
        association_filters["contact"] = associated_contact

    return search_objects(
        object_type="carts",
        query=query,
        filters=filters,
        association_filters=association_filters or None,
        properties=properties,
        include_all_properties=include_all_properties,
        sorts=sorts,
        limit=limit,
        after=after,
    )


def get_cart(cart_id: str) -> dict[str, Any] | None:
    """
    Get a single cart by ID with all properties.

    Args:
        cart_id: The cart's HubSpot ID.

    Returns:
        Cart object with id, properties, createdAt, updatedAt, or None if not found.
    """
    return get_object("carts", cart_id)

"""HubSpot CRM Orders API."""

from typing import Any

from .search import search_objects, get_object


def search_orders(
    query: str | None = None,
    filters: list[dict[str, Any]] | None = None,
    associated_contact: str | None = None,
    associated_company: str | None = None,
    associated_deal: str | None = None,
    include_all_properties: bool = True,
    properties: list[str] | None = None,
    sorts: list[dict[str, str]] | None = None,
    limit: int = 100,
    after: str | None = None,
) -> dict[str, Any]:
    """
    Search orders with all properties and association support.

    Args:
        query: Text search across default searchable properties.
        filters: Filter objects with propertyName, operator, and value.
        associated_contact: Filter by associated contact ID.
        associated_company: Filter by associated company ID.
        associated_deal: Filter by associated deal ID.
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
    if associated_company:
        association_filters["company"] = associated_company
    if associated_deal:
        association_filters["deal"] = associated_deal

    return search_objects(
        object_type="orders",
        query=query,
        filters=filters,
        association_filters=association_filters or None,
        properties=properties,
        include_all_properties=include_all_properties,
        sorts=sorts,
        limit=limit,
        after=after,
    )


def get_order(order_id: str) -> dict[str, Any] | None:
    """
    Get a single order by ID with all properties.

    Args:
        order_id: The order's HubSpot ID.

    Returns:
        Order object with id, properties, createdAt, updatedAt, or None if not found.
    """
    return get_object("orders", order_id)

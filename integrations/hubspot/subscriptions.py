"""HubSpot CRM Subscriptions API."""

from typing import Any

from .search import search_objects, get_object


def search_subscriptions(
    query: str | None = None,
    filters: list[dict[str, Any]] | None = None,
    associated_contact: str | None = None,
    associated_company: str | None = None,
    include_all_properties: bool = True,
    properties: list[str] | None = None,
    sorts: list[dict[str, str]] | None = None,
    limit: int = 100,
    after: str | None = None,
) -> dict[str, Any]:
    """
    Search subscriptions with all properties and association support.

    Args:
        query: Text search across default searchable properties.
        filters: Filter objects with propertyName, operator, and value.
        associated_contact: Filter by associated contact ID.
        associated_company: Filter by associated company ID.
        include_all_properties: Fetch all properties including custom (default True).
        properties: Specific properties to return (overrides include_all_properties).
        sorts: Sort objects with propertyName and direction.
        limit: Maximum results (max 200).
        after: Pagination cursor.

    Returns:
        Search results with total, results list, and paging info.

    Example:
        # Find active subscriptions
        subscriptions = search_subscriptions(
            filters=[{
                "propertyName": "hs_status",
                "operator": "EQ",
                "value": "active"
            }]
        )
    """
    association_filters = {}
    if associated_contact:
        association_filters["contact"] = associated_contact
    if associated_company:
        association_filters["company"] = associated_company

    return search_objects(
        object_type="subscriptions",
        query=query,
        filters=filters,
        association_filters=association_filters or None,
        properties=properties,
        include_all_properties=include_all_properties,
        sorts=sorts,
        limit=limit,
        after=after,
    )


def get_subscription(subscription_id: str) -> dict[str, Any] | None:
    """
    Get a single subscription by ID with all properties.

    Args:
        subscription_id: The subscription's HubSpot ID.

    Returns:
        Subscription object with id, properties, createdAt, updatedAt, or None if not found.
    """
    return get_object("subscriptions", subscription_id)

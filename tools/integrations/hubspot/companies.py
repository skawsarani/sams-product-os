"""HubSpot CRM Companies API."""

from typing import Any

from .search import search_objects, get_object


def search_companies(
    query: str | None = None,
    filters: list[dict[str, Any]] | None = None,
    associated_contact: str | None = None,
    associated_deal: str | None = None,
    include_all_properties: bool = True,
    properties: list[str] | None = None,
    sorts: list[dict[str, str]] | None = None,
    limit: int = 100,
    after: str | None = None,
) -> dict[str, Any]:
    """
    Search companies with all properties and association support.

    Args:
        query: Text search across default searchable properties.
        filters: Filter objects with propertyName, operator, and value.
        associated_contact: Filter by associated contact ID.
        associated_deal: Filter by associated deal ID.
        include_all_properties: Fetch all properties including custom (default True).
        properties: Specific properties to return (overrides include_all_properties).
        sorts: Sort objects with propertyName and direction.
        limit: Maximum results (max 200).
        after: Pagination cursor.

    Returns:
        Search results with total, results list, and paging info.

    Example:
        # Find companies with revenue > $1M
        companies = search_companies(
            filters=[{
                "propertyName": "annualrevenue",
                "operator": "GT",
                "value": "1000000"
            }]
        )
    """
    association_filters = {}
    if associated_contact:
        association_filters["contact"] = associated_contact
    if associated_deal:
        association_filters["deal"] = associated_deal

    return search_objects(
        object_type="companies",
        query=query,
        filters=filters,
        association_filters=association_filters or None,
        properties=properties,
        include_all_properties=include_all_properties,
        sorts=sorts,
        limit=limit,
        after=after,
    )


def get_company(company_id: str) -> dict[str, Any] | None:
    """
    Get a single company by ID with all properties.

    Args:
        company_id: The company's HubSpot ID.

    Returns:
        Company object with id, properties, createdAt, updatedAt, or None if not found.
    """
    return get_object("companies", company_id)

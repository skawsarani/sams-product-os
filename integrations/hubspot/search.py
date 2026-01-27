"""HubSpot CRM generic search helper.

Provides a unified search interface for all CRM object types with support for:
- Text search across default searchable properties
- Filter groups with all HubSpot operators
- Association filtering (e.g., find tickets for a contact)
- Automatic fetching of all properties (including custom)
- Pagination
"""

from typing import Any

from .client import get_client
from .properties import get_all_property_names


def search_objects(
    object_type: str,
    query: str | None = None,
    filters: list[dict[str, Any]] | None = None,
    association_filters: dict[str, str] | None = None,
    properties: list[str] | None = None,
    include_all_properties: bool = True,
    sorts: list[dict[str, str]] | None = None,
    limit: int = 100,
    after: str | None = None,
) -> dict[str, Any]:
    """
    Generic CRM object search with association and property support.

    Args:
        object_type: The CRM object type (e.g., 'contacts', 'companies', 'deals').
        query: Text search string across default searchable properties.
        filters: List of filter objects. Each filter has:
            - propertyName: Property to filter on
            - operator: EQ, NEQ, LT, LTE, GT, GTE, BETWEEN, IN, NOT_IN,
                       HAS_PROPERTY, NOT_HAS_PROPERTY, CONTAINS_TOKEN, NOT_CONTAINS_TOKEN
            - value: Filter value (for most operators)
            - values: List of values (for IN, NOT_IN)
            - highValue: Upper bound (for BETWEEN)
        association_filters: Dict mapping object type to ID for association filtering.
            Example: {"contact": "123"} finds objects associated with contact 123.
        properties: Specific properties to return. If None and include_all_properties
            is True, fetches all properties including custom ones.
        include_all_properties: If True and properties is None, fetch all properties.
            If False and properties is None, returns only default properties.
        sorts: List of sort objects with 'propertyName' and 'direction' (ASCENDING/DESCENDING).
        limit: Maximum results to return (max 200).
        after: Pagination cursor from previous response.

    Returns:
        Dict with:
        - results: List of matching objects with id, properties, createdAt, updatedAt
        - total: Total number of matching results
        - paging: Pagination info with next.after cursor if more results exist

    Example:
        # Find contacts with email containing @hubspot.com
        results = search_objects(
            "contacts",
            filters=[{
                "propertyName": "email",
                "operator": "CONTAINS_TOKEN",
                "value": "*@hubspot.com"
            }]
        )

        # Find deals associated with a specific contact
        results = search_objects(
            "deals",
            association_filters={"contact": "12345"}
        )
    """
    client = get_client()

    # Build request body
    body: dict[str, Any] = {
        "limit": min(limit, 200),  # HubSpot max is 200
    }

    # Add text search query
    if query:
        body["query"] = query

    # Build filter groups
    filter_groups: list[dict[str, Any]] = []

    # Add regular filters
    if filters:
        filter_groups.append({"filters": filters})

    # Add association filters (using associations.{type} pseudo-property)
    if association_filters:
        assoc_filters = [
            {
                "propertyName": f"associations.{obj_type}",
                "operator": "EQ",
                "value": obj_id,
            }
            for obj_type, obj_id in association_filters.items()
        ]
        if filter_groups:
            # AND with existing filters
            filter_groups[0]["filters"].extend(assoc_filters)
        else:
            filter_groups.append({"filters": assoc_filters})

    if filter_groups:
        body["filterGroups"] = filter_groups

    # Determine properties to fetch
    if properties:
        body["properties"] = properties
    elif include_all_properties:
        # Fetch all properties including custom ones
        body["properties"] = get_all_property_names(object_type)

    # Add sorting
    if sorts:
        body["sorts"] = sorts

    # Add pagination cursor
    if after:
        body["after"] = after

    # Make the search request
    endpoint = f"/crm/v3/objects/{object_type}/search"
    return client.post(endpoint, body)


def get_object(object_type: str, object_id: str) -> dict[str, Any] | None:
    """
    Get a single CRM object by ID with all properties.

    Args:
        object_type: The CRM object type (e.g., 'contacts', 'companies', 'deals').
        object_id: The object's HubSpot ID.

    Returns:
        Object dict with id, properties, createdAt, updatedAt, or None if not found.
    """
    client = get_client()

    # Get all property names to fetch all properties
    all_props = get_all_property_names(object_type)

    try:
        endpoint = f"/crm/v3/objects/{object_type}/{object_id}"
        params = {"properties": ",".join(all_props)} if all_props else None
        return client.get(endpoint, params=params)
    except Exception:
        return None

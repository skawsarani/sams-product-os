"""HubSpot CRM property definitions API.

To fetch ALL properties (including custom properties) for an object,
we first need to get the property definitions from the properties API.
"""

from functools import lru_cache
from typing import Any

from .client import get_client


def list_properties(object_type: str) -> list[dict[str, Any]]:
    """
    Get all property definitions for an object type.

    Args:
        object_type: The CRM object type (e.g., 'contacts', 'companies', 'deals').

    Returns:
        List of property definition objects with keys like:
        - name: Property internal name
        - label: Property display label
        - type: Property type (string, number, date, etc.)
        - fieldType: UI field type (text, select, checkbox, etc.)
        - groupName: Property group name
        - description: Property description
    """
    client = get_client()
    response = client.get(f"/crm/v3/properties/{object_type}")
    return response.get("results", [])


@lru_cache(maxsize=32)
def get_all_property_names(object_type: str) -> list[str]:
    """
    Get all property names for an object type.

    This is cached to avoid repeated API calls when doing multiple searches.
    Use clear_property_cache() if you need to refresh.

    Args:
        object_type: The CRM object type (e.g., 'contacts', 'companies', 'deals').

    Returns:
        List of property names (internal names) that can be used in search requests.
    """
    properties = list_properties(object_type)
    return [prop["name"] for prop in properties]


def clear_property_cache():
    """Clear the cached property names. Call this if properties have changed."""
    get_all_property_names.cache_clear()

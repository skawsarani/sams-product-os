"""Linear Initiatives read operations."""

from typing import Any
from .client import get_client


def get_initiative(initiative_id: str) -> dict[str, Any] | None:
    """
    Get an initiative by ID.

    Args:
        initiative_id: Initiative ID.

    Returns:
        Initiative data or None if not found.
    """
    query = """
    query Initiative($id: String!) {
        initiative(id: $id) {
            id
            name
            description
            owner { id name }
            targetDate
            createdAt
            updatedAt
            archivedAt
        }
    }
    """
    result = get_client().query(query, {"id": initiative_id})
    return result.get("initiative")


def list_initiatives(
    include_archived: bool = False,
    first: int = 50,
    after: str | None = None,
) -> list[dict[str, Any]]:
    """
    List initiatives.

    Args:
        include_archived: Include archived initiatives.
        first: Number of initiatives to return.
        after: Cursor for pagination.

    Returns:
        List of initiatives.
    """
    query = """
    query Initiatives($first: Int, $after: String, $includeArchived: Boolean) {
        initiatives(first: $first, after: $after, includeArchived: $includeArchived) {
            nodes {
                id
                name
                description
                owner { id name }
                targetDate
                createdAt
                updatedAt
            }
            pageInfo {
                hasNextPage
                endCursor
            }
        }
    }
    """
    variables: dict[str, Any] = {
        "first": first,
        "includeArchived": include_archived,
    }
    if after:
        variables["after"] = after

    result = get_client().query(query, variables)
    return result["initiatives"]["nodes"]

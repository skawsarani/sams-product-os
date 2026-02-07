"""Linear Cycles read operations."""

from typing import Any
from .client import get_client


def get_cycle(cycle_id: str) -> dict[str, Any] | None:
    """
    Get a cycle by ID.

    Args:
        cycle_id: Cycle ID.

    Returns:
        Cycle data or None if not found.
    """
    query = """
    query Cycle($id: String!) {
        cycle(id: $id) {
            id
            name
            description
            number
            startsAt
            endsAt
            createdAt
            updatedAt
            archivedAt
        }
    }
    """
    result = get_client().query(query, {"id": cycle_id})
    return result.get("cycle")


def list_cycles(
    team_id: str | None = None,
    include_archived: bool = False,
    first: int = 50,
    after: str | None = None,
) -> list[dict[str, Any]]:
    """
    List cycles with optional filters.

    Args:
        team_id: Filter by team ID.
        include_archived: Include archived cycles.
        first: Number of cycles to return.
        after: Cursor for pagination.

    Returns:
        List of cycles.
    """
    query = """
    query Cycles($filter: CycleFilter, $first: Int, $after: String, $includeArchived: Boolean) {
        cycles(filter: $filter, first: $first, after: $after, includeArchived: $includeArchived) {
            nodes {
                id
                name
                description
                number
                startsAt
                endsAt
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
    filter_obj: dict[str, Any] = {}
    if team_id:
        filter_obj["team"] = {"id": {"eq": team_id}}

    variables: dict[str, Any] = {
        "first": first,
        "includeArchived": include_archived,
    }
    if filter_obj:
        variables["filter"] = filter_obj
    if after:
        variables["after"] = after

    result = get_client().query(query, variables)
    return result["cycles"]["nodes"]

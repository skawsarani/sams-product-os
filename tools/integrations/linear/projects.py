"""Linear Projects read operations."""

from typing import Any
from .client import get_client


def get_project(project_id: str) -> dict[str, Any] | None:
    """
    Get a project by ID.

    Args:
        project_id: Project ID.

    Returns:
        Project data or None if not found.
    """
    query = """
    query Project($id: String!) {
        project(id: $id) {
            id
            name
            description
            state
            lead { id name }
            startDate
            targetDate
            createdAt
            updatedAt
            archivedAt
        }
    }
    """
    result = get_client().query(query, {"id": project_id})
    return result.get("project")


def list_projects(
    team_id: str | None = None,
    state: str | None = None,
    include_archived: bool = False,
    first: int = 50,
    after: str | None = None,
) -> list[dict[str, Any]]:
    """
    List projects with optional filters.

    Args:
        team_id: Filter by team ID.
        state: Filter by state (planned, started, paused, completed, canceled).
        include_archived: Include archived projects.
        first: Number of projects to return.
        after: Cursor for pagination.

    Returns:
        List of projects.
    """
    query = """
    query Projects($filter: ProjectFilter, $first: Int, $after: String, $includeArchived: Boolean) {
        projects(filter: $filter, first: $first, after: $after, includeArchived: $includeArchived) {
            nodes {
                id
                name
                description
                state
                lead { id name }
                startDate
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
    filter_obj: dict[str, Any] = {}
    if team_id:
        filter_obj["accessibleTeams"] = {"id": {"eq": team_id}}
    if state:
        filter_obj["state"] = {"eq": state}

    variables: dict[str, Any] = {
        "first": first,
        "includeArchived": include_archived,
    }
    if filter_obj:
        variables["filter"] = filter_obj
    if after:
        variables["after"] = after

    result = get_client().query(query, variables)
    return result["projects"]["nodes"]

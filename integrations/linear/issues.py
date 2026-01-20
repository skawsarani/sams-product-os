"""Linear Issues read operations."""

from typing import Any
from .client import get_client


def get_issue(issue_id: str) -> dict[str, Any] | None:
    """
    Get an issue by ID.

    Args:
        issue_id: Issue ID (UUID or identifier like BLA-123).

    Returns:
        Issue data or None if not found.
    """
    query = """
    query Issue($id: String!) {
        issue(id: $id) {
            id
            identifier
            title
            description
            priority
            state { id name }
            assignee { id name }
            project { id name }
            labels { nodes { id name } }
            cycle { id name }
            createdAt
            updatedAt
            archivedAt
        }
    }
    """
    result = get_client().query(query, {"id": issue_id})
    return result.get("issue")


def list_issues(
    team_id: str | None = None,
    project_id: str | None = None,
    state_id: str | None = None,
    assignee_id: str | None = None,
    include_archived: bool = False,
    first: int = 50,
    after: str | None = None,
) -> list[dict[str, Any]]:
    """
    List issues with optional filters.

    Args:
        team_id: Filter by team ID.
        project_id: Filter by project ID.
        state_id: Filter by state ID.
        assignee_id: Filter by assignee ID.
        include_archived: Include archived issues.
        first: Number of issues to return (max 250).
        after: Cursor for pagination.

    Returns:
        List of issues.
    """
    query = """
    query Issues($filter: IssueFilter, $first: Int, $after: String, $includeArchived: Boolean) {
        issues(filter: $filter, first: $first, after: $after, includeArchived: $includeArchived) {
            nodes {
                id
                identifier
                title
                description
                priority
                state { id name }
                assignee { id name }
                project { id name }
                labels { nodes { id name } }
                cycle { id name }
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
    if project_id:
        filter_obj["project"] = {"id": {"eq": project_id}}
    if state_id:
        filter_obj["state"] = {"id": {"eq": state_id}}
    if assignee_id:
        filter_obj["assignee"] = {"id": {"eq": assignee_id}}

    variables: dict[str, Any] = {
        "first": first,
        "includeArchived": include_archived,
    }
    if filter_obj:
        variables["filter"] = filter_obj
    if after:
        variables["after"] = after

    result = get_client().query(query, variables)
    return result["issues"]["nodes"]

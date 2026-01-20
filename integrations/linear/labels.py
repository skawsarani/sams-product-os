"""Linear Labels read operations."""

from typing import Any
from .client import get_client


def get_label(label_id: str) -> dict[str, Any] | None:
    """
    Get a label by ID.

    Args:
        label_id: Label ID.

    Returns:
        Label data or None if not found.
    """
    query = """
    query IssueLabel($id: String!) {
        issueLabel(id: $id) {
            id
            name
            color
            description
            createdAt
            updatedAt
            archivedAt
        }
    }
    """
    result = get_client().query(query, {"id": label_id})
    return result.get("issueLabel")


def list_labels(
    team_id: str | None = None,
    include_archived: bool = False,
    first: int = 50,
    after: str | None = None,
) -> list[dict[str, Any]]:
    """
    List labels with optional filters.

    Args:
        team_id: Filter by team ID.
        include_archived: Include archived labels.
        first: Number of labels to return.
        after: Cursor for pagination.

    Returns:
        List of labels.
    """
    query = """
    query IssueLabels($filter: IssueLabelFilter, $first: Int, $after: String, $includeArchived: Boolean) {
        issueLabels(filter: $filter, first: $first, after: $after, includeArchived: $includeArchived) {
            nodes {
                id
                name
                color
                description
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
    return result["issueLabels"]["nodes"]

"""Linear Comments read operations."""

from typing import Any
from .client import get_client


def get_comment(comment_id: str) -> dict[str, Any] | None:
    """
    Get a comment by ID.

    Args:
        comment_id: Comment ID.

    Returns:
        Comment data or None if not found.
    """
    query = """
    query Comment($id: String!) {
        comment(id: $id) {
            id
            body
            user { id name }
            issue { id identifier }
            createdAt
            updatedAt
        }
    }
    """
    result = get_client().query(query, {"id": comment_id})
    return result.get("comment")


def list_comments(
    issue_id: str | None = None,
    first: int = 50,
    after: str | None = None,
) -> list[dict[str, Any]]:
    """
    List comments with optional filters.

    Args:
        issue_id: Filter by issue ID.
        first: Number of comments to return.
        after: Cursor for pagination.

    Returns:
        List of comments.
    """
    query = """
    query Comments($filter: CommentFilter, $first: Int, $after: String) {
        comments(filter: $filter, first: $first, after: $after) {
            nodes {
                id
                body
                user { id name }
                issue { id identifier }
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
    if issue_id:
        filter_obj["issue"] = {"id": {"eq": issue_id}}

    variables: dict[str, Any] = {"first": first}
    if filter_obj:
        variables["filter"] = filter_obj
    if after:
        variables["after"] = after

    result = get_client().query(query, variables)
    return result["comments"]["nodes"]

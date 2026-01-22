"""Linear Customers read operations (includes customer needs)."""

from typing import Any
from .client import get_client


def get_customer(customer_id: str, include_needs: bool = False, needs_first: int = 50) -> dict[str, Any] | None:
    """Get a customer by ID, optionally with their needs.

    Args:
        customer_id: The customer's unique identifier.
        include_needs: If True, also fetch customer needs.
        needs_first: Max needs to fetch (default 50).

    Returns:
        Customer dict with embedded 'tier', 'status', 'owner'.
        If include_needs=True, also includes 'needs' list.
        Returns None if not found.
    """
    if include_needs:
        # Single query with multiple root fields
        query = """
        query CustomerWithNeeds($id: String!, $needsFilter: CustomerNeedFilter, $needsFirst: Int) {
            customer(id: $id) {
                id
                name
                logoUrl
                domains
                revenue
                size
                approximateNeedCount
                slackChannelId
                url
                owner { id name email }
                status { id name color }
                tier { id name color description }
                createdAt
                updatedAt
                archivedAt
            }
            customerNeeds(filter: $needsFilter, first: $needsFirst) {
                nodes {
                    id
                    body
                    priority
                    url
                    issue { id identifier title state { name } }
                    project { id name }
                    creator { id name }
                    createdAt
                }
            }
        }
        """
        result = get_client().query(query, {
            "id": customer_id,
            "needsFilter": {"customer": {"id": {"eq": customer_id}}},
            "needsFirst": needs_first,
        })
        customer = result.get("customer")
        if customer:
            customer["needs"] = result.get("customerNeeds", {}).get("nodes", [])
        return customer
    else:
        query = """
        query Customer($id: String!) {
            customer(id: $id) {
                id
                name
                logoUrl
                domains
                revenue
                size
                approximateNeedCount
                slackChannelId
                url
                owner { id name email }
                status { id name color }
                tier { id name color description }
                createdAt
                updatedAt
                archivedAt
            }
        }
        """
        result = get_client().query(query, {"id": customer_id})
        return result.get("customer")


def list_customers(
    tier_id: str | None = None,
    status_id: str | None = None,
    owner_id: str | None = None,
    include_archived: bool = False,
    first: int = 50,
    after: str | None = None,
) -> list[dict[str, Any]]:
    """List customers with optional filters.

    Each customer includes embedded tier, status, and owner.

    Args:
        tier_id: Filter by customer tier ID.
        status_id: Filter by customer status ID.
        owner_id: Filter by owner (account manager) ID.
        include_archived: Include archived customers.
        first: Maximum number of results.
        after: Pagination cursor.

    Returns:
        List of customer dicts.
    """
    query = """
    query Customers($filter: CustomerFilter, $first: Int, $after: String, $includeArchived: Boolean) {
        customers(filter: $filter, first: $first, after: $after, includeArchived: $includeArchived) {
            nodes {
                id
                name
                logoUrl
                domains
                revenue
                size
                approximateNeedCount
                url
                owner { id name }
                status { id name color }
                tier { id name color }
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
    if tier_id:
        filter_obj["tier"] = {"id": {"eq": tier_id}}
    if status_id:
        filter_obj["status"] = {"id": {"eq": status_id}}
    if owner_id:
        filter_obj["owner"] = {"id": {"eq": owner_id}}

    variables: dict[str, Any] = {
        "first": first,
        "includeArchived": include_archived,
    }
    if filter_obj:
        variables["filter"] = filter_obj
    if after:
        variables["after"] = after

    result = get_client().query(query, variables)
    return result["customers"]["nodes"]


def list_customer_needs(
    customer_id: str | None = None,
    issue_id: str | None = None,
    project_id: str | None = None,
    important_only: bool = False,
    include_archived: bool = False,
    first: int = 50,
    after: str | None = None,
) -> list[dict[str, Any]]:
    """List customer needs with optional filters.

    Args:
        customer_id: Filter by customer ID.
        issue_id: Filter by linked issue ID.
        project_id: Filter by linked project ID.
        important_only: Only return needs with priority=1 (important).
        include_archived: Include archived needs.
        first: Maximum number of results.
        after: Pagination cursor.

    Returns:
        List of customer need dicts.
    """
    query = """
    query CustomerNeeds($filter: CustomerNeedFilter, $first: Int, $after: String, $includeArchived: Boolean) {
        customerNeeds(filter: $filter, first: $first, after: $after, includeArchived: $includeArchived) {
            nodes {
                id
                body
                priority
                url
                customer { id name tier { id name } }
                issue { id identifier title state { name } }
                project { id name }
                creator { id name }
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
    if customer_id:
        filter_obj["customer"] = {"id": {"eq": customer_id}}
    if issue_id:
        filter_obj["issue"] = {"id": {"eq": issue_id}}
    if project_id:
        filter_obj["project"] = {"id": {"eq": project_id}}
    if important_only:
        filter_obj["priority"] = {"eq": 1}

    variables: dict[str, Any] = {
        "first": first,
        "includeArchived": include_archived,
    }
    if filter_obj:
        variables["filter"] = filter_obj
    if after:
        variables["after"] = after

    result = get_client().query(query, variables)
    return result["customerNeeds"]["nodes"]

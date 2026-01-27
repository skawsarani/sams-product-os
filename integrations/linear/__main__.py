"""CLI interface for Linear integration.

Usage:
    uv run python -m integrations.linear <command> [options]

Commands:
    list-issues         List issues (filter only, no text search)
    get-issue           Get issue by ID or identifier
    list-customers      List customers
    get-customer        Get customer by ID
    list-customer-needs List customer needs
"""

import argparse
import json
import sys

from . import (
    list_issues,
    get_issue,
    list_customers,
    get_customer,
    list_customer_needs,
)


def cmd_list_issues(args: argparse.Namespace) -> None:
    """List issues."""
    result = list_issues(
        team_id=args.team_id,
        project_id=args.project_id,
        state_id=args.state_id,
        assignee_id=args.assignee_id,
        include_archived=args.include_archived,
        first=args.first,
        after=args.after,
    )
    print(json.dumps(result, indent=2, default=str))


def cmd_get_issue(args: argparse.Namespace) -> None:
    """Get issue by ID."""
    result = get_issue(args.id)
    print(json.dumps(result, indent=2, default=str))


def cmd_list_customers(args: argparse.Namespace) -> None:
    """List customers."""
    result = list_customers(
        tier_id=args.tier_id,
        status_id=args.status_id,
        owner_id=args.owner_id,
        include_archived=args.include_archived,
        first=args.first,
        after=args.after,
    )
    print(json.dumps(result, indent=2, default=str))


def cmd_get_customer(args: argparse.Namespace) -> None:
    """Get customer by ID."""
    result = get_customer(
        customer_id=args.id,
        include_needs=args.include_needs,
        needs_first=args.needs_first,
    )
    print(json.dumps(result, indent=2, default=str))


def cmd_list_customer_needs(args: argparse.Namespace) -> None:
    """List customer needs."""
    result = list_customer_needs(
        customer_id=args.customer_id,
        issue_id=args.issue_id,
        project_id=args.project_id,
        important_only=args.important_only,
        include_archived=args.include_archived,
        first=args.first,
        after=args.after,
    )
    print(json.dumps(result, indent=2, default=str))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Linear integration CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # list-issues
    p_issues = subparsers.add_parser("list-issues", help="List issues (filter only)")
    p_issues.add_argument("--team-id", help="Filter by team ID")
    p_issues.add_argument("--project-id", help="Filter by project ID")
    p_issues.add_argument("--state-id", help="Filter by state ID")
    p_issues.add_argument("--assignee-id", help="Filter by assignee ID")
    p_issues.add_argument("--include-archived", action="store_true", help="Include archived")
    p_issues.add_argument("--first", type=int, default=50, help="Max results (max 250)")
    p_issues.add_argument("--after", help="Pagination cursor")
    p_issues.set_defaults(func=cmd_list_issues)

    # get-issue
    p_get_issue = subparsers.add_parser("get-issue", help="Get issue by ID or identifier")
    p_get_issue.add_argument("--id", required=True, help="Issue ID or identifier (e.g., ENG-123)")
    p_get_issue.set_defaults(func=cmd_get_issue)

    # list-customers
    p_customers = subparsers.add_parser("list-customers", help="List customers")
    p_customers.add_argument("--tier-id", help="Filter by tier ID")
    p_customers.add_argument("--status-id", help="Filter by status ID")
    p_customers.add_argument("--owner-id", help="Filter by owner ID")
    p_customers.add_argument("--include-archived", action="store_true", help="Include archived")
    p_customers.add_argument("--first", type=int, default=50, help="Max results")
    p_customers.add_argument("--after", help="Pagination cursor")
    p_customers.set_defaults(func=cmd_list_customers)

    # get-customer
    p_get_customer = subparsers.add_parser("get-customer", help="Get customer by ID")
    p_get_customer.add_argument("--id", required=True, help="Customer ID")
    p_get_customer.add_argument("--include-needs", action="store_true", help="Include customer needs")
    p_get_customer.add_argument("--needs-first", type=int, default=50, help="Max needs to fetch")
    p_get_customer.set_defaults(func=cmd_get_customer)

    # list-customer-needs
    p_needs = subparsers.add_parser("list-customer-needs", help="List customer needs")
    p_needs.add_argument("--customer-id", help="Filter by customer ID")
    p_needs.add_argument("--issue-id", help="Filter by issue ID")
    p_needs.add_argument("--project-id", help="Filter by project ID")
    p_needs.add_argument("--important-only", action="store_true", help="Only priority=1 needs")
    p_needs.add_argument("--include-archived", action="store_true", help="Include archived")
    p_needs.add_argument("--first", type=int, default=50, help="Max results")
    p_needs.add_argument("--after", help="Pagination cursor")
    p_needs.set_defaults(func=cmd_list_customer_needs)

    args = parser.parse_args()

    try:
        args.func(args)
        return 0
    except Exception as e:
        print(json.dumps({"error": str(e)}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())

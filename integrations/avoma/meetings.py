"""Avoma Meetings operations."""

import time
from datetime import datetime, timedelta
from typing import Any

import httpx

from .client import get_client, BASE_URL
from ..common.config import get_avoma_api_key


def get_meeting(meeting_id: str) -> dict[str, Any] | None:
    """
    Get meeting details by ID.

    Args:
        meeting_id: Meeting ID.

    Returns:
        Meeting data or None if not found.
    """
    try:
        return get_client().get(f"/meetings/{meeting_id}")
    except Exception:
        return None


def list_meetings(
    limit: int = 20,
    offset: int = 0,
    from_date: str | None = None,
    to_date: str | None = None,
    status: str | None = None,
    scope: str = "all",
) -> dict[str, Any]:
    """
    List meetings.

    Args:
        limit: Number of meetings to return (max 100).
        offset: Offset for pagination.
        from_date: Start date filter (YYYY-MM-DD). Defaults to 30 days ago.
        to_date: End date filter (YYYY-MM-DD). Defaults to today.
        status: Filter by status (e.g., 'completed', 'scheduled').
        scope: Meeting scope - "all" for all accessible meetings, "team" for team
               meetings, "mine" for only your meetings. Defaults to "all".

    Returns:
        Dict with 'meetings' list and pagination info.

    Example:
        # List all accessible meetings (last 30 days)
        list_meetings(limit=10)

        # List only team meetings
        list_meetings(limit=10, scope="team")

        # List meetings in date range
        list_meetings(from_date="2026-01-01", to_date="2026-01-31")
    """
    # Avoma API requires from_date and to_date
    if not from_date:
        from_date = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d")
    if not to_date:
        to_date = datetime.now().strftime("%Y-%m-%d")

    params: dict[str, Any] = {
        "limit": limit,
        "offset": offset,
        "from_date": from_date,
        "to_date": to_date,
    }

    if status:
        params["status"] = status

    # Add scope parameter to fetch all/team/personal meetings
    if scope:
        params["scope"] = scope

    result = get_client().get("/meetings", params)

    # Handle both list and dict responses
    if isinstance(result, list):
        return {"meetings": result, "total": len(result)}

    return {
        "meetings": result.get("meetings", result.get("results", result.get("data", []))),
        "total": result.get("total", result.get("count", 0)),
        "offset": offset,
        "limit": limit,
    }


def search_meetings(
    query: str,
    max_results: int = 10,
    from_date: str | None = None,
    to_date: str | None = None,
    scope: str = "all",
    case_sensitive: bool = False,
) -> list[dict[str, Any]]:
    """
    Search meetings by subject (client-side filtering).

    Since the Avoma API doesn't support server-side subject filtering,
    this function paginates through meetings and filters by subject locally.

    Args:
        query: Search term to match in meeting subject.
        max_results: Maximum number of matching meetings to return (default 10).
        from_date: Start date filter (YYYY-MM-DD). Defaults to 90 days ago.
        to_date: End date filter (YYYY-MM-DD). Defaults to today.
        scope: Meeting scope - "all", "team", or "mine". Defaults to "all".
        case_sensitive: Whether search should be case-sensitive. Defaults to False.

    Returns:
        List of meetings matching the query.

    Example:
        # Find meetings with "Interac" in subject
        meetings = search_meetings("Interac", max_results=5)
        for m in meetings:
            print(f"{m['subject']} - {m['start_at']}")
    """
    if not from_date:
        from_date = (datetime.now() - timedelta(days=90)).strftime("%Y-%m-%d")
    if not to_date:
        to_date = datetime.now().strftime("%Y-%m-%d")

    api_key = get_avoma_api_key()
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    matches: list[dict[str, Any]] = []
    page = 1
    max_pages = 50  # Safety limit

    search_term = query if case_sensitive else query.lower()

    with httpx.Client(timeout=60.0, follow_redirects=True) as client:
        while len(matches) < max_results and page <= max_pages:
            response = client.get(
                f"{BASE_URL}/meetings",
                headers=headers,
                params={
                    "from_date": from_date,
                    "to_date": to_date,
                    "limit": 50,
                    "page": page,
                    "scope": scope,
                },
            )

            if response.status_code == 429:
                time.sleep(5)
                continue

            if response.status_code != 200:
                break

            data = response.json()
            meetings = data.get("results", [])

            if not meetings:
                break

            for meeting in meetings:
                subject = meeting.get("subject", "")
                compare_subject = subject if case_sensitive else subject.lower()

                if search_term in compare_subject:
                    matches.append(meeting)
                    if len(matches) >= max_results:
                        break

            if not data.get("next"):
                break

            page += 1
            time.sleep(0.2)  # Rate limit protection

    return matches

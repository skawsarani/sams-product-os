"""Google Calendar Events read operations."""

from typing import Any
from datetime import datetime, timezone

from .client import get_service


def get_event(calendar_id: str, event_id: str) -> dict[str, Any] | None:
    """
    Get an event by ID.

    Args:
        calendar_id: Calendar ID.
        event_id: Event ID.

    Returns:
        Event data or None if not found.
    """
    try:
        return get_service().events().get(calendarId=calendar_id, eventId=event_id).execute()
    except Exception:
        return None


def list_events(
    calendar_id: str,
    time_min: str | datetime | None = None,
    time_max: str | datetime | None = None,
    max_results: int = 100,
    single_events: bool = True,
    order_by: str = "startTime",
    page_token: str | None = None,
    q: str | None = None,
) -> dict[str, Any]:
    """
    List events in a calendar.

    Args:
        calendar_id: Calendar ID ('primary' for default).
        time_min: Lower bound for event start (default: now).
        time_max: Upper bound for event start.
        max_results: Maximum number of events (max 2500).
        single_events: Expand recurring events into instances.
        order_by: Sort order ('startTime' or 'updated'). Requires single_events=True for startTime.
        page_token: Pagination token.
        q: Free text search query.

    Returns:
        Dict with 'items' (events) and pagination info.
    """
    # Default to current time if not specified
    if time_min is None:
        time_min = datetime.now(timezone.utc).isoformat()
    elif isinstance(time_min, datetime):
        time_min = time_min.isoformat()

    if isinstance(time_max, datetime):
        time_max = time_max.isoformat()

    params: dict[str, Any] = {
        "calendarId": calendar_id,
        "timeMin": time_min,
        "maxResults": max_results,
        "singleEvents": single_events,
        "orderBy": order_by,
    }

    if time_max:
        params["timeMax"] = time_max
    if page_token:
        params["pageToken"] = page_token
    if q:
        params["q"] = q

    result = get_service().events().list(**params).execute()

    return {
        "items": result.get("items", []),
        "nextPageToken": result.get("nextPageToken"),
        "summary": result.get("summary"),
    }

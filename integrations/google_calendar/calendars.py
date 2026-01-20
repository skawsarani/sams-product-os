"""Google Calendar Calendars operations."""

from typing import Any

from .client import get_service


def get_calendar(calendar_id: str) -> dict[str, Any] | None:
    """
    Get calendar metadata.

    Args:
        calendar_id: Calendar ID ('primary' for default calendar).

    Returns:
        Calendar data or None if not found.
    """
    try:
        return get_service().calendars().get(calendarId=calendar_id).execute()
    except Exception:
        return None


def list_calendars(
    max_results: int = 100,
    page_token: str | None = None,
    show_hidden: bool = False,
) -> dict[str, Any]:
    """
    List calendars accessible to the authenticated user.

    Args:
        max_results: Maximum number of calendars to return.
        page_token: Pagination token.
        show_hidden: Include hidden calendars.

    Returns:
        Dict with 'items' (calendars) and pagination info.

    Note:
        Shows calendars the authenticated user has access to.
    """
    params: dict[str, Any] = {
        "maxResults": max_results,
        "showHidden": show_hidden,
    }

    if page_token:
        params["pageToken"] = page_token

    result = get_service().calendarList().list(**params).execute()

    return {
        "items": result.get("items", []),
        "nextPageToken": result.get("nextPageToken"),
    }

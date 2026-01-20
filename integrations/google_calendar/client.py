"""Google Calendar API client."""

from googleapiclient.discovery import Resource

from ..common.google_auth import build_calendar_service

# Default client instance (lazy initialization)
_default_service: Resource | None = None


def get_service() -> Resource:
    """Get or create the default Google Calendar service."""
    global _default_service
    if _default_service is None:
        _default_service = build_calendar_service()
    return _default_service

"""Google Drive API client."""

from googleapiclient.discovery import Resource

from ..common.google_auth import build_drive_service

# Default client instance (lazy initialization)
_default_service: Resource | None = None


def get_service() -> Resource:
    """Get or create the default Google Drive service."""
    global _default_service
    if _default_service is None:
        _default_service = build_drive_service()
    return _default_service

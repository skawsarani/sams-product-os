"""Avoma Notes operations."""

from typing import Any

from .client import get_client


def get_notes(meeting_uuid: str) -> dict[str, Any] | None:
    """
    Get AI-generated notes/insights for a meeting.

    This first fetches meeting details to check if notes are ready,
    then retrieves the insights data from the /meetings/{uuid}/insights endpoint.

    Args:
        meeting_uuid: Meeting UUID.

    Returns:
        Notes/insights data including ai_notes, action items, etc., or None if not available.
        Returns None if notes are not ready or don't exist.

    Example:
        notes = get_notes(meeting_uuid="abc123-...")
        if notes:
            for note in notes.get("ai_notes", []):
                print(f"[{note.get('note_type')}] {note.get('text')}")
    """
    try:
        client = get_client()
        meeting = client.get(f"/meetings/{meeting_uuid}")

        # Check if notes are ready
        if not meeting.get("notes_ready", False):
            return None

        # Get insights which contains AI notes
        return client.get(f"/meetings/{meeting_uuid}/insights")
    except Exception:
        return None


def get_meeting_insights(meeting_uuid: str) -> dict[str, Any] | None:
    """
    Get meeting insights directly without checking notes_ready.

    Use this if you want to try fetching insights regardless of the notes_ready flag.

    Args:
        meeting_uuid: Meeting UUID.

    Returns:
        Insights data containing ai_notes, or None if not found.
    """
    try:
        return get_client().get(f"/meetings/{meeting_uuid}/insights")
    except Exception:
        return None

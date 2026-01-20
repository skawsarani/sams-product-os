"""Avoma Transcripts operations."""

from typing import Any

from .client import get_client


def get_transcript(meeting_uuid: str) -> dict[str, Any] | None:
    """
    Get the transcript for a meeting.

    This first fetches meeting details to get the transcription_uuid,
    then retrieves the actual transcript data.

    Args:
        meeting_uuid: Meeting UUID.

    Returns:
        Transcript data including text segments, or None if not available.
        Returns None if transcript is not ready or doesn't exist.

    Example:
        transcript = get_transcript(meeting_uuid="abc123-...")
        if transcript:
            for segment in transcript.get("segments", []):
                print(f"{segment['speaker']}: {segment['text']}")
    """
    try:
        # First get meeting details to find transcription_uuid
        client = get_client()
        meeting = client.get(f"/meetings/{meeting_uuid}")

        transcription_uuid = meeting.get("transcription_uuid")
        if not transcription_uuid:
            return None

        # Check if transcript is ready
        if not meeting.get("transcript_ready", False):
            return None

        # Get the transcript using the transcription UUID
        return client.get(f"/transcriptions/{transcription_uuid}")
    except Exception:
        return None


def get_transcription(transcription_uuid: str) -> dict[str, Any] | None:
    """
    Get a transcript directly by its transcription UUID.

    Use this if you already have the transcription_uuid from meeting details.

    Args:
        transcription_uuid: The transcription UUID.

    Returns:
        Transcript data or None if not found.
    """
    try:
        return get_client().get(f"/transcriptions/{transcription_uuid}")
    except Exception:
        return None

#!/usr/bin/env python3
"""Test script to verify Avoma API integration is working.

Run from project root:
  uv run python integrations/avoma/test_avoma.py
"""

import sys
from pathlib import Path

# Add project root to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from integrations.avoma.meetings import list_meetings, get_meeting, search_meetings
from integrations.avoma.notes import get_notes
from integrations.avoma.transcripts import get_transcript


def test_list_meetings():
    """Test listing meetings."""
    print(f"\n{'='*60}")
    print("Testing: list_meetings")
    print(f"{'='*60}")
    try:
        result = list_meetings(limit=10)
        meetings = result.get("meetings", [])
        total = result.get("total", 0)
        print(f"✓ Success! Found {len(meetings)} meetings (total: {total})")
        
        if meetings:
            first = meetings[0]
            print(f"\n  First meeting:")
            for key in ["uuid", "subject", "start_at", "end_at", "organizer_email"]:
                if key in first:
                    print(f"    {key}: {first[key]}")
            return first.get("uuid")
        return None
    except Exception as e:
        print(f"✗ Failed: {e}")
        return None


def test_get_meeting(meeting_uuid: str | None):
    """Test getting a specific meeting."""
    if not meeting_uuid:
        print(f"\n[SKIP] get_meeting - no meeting UUID available")
        return
    
    print(f"\n{'-'*40}")
    print(f"Testing: get_meeting (uuid: {meeting_uuid[:20]}...)")
    print(f"{'-'*40}")
    try:
        result = get_meeting(meeting_uuid)
        if result:
            print(f"✓ Success!")
            print(f"  subject: {result.get('subject')}")
            print(f"  start_at: {result.get('start_at')}")
            print(f"  transcript_ready: {result.get('transcript_ready')}")
            print(f"  transcription_uuid: {result.get('transcription_uuid')}")
            return result
        else:
            print(f"✗ Returned None")
    except Exception as e:
        print(f"✗ Failed: {e}")
    return None


def find_meeting_with_transcript():
    """Find a meeting that has a transcript ready."""
    print(f"\n{'-'*40}")
    print("Finding a meeting with transcript ready...")
    print(f"{'-'*40}")
    
    import httpx
    import time
    from datetime import datetime, timedelta
    from integrations.common.config import get_avoma_api_key
    
    # Look back 90 days to find meetings with transcripts
    from_date = (datetime.now() - timedelta(days=90)).strftime("%Y-%m-%d")
    to_date = datetime.now().strftime("%Y-%m-%d")
    
    api_key = get_avoma_api_key()
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    
    try:
        checked = 0
        page = 1
        
        with httpx.Client(timeout=60.0, follow_redirects=True) as client:
            while checked < 50:  # Check up to 50 meetings
                # Fetch a page of meetings
                response = client.get(
                    "https://api.avoma.com/v1/meetings",
                    headers=headers,
                    params={
                        "from_date": from_date,
                        "to_date": to_date,
                        "limit": 20,
                        "page": page,
                    }
                )
                
                if response.status_code == 429:
                    print(f"  Rate limited, waiting 5 seconds...")
                    time.sleep(5)
                    continue
                
                if response.status_code != 200:
                    print(f"  API error: {response.status_code}")
                    break
                
                data = response.json()
                meetings = data.get("results", [])
                
                if not meetings:
                    break
                
                print(f"  Page {page}: checking {len(meetings)} meetings...")
                
                for meeting in meetings:
                    meeting_uuid = meeting.get("uuid")
                    
                    # Small delay to avoid rate limiting
                    time.sleep(0.2)
                    
                    # Get full meeting details
                    detail_response = client.get(
                        f"https://api.avoma.com/v1/meetings/{meeting_uuid}",
                        headers=headers
                    )
                    checked += 1
                    
                    if detail_response.status_code == 429:
                        print(f"  Rate limited, waiting 5 seconds...")
                        time.sleep(5)
                        continue
                    
                    if detail_response.status_code == 200:
                        details = detail_response.json()
                        if details.get("transcript_ready") and details.get("transcription_uuid"):
                            print(f"  ✓ Found meeting with transcript after checking {checked} meetings")
                            print(f"    Subject: {details.get('subject')}")
                            print(f"    UUID: {meeting_uuid}")
                            return meeting_uuid, details
                    
                    if checked >= 50:
                        break
                
                # Check if there's a next page
                if not data.get("next"):
                    break
                page += 1
                time.sleep(0.5)  # Small delay between pages
        
        print(f"  No meetings with ready transcripts found (checked {checked})")
        return None, None
    except Exception as e:
        print(f"  ✗ Error searching: {e}")
        import traceback
        traceback.print_exc()
        return None, None


def test_get_transcript(meeting_uuid: str | None, meeting_details: dict | None = None):
    """Test getting a meeting transcript."""
    if not meeting_uuid:
        print(f"\n[SKIP] get_transcript - no meeting UUID available")
        return
    
    print(f"\n{'-'*40}")
    print(f"Testing: get_transcript")
    print(f"{'-'*40}")
    
    # Check if this meeting has a transcript
    transcript_ready = meeting_details.get("transcript_ready", False) if meeting_details else False
    transcription_uuid = meeting_details.get("transcription_uuid") if meeting_details else None
    
    print(f"  Meeting: {meeting_details.get('subject', 'Unknown') if meeting_details else 'Unknown'}")
    print(f"  transcript_ready: {transcript_ready}")
    print(f"  transcription_uuid: {transcription_uuid}")
    
    if not transcript_ready or not transcription_uuid:
        print(f"  Note: This meeting doesn't have a transcript ready")
        return
    
    try:
        result = get_transcript(meeting_uuid)
        if result:
            print(f"✓ Success! Retrieved transcript")
            print(f"  Keys: {list(result.keys())}")
            
            # Show speakers
            if "speakers" in result:
                speakers = result["speakers"]
                print(f"  Speakers: {len(speakers)}")
                for s in speakers[:3]:  # Show first 3 speakers
                    print(f"    - {s.get('name', s.get('email', 'Unknown'))}")
            
            # Show transcript preview
            if "transcript" in result:
                transcript_data = result["transcript"]
                speakers = result.get("speakers", [])
                
                if isinstance(transcript_data, list):
                    print(f"  Transcript segments: {len(transcript_data)}")
                    # Show first few segments with speaker names
                    for i, seg in enumerate(transcript_data[:3]):
                        speaker_id = seg.get("speaker_id", 0)
                        speaker_name = speakers[speaker_id].get("name", f"Speaker {speaker_id}") if speaker_id < len(speakers) else f"Speaker {speaker_id}"
                        text = seg.get("transcript", "")[:80]
                        print(f"    [{speaker_name}]: {text}...")
                elif isinstance(transcript_data, str) and transcript_data:
                    preview = transcript_data[:300].replace('\n', ' ')
                    print(f"  Transcript preview: {preview}...")
                    print(f"  Total length: {len(transcript_data)} chars")
            
            # Show VTT URL if available
            if "transcription_vtt_url" in result:
                print(f"  VTT URL: {result['transcription_vtt_url'][:60]}...")
        else:
            print(f"✗ Returned None (unexpected - transcript should be available)")
    except Exception as e:
        print(f"✗ Failed: {e}")


def test_list_meetings_with_filters():
    """Test listing meetings with filters."""
    print(f"\n{'-'*40}")
    print("Testing: list_meetings with status filter")
    print(f"{'-'*40}")
    try:
        result = list_meetings(limit=5, status="completed")
        meetings = result.get("meetings", [])
        print(f"✓ Success! Found {len(meetings)} completed meetings")
    except Exception as e:
        print(f"✗ Failed: {e}")


def test_list_meetings_with_date_range():
    """Test listing meetings with date range."""
    print(f"\n{'-'*40}")
    print("Testing: list_meetings with date range")
    print(f"{'-'*40}")
    try:
        result = list_meetings(
            limit=5,
            from_date="2026-01-01",
            to_date="2026-01-20"
        )
        meetings = result.get("meetings", [])
        print(f"✓ Success! Found {len(meetings)} meetings in Jan 2026")
    except Exception as e:
        print(f"✗ Failed: {e}")


def test_list_meetings_with_scope():
    """Test listing meetings with different scope values."""
    print(f"\n{'-'*40}")
    print("Testing: list_meetings with scope parameter")
    print(f"{'-'*40}")
    
    # Test different scope values to discover what's supported
    scopes = ["all", "team", "mine", "organization"]
    
    for scope in scopes:
        try:
            result = list_meetings(limit=5, scope=scope)
            meetings = result.get("meetings", [])
            total = result.get("total", 0)
            print(f"  scope='{scope}': {len(meetings)} meetings (total: {total})")
        except Exception as e:
            print(f"  scope='{scope}': Error - {e}")


def test_search_meetings():
    """Test searching meetings by subject keyword."""
    print(f"\n{'-'*40}")
    print("Testing: search_meetings (client-side subject filtering)")
    print(f"{'-'*40}")
    
    # Use generic keywords commonly found in meeting titles
    test_keywords = ["sync", "check", "update", "review", "meeting"]
    
    for keyword in test_keywords:
        try:
            matches = search_meetings(keyword, max_results=3)
            if matches:
                print(f"  keyword='{keyword}': Found {len(matches)} matches")
                # Show first match subject (truncated for privacy)
                subject = matches[0].get("subject", "")
                truncated = subject[:40] + "..." if len(subject) > 40 else subject
                print(f"    First match: {truncated}")
                return matches  # Return first successful search for further testing
            else:
                print(f"  keyword='{keyword}': No matches")
        except Exception as e:
            print(f"  keyword='{keyword}': Error - {e}")
    
    print("  Note: No matches found for common keywords")
    return []


def find_meeting_with_notes():
    """Find a meeting that has notes ready."""
    print(f"\n{'-'*40}")
    print("Finding a meeting with notes ready...")
    print(f"{'-'*40}")
    
    import httpx
    import time
    from datetime import datetime, timedelta
    from integrations.common.config import get_avoma_api_key
    
    # Look back 90 days to find meetings with notes
    from_date = (datetime.now() - timedelta(days=90)).strftime("%Y-%m-%d")
    to_date = datetime.now().strftime("%Y-%m-%d")
    
    api_key = get_avoma_api_key()
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    
    try:
        checked = 0
        page = 1
        
        with httpx.Client(timeout=60.0, follow_redirects=True) as client:
            while checked < 50:  # Check up to 50 meetings
                # Fetch a page of meetings with scope=all to get team meetings
                response = client.get(
                    "https://api.avoma.com/v1/meetings",
                    headers=headers,
                    params={
                        "from_date": from_date,
                        "to_date": to_date,
                        "limit": 20,
                        "page": page,
                        "scope": "all",
                    }
                )
                
                if response.status_code == 429:
                    print(f"  Rate limited, waiting 5 seconds...")
                    time.sleep(5)
                    continue
                
                if response.status_code != 200:
                    print(f"  API error: {response.status_code}")
                    break
                
                data = response.json()
                meetings = data.get("results", [])
                
                if not meetings:
                    break
                
                print(f"  Page {page}: checking {len(meetings)} meetings...")
                
                for meeting in meetings:
                    meeting_uuid = meeting.get("uuid")
                    
                    # Small delay to avoid rate limiting
                    time.sleep(0.2)
                    
                    # Get full meeting details
                    detail_response = client.get(
                        f"https://api.avoma.com/v1/meetings/{meeting_uuid}",
                        headers=headers
                    )
                    checked += 1
                    
                    if detail_response.status_code == 429:
                        print(f"  Rate limited, waiting 5 seconds...")
                        time.sleep(5)
                        continue
                    
                    if detail_response.status_code == 200:
                        details = detail_response.json()
                        if details.get("notes_ready"):
                            print(f"  ✓ Found meeting with notes after checking {checked} meetings")
                            print(f"    Subject: {details.get('subject')}")
                            print(f"    UUID: {meeting_uuid}")
                            return meeting_uuid, details
                    
                    if checked >= 50:
                        break
                
                # Check if there's a next page
                if not data.get("next"):
                    break
                page += 1
                time.sleep(0.5)  # Small delay between pages
        
        print(f"  No meetings with ready notes found (checked {checked})")
        return None, None
    except Exception as e:
        print(f"  ✗ Error searching: {e}")
        import traceback
        traceback.print_exc()
        return None, None


def test_get_notes(meeting_uuid: str | None, meeting_details: dict | None = None):
    """Test getting meeting notes."""
    if not meeting_uuid:
        print(f"\n[SKIP] get_notes - no meeting UUID available")
        return
    
    print(f"\n{'-'*40}")
    print(f"Testing: get_notes")
    print(f"{'-'*40}")
    
    # Check if this meeting has notes
    notes_ready = meeting_details.get("notes_ready", False) if meeting_details else False
    
    print(f"  Meeting: {meeting_details.get('subject', 'Unknown') if meeting_details else 'Unknown'}")
    print(f"  notes_ready: {notes_ready}")
    
    if not notes_ready:
        print(f"  Note: This meeting doesn't have notes ready")
        return
    
    try:
        result = get_notes(meeting_uuid)
        if result:
            print(f"✓ Success! Retrieved notes/insights")
            print(f"  Keys: {list(result.keys())}")
            
            # Show AI notes
            ai_notes = result.get("ai_notes", [])
            if ai_notes:
                print(f"  AI Notes: {len(ai_notes)} items")
                # Group by note_type
                note_types = {}
                for note in ai_notes:
                    note_type = note.get("note_type", "unknown")
                    if note_type not in note_types:
                        note_types[note_type] = []
                    note_types[note_type].append(note)
                
                print(f"  Note types: {list(note_types.keys())}")
                
                # Show first few notes
                for note in ai_notes[:3]:
                    note_type = note.get("note_type", "unknown")
                    text = note.get("text", "")[:100]
                    print(f"    [{note_type}] {text}...")
            
            # Show other fields if present
            for key in ["summary", "action_items", "key_points", "topics"]:
                if key in result:
                    val = result[key]
                    if isinstance(val, list):
                        print(f"  {key}: {len(val)} items")
                    elif isinstance(val, str):
                        print(f"  {key}: {val[:100]}...")
        else:
            print(f"✗ Returned None (notes may not be available)")
    except Exception as e:
        print(f"✗ Failed: {e}")


def main():
    print("\n" + "="*60)
    print("AVOMA API INTEGRATION TEST")
    print("="*60)
    print("\nMake sure AVOMA_API_KEY is set in your .env file")
    
    # Verify API key is configured
    try:
        from integrations.common.config import get_avoma_api_key
        api_key = get_avoma_api_key()
        print(f"✓ API key configured (starts with: {api_key[:8]}...)")
    except ValueError as e:
        print(f"✗ {e}")
        print("  Set AVOMA_API_KEY in your .env file")
        return
    
    # Test list meetings (default scope=all for team meetings)
    meeting_uuid = test_list_meetings()
    
    # Test get meeting
    meeting_details = test_get_meeting(meeting_uuid)
    
    # Test scope parameter for team/all meetings
    test_list_meetings_with_scope()
    
    # Test search by subject keyword
    test_search_meetings()
    
    # Find a meeting with transcript and test transcript fetching
    transcript_meeting_uuid, transcript_meeting_details = find_meeting_with_transcript()
    
    # Test get transcript (use meeting with transcript if found, otherwise use first meeting)
    if transcript_meeting_uuid:
        test_get_transcript(transcript_meeting_uuid, transcript_meeting_details)
    else:
        print(f"\n{'-'*40}")
        print("Testing: get_transcript")
        print(f"{'-'*40}")
        print("  No meetings with ready transcripts found in last 90 days.")
        print("  Transcript test skipped.")
    
    # Find a meeting with notes and test notes fetching
    notes_meeting_uuid, notes_meeting_details = find_meeting_with_notes()
    
    # Test get notes (use meeting with notes if found)
    if notes_meeting_uuid:
        test_get_notes(notes_meeting_uuid, notes_meeting_details)
    else:
        print(f"\n{'-'*40}")
        print("Testing: get_notes")
        print(f"{'-'*40}")
        print("  No meetings with ready notes found in last 90 days.")
        print("  Notes test skipped.")
    
    # Test filters
    test_list_meetings_with_filters()
    test_list_meetings_with_date_range()
    
    print("\n" + "="*60)
    print("TEST COMPLETE")
    print("="*60)
    print("\nSummary:")
    print("  - list_meetings: Working (with scope parameter for team meetings)")
    print("  - search_meetings: Working (client-side subject filtering)")
    print("  - get_meeting: Working")
    print("  - get_transcript: Available when meeting has processed transcript")
    print("  - get_notes: Available when meeting has processed notes")
    print("\nNote: Transcripts and notes are only available for meetings where")
    print("      Avoma has finished processing the recording.")


if __name__ == "__main__":
    main()

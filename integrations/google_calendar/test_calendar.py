#!/usr/bin/env python3
"""Test script to verify Google Calendar API integration is working.

Run from project root:
  uv run python integrations/google_calendar/test_calendar.py
"""

import sys
from pathlib import Path
from datetime import datetime, timedelta, timezone

# Add project root to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from integrations.google_calendar import list_calendars, get_calendar, list_events, get_event


def test_list_calendars():
    """Test listing all accessible calendars."""
    print("\n1. Testing list_calendars()...")
    try:
        result = list_calendars(max_results=10)
        calendars = result.get("items", [])
        print(f"   ✓ Success! Found {len(calendars)} calendar(s)")
        
        for cal in calendars[:5]:
            name = cal.get("summary", "Unnamed")
            primary = " (primary)" if cal.get("primary") else ""
            print(f"      - {name}{primary}")
        
        return result
    except Exception as e:
        print(f"   ✗ Failed: {e}")
        return None


def test_get_primary_calendar():
    """Test getting the primary calendar."""
    print("\n2. Testing get_calendar('primary')...")
    try:
        calendar = get_calendar("primary")
        
        if calendar:
            print(f"   ✓ Success!")
            print(f"      Name: {calendar.get('summary', 'Unnamed')}")
            print(f"      Timezone: {calendar.get('timeZone', 'N/A')}")
        else:
            print("   ✗ Could not retrieve primary calendar")
        
        return calendar
    except Exception as e:
        print(f"   ✗ Failed: {e}")
        return None


def test_list_events():
    """Test listing upcoming events."""
    print("\n3. Testing list_events()...")
    try:
        # Get events for the next 7 days
        now = datetime.now(timezone.utc)
        time_max = now + timedelta(days=7)
        
        result = list_events(
            calendar_id="primary",
            time_min=now,
            time_max=time_max,
            max_results=10,
        )
        
        events = result.get("items", [])
        print(f"   ✓ Success! Found {len(events)} event(s) in the next 7 days")
        
        for event in events[:5]:
            start = event.get("start", {})
            start_time = start.get("dateTime", start.get("date", "N/A"))
            summary = event.get("summary", "Untitled")
            attendees = len(event.get("attendees", []))
            attendee_info = f" ({attendees} attendees)" if attendees else ""
            print(f"      - {summary}{attendee_info}")
            print(f"        Start: {start_time}")
        
        return result
    except Exception as e:
        print(f"   ✗ Failed: {e}")
        return None


def test_get_event():
    """Test getting a specific event."""
    print("\n4. Testing get_event()...")
    try:
        # First, get an event ID from the list
        result = list_events(calendar_id="primary", max_results=1)
        events = result.get("items", [])
        
        if not events:
            print("   ○ Skipped - no events found to test get_event()")
            return None
        
        event_id = events[0].get("id")
        event = get_event("primary", event_id)
        
        if event:
            print(f"   ✓ Success!")
            print(f"      Event: {event.get('summary', 'Untitled')}")
            print(f"      Status: {event.get('status', 'N/A')}")
            print(f"      Organizer: {event.get('organizer', {}).get('email', 'N/A')}")
        else:
            print("   ✗ Could not retrieve event")
        
        return event
    except Exception as e:
        print(f"   ✗ Failed: {e}")
        return None


def main():
    """Run all tests."""
    print("=" * 60)
    print("Google Calendar Integration Test Suite")
    print("=" * 60)
    
    results = {}
    
    # Test 1: List calendars
    results["list_calendars"] = test_list_calendars() is not None
    
    # Test 2: Get primary calendar
    results["get_calendar"] = test_get_primary_calendar() is not None
    
    # Test 3: List events
    results["list_events"] = test_list_events() is not None
    
    # Test 4: Get specific event
    results["get_event"] = test_get_event() is not None
    
    # Summary
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    
    passed = sum(1 for v in results.values() if v is True)
    failed = sum(1 for v in results.values() if v is False)
    
    for test_name, result in results.items():
        status = "✓ PASSED" if result else "✗ FAILED"
        print(f"   {test_name}: {status}")
    
    print(f"\nTotal: {passed} passed, {failed} failed")
    print("=" * 60)
    
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

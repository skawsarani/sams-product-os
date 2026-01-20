#!/usr/bin/env python3
"""Test script to verify all Slack integration functions work.

Run from project root:
  uv run python integrations/slack/test_slack.py
"""

import sys
from pathlib import Path

# Add project root to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from integrations.slack import (
    list_channels,
    get_channel_info,
    list_messages,
    search_messages,
    search_files,
)
from integrations.slack.client import get_client


def test_auth():
    """Test authentication and show current scopes."""
    print("\n0. Testing authentication (auth.test)...")
    try:
        client = get_client()
        result = client.get("auth.test")
        user = result.get("user", "unknown")
        team = result.get("team", "unknown")
        print(f"   ✓ Authenticated as: {user} @ {team}")
        print(f"   User ID: {result.get('user_id')}")
        print(f"   Team ID: {result.get('team_id')}")
        return True
    except Exception as e:
        print(f"   ✗ Failed: {e}")
        return False


def test_list_channels():
    """Test listing channels."""
    print("\n1. Testing list_channels()...")
    print("   Required scopes: channels:read, groups:read")
    try:
        result = list_channels(limit=5)
        channels = result.get("channels", [])
        print(f"   ✓ Success! Found {len(channels)} channels")
        if channels:
            for ch in channels[:3]:
                print(f"      - #{ch.get('name')} (id: {ch.get('id')})")
        return channels[0]["id"] if channels else None
    except Exception as e:
        print(f"   ✗ Failed: {e}")
        return None


def test_get_channel_info(channel_id: str):
    """Test getting channel info."""
    print(f"\n2. Testing get_channel_info(channel={channel_id})...")
    print("   Required scopes: channels:read, groups:read")
    try:
        result = get_channel_info(channel_id, include_num_members=True)
        name = result.get("name", "unknown")
        purpose = result.get("purpose", {}).get("value", "No purpose set")
        num_members = result.get("num_members", "N/A")
        print(f"   ✓ Success! Channel: #{name}")
        print(f"      Purpose: {purpose[:60]}..." if len(purpose) > 60 else f"      Purpose: {purpose}")
        print(f"      Members: {num_members}")
        return True
    except Exception as e:
        print(f"   ✗ Failed: {e}")
        return False


def test_list_messages(channel_id: str):
    """Test listing messages in a channel."""
    print(f"\n3. Testing list_messages(channel={channel_id})...")
    print("   Required scopes: channels:history, groups:history")
    try:
        result = list_messages(channel_id, limit=5)
        messages = result.get("messages", [])
        has_more = result.get("has_more", False)
        print(f"   ✓ Success! Found {len(messages)} messages (has_more: {has_more})")
        if messages:
            for msg in messages[:2]:
                text = msg.get("text", "")[:50]
                user = msg.get("user", "unknown")
                print(f"      - [{user}]: {text}...")
        return True
    except Exception as e:
        print(f"   ✗ Failed: {e}")
        return False


def test_search_messages():
    """Test searching messages."""
    print("\n4. Testing search_messages(query='*')...")
    print("   Required scopes: search:read")
    try:
        result = search_messages(query="*", count=3)
        matches = result.get("matches", [])
        total = result.get("total", 0)
        print(f"   ✓ Success! Found {total} total matches, returned {len(matches)}")
        if matches:
            for match in matches[:2]:
                text = match.get("text", "")[:50]
                channel = match.get("channel", {}).get("name", "unknown")
                print(f"      - [#{channel}]: {text}...")
        return True
    except Exception as e:
        print(f"   ✗ Failed: {e}")
        return False


def test_search_files():
    """Test searching files."""
    print("\n5. Testing search_files(query='*')...")
    print("   Required scopes: search:read")
    try:
        result = search_files(query="*", count=3)
        matches = result.get("matches", [])
        total = result.get("total", 0)
        print(f"   ✓ Success! Found {total} total files, returned {len(matches)}")
        if matches:
            for match in matches[:2]:
                name = match.get("name", "unknown")
                filetype = match.get("filetype", "unknown")
                print(f"      - {name} ({filetype})")
        return True
    except Exception as e:
        print(f"   ✗ Failed: {e}")
        return False


def main():
    """Run all tests."""
    print("=" * 60)
    print("Slack Integration Test Suite")
    print("=" * 60)
    
    results = {}
    
    # Test 0: Auth test
    results["auth"] = test_auth()
    
    if not results["auth"]:
        print("\n   ✗ Authentication failed. Check your SLACK_USER_TOKEN.")
        print("\n" + "=" * 60)
        return 1
    
    # Test 1: List channels (and get a channel ID for subsequent tests)
    channel_id = test_list_channels()
    results["list_channels"] = channel_id is not None
    
    if channel_id:
        # Test 2: Get channel info
        results["get_channel_info"] = test_get_channel_info(channel_id)
        
        # Test 3: List messages
        results["list_messages"] = test_list_messages(channel_id)
    else:
        print("\n   Skipping channel-specific tests (no channels found or missing scope)")
        results["get_channel_info"] = None
        results["list_messages"] = None
    
    # Test 4: Search messages
    results["search_messages"] = test_search_messages()
    
    # Test 5: Search files
    results["search_files"] = test_search_files()
    
    # Summary
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    
    passed = 0
    failed = 0
    skipped = 0
    
    for test_name, result in results.items():
        if result is True:
            status = "✓ PASSED"
            passed += 1
        elif result is False:
            status = "✗ FAILED"
            failed += 1
        else:
            status = "○ SKIPPED"
            skipped += 1
        print(f"   {test_name}: {status}")
    
    print(f"\nTotal: {passed} passed, {failed} failed, {skipped} skipped")
    
    if failed > 0:
        print("\n" + "-" * 60)
        print("Required Scopes Summary:")
        print("-" * 60)
        print("Your Slack User Token needs these OAuth scopes:")
        print("  - channels:read     (list public channels)")
        print("  - groups:read       (list private channels)")
        print("  - channels:history  (read messages in public channels)")
        print("  - groups:history    (read messages in private channels)")
        print("  - search:read       (search messages and files)")
        print("\nTo add scopes, go to api.slack.com/apps > Your App > OAuth & Permissions")
    
    print("=" * 60)
    
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

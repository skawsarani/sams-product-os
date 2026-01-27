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
    get_thread_replies,
    get_channel_day_summary,
    get_user,
    list_users,
    find_user_by_handle,
    get_user_display_name,
    parse_slack_message_link,
    build_slack_message_url,
    is_slack_url,
    # Mapping/caching functions
    get_user_id,
    set_user_mapping,
    get_cached_user_display_name,
    set_user_display_name,
    upsert_user_cache,
    clear_mappings,
    is_caching_enabled,
)
from integrations.slack.messages import find_unanswered_messages
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


def test_find_unanswered_messages(channel_id: str):
    """Test finding unanswered messages (no replies, no reactions)."""
    print(f"\n6. Testing find_unanswered_messages(channel={channel_id})...")
    print("   Required scopes: channels:history, groups:history")
    print("   Criteria: No thread replies AND no emoji reactions")
    try:
        result = find_unanswered_messages(
            channel=channel_id,
            hours_old=168,  # Look back 7 days
            max_results=10,
            resolve_users=True,
        )
        messages = result.get("messages", [])
        total_checked = result.get("total_checked", 0)
        user_names = result.get("user_names", {})

        print(f"   ✓ Success! Found {len(messages)} unanswered messages (checked {total_checked})")

        if messages:
            for msg in messages[:3]:
                text = msg.get("text", "")[:50]
                user_id = msg.get("user", "unknown")
                user_name = user_names.get(user_id, user_id)
                ts = msg.get("ts", "")
                print(f"      - [{user_name}] ({ts}): {text}...")

        return True
    except Exception as e:
        print(f"   ✗ Failed: {e}")
        return False


def test_get_thread_replies(channel_id: str, thread_ts: str | None):
    """Test getting thread replies."""
    print(f"\n7. Testing get_thread_replies(channel={channel_id})...")
    print("   Required scopes: channels:history, groups:history")

    if not thread_ts:
        print("   ○ Skipped - no thread found to test")
        return None

    try:
        result = get_thread_replies(
            channel=channel_id,
            thread_ts=thread_ts,
            limit=10,
        )
        messages = result.get("messages", [])
        has_more = result.get("has_more", False)

        print(f"   ✓ Success! Found {len(messages)} messages in thread (has_more: {has_more})")

        if messages:
            for msg in messages[:2]:
                text = msg.get("text", "")[:50]
                user = msg.get("user", "unknown")
                print(f"      - [{user}]: {text}...")

        return True
    except Exception as e:
        print(f"   ✗ Failed: {e}")
        return False


def test_get_channel_day_summary(channel_id: str):
    """Test getting channel day summary."""
    print(f"\n8. Testing get_channel_day_summary(channel={channel_id})...")
    print("   Required scopes: channels:history, groups:history, users:read")
    try:
        summary = get_channel_day_summary(
            channel=channel_id,
            # target_date defaults to today if not provided
        )

        print(f"   ✓ Success!")
        print(f"      Channel: #{summary.channel_name}")
        print(f"      Date: {summary.date}")
        print(f"      Total messages: {summary.message_count}")
        print(f"      Active users: {summary.participant_count}")
        print(f"      Thread count: {summary.thread_count}")

        if summary.top_participants:
            top_names = [p["who"] for p in summary.top_participants[:3]]
            print(f"      Top participants: {', '.join(top_names)}")

        return True
    except Exception as e:
        print(f"   ✗ Failed: {e}")
        return False


def test_list_users():
    """Test listing users in the workspace."""
    print("\n9. Testing list_users()...")
    print("   Required scopes: users:read")
    try:
        result = list_users(limit=10, include_bots=False)
        members = result.get("members", [])
        print(f"   ✓ Success! Found {len(members)} users (excluding bots)")

        if members:
            for member in members[:3]:
                name = get_user_display_name(member)
                user_id = member.get("id", "unknown")
                print(f"      - {name} ({user_id})")

        return members[0].get("id") if members else None
    except Exception as e:
        print(f"   ✗ Failed: {e}")
        return None


def test_get_user(user_id: str | None):
    """Test getting a specific user."""
    print(f"\n10. Testing get_user(user_id={user_id})...")
    print("    Required scopes: users:read")

    if not user_id:
        print("    ○ Skipped - no user ID available")
        return None

    try:
        user = get_user(user_id)
        display_name = get_user_display_name(user)
        email = user.get("profile", {}).get("email", "N/A")
        is_admin = user.get("is_admin", False)

        print(f"    ✓ Success!")
        print(f"       Display name: {display_name}")
        print(f"       Email: {email}")
        print(f"       Is admin: {is_admin}")

        return user
    except Exception as e:
        print(f"    ✗ Failed: {e}")
        return None


def test_find_user_by_handle(user: dict | None):
    """Test finding a user by handle."""
    print("\n11. Testing find_user_by_handle()...")
    print("    Required scopes: users:read")

    if not user:
        print("    ○ Skipped - no user available to search for")
        return None

    handle = user.get("name")
    if not handle:
        print("    ○ Skipped - user has no handle")
        return None

    try:
        found = find_user_by_handle(handle)
        if found and found.get("id") == user.get("id"):
            print(f"    ✓ Success! Found user @{handle}")
            return True
        else:
            print(f"    ✗ User not found or ID mismatch")
            return False
    except Exception as e:
        print(f"    ✗ Failed: {e}")
        return False


def test_slack_links_unit():
    """Unit tests for Slack URL parsing (no API required)."""
    print("\n12. Testing Slack link utilities (unit tests)...")

    passed = 0
    total = 0

    # Test parse_slack_message_link
    test_urls = [
        {
            "url": "https://myteam.slack.com/archives/C12345678/p1700000000000123",
            "expected_channel": "C12345678",
            "expected_ts": "1700000000.000123",
            "expected_thread": None,
        },
        {
            "url": "https://company.slack.com/archives/C98765432/p1705123456789012?thread_ts=1705000000.000001&cid=C98765432",
            "expected_channel": "C98765432",
            "expected_ts": "1705123456.789012",
            "expected_thread": "1705000000.000001",
        },
    ]

    for test in test_urls:
        total += 1
        result = parse_slack_message_link(test["url"])
        if result and result.channel_id == test["expected_channel"]:
            if result.message_ts == test["expected_ts"]:
                if result.thread_ts == test["expected_thread"]:
                    passed += 1
                else:
                    print(f"    ✗ thread_ts mismatch: {result.thread_ts} != {test['expected_thread']}")
            else:
                print(f"    ✗ message_ts mismatch: {result.message_ts} != {test['expected_ts']}")
        else:
            print(f"    ✗ Failed to parse: {test['url']}")

    # Test build_slack_message_url
    total += 1
    built_url = build_slack_message_url("myteam", "C12345678", "1700000000.000123")
    expected_url = "https://myteam.slack.com/archives/C12345678/p1700000000000123"
    if built_url == expected_url:
        passed += 1
    else:
        print(f"    ✗ build_url mismatch: {built_url}")

    # Test with thread_ts
    total += 1
    built_url = build_slack_message_url("myteam", "C12345678", "1700000000.000123", "1699999999.000001")
    if "thread_ts=1699999999.000001" in built_url:
        passed += 1
    else:
        print(f"    ✗ build_url with thread mismatch: {built_url}")

    # Test is_slack_url
    total += 1
    if is_slack_url("https://myteam.slack.com/archives/C123/p456"):
        passed += 1
    else:
        print("    ✗ is_slack_url failed for valid URL")

    total += 1
    if not is_slack_url("https://github.com/user/repo"):
        passed += 1
    else:
        print("    ✗ is_slack_url returned True for non-Slack URL")

    print(f"    ✓ Passed {passed}/{total} unit tests")
    return passed == total


def test_user_mapping_cache_basic():
    """Unit tests for user mapping cache read/write (no API required)."""
    print("\n13. Testing user mapping cache basic operations (unit tests)...")

    passed = 0
    total = 0

    # Clear cache before testing
    clear_mappings()

    # Test set_user_mapping / get_user_id
    total += 1
    set_user_mapping("jsmith", "U12345ABC")
    if get_user_id("jsmith") == "U12345ABC":
        passed += 1
    else:
        print("    ✗ set_user_mapping/get_user_id failed")

    # Test set_user_display_name / get_cached_user_display_name
    total += 1
    set_user_display_name("U12345ABC", "John Smith")
    if get_cached_user_display_name("U12345ABC") == "John Smith":
        passed += 1
    else:
        print("    ✗ set_user_display_name/get_cached_user_display_name failed")

    # Test upsert_user_cache batch updates
    total += 1
    upsert_user_cache([
        {"id": "U111", "handle": "alice", "display_name": "Alice Anderson"},
        {"id": "U222", "handle": "bob", "display_name": "Bob Builder"},
    ])
    if (
        get_user_id("alice") == "U111"
        and get_user_id("bob") == "U222"
        and get_cached_user_display_name("U111") == "Alice Anderson"
        and get_cached_user_display_name("U222") == "Bob Builder"
    ):
        passed += 1
    else:
        print("    ✗ upsert_user_cache batch failed")

    # Test clear_mappings
    total += 1
    clear_mappings()
    if get_user_id("jsmith") is None and get_cached_user_display_name("U12345ABC") is None:
        passed += 1
    else:
        print("    ✗ clear_mappings failed")

    print(f"    ✓ Passed {passed}/{total} unit tests")
    return passed == total


def test_user_cache_normalization():
    """Test handle normalization in cache (@ prefix, case insensitivity)."""
    print("\n14. Testing user cache handle normalization (unit tests)...")

    passed = 0
    total = 0

    clear_mappings()

    # Test @ prefix removal
    total += 1
    set_user_mapping("@testuser", "U99999")
    if get_user_id("testuser") == "U99999":
        passed += 1
    else:
        print("    ✗ @ prefix removal failed")

    # Test case insensitivity
    total += 1
    set_user_mapping("MixedCase", "U88888")
    if get_user_id("mixedcase") == "U88888" and get_user_id("MIXEDCASE") == "U88888":
        passed += 1
    else:
        print("    ✗ case insensitivity failed")

    # Test combined: @Prefix + Mixed Case
    total += 1
    if get_user_id("@TestUser") == "U99999":
        passed += 1
    else:
        print("    ✗ combined @prefix + case normalization failed")

    clear_mappings()

    print(f"    ✓ Passed {passed}/{total} unit tests")
    return passed == total


def test_user_cache_passthrough():
    """Test that user IDs pass through without cache lookup."""
    print("\n15. Testing user ID passthrough (unit tests)...")

    passed = 0
    total = 0

    clear_mappings()

    # User ID should pass through as-is
    total += 1
    if get_user_id("U12345ABC") == "U12345ABC":
        passed += 1
    else:
        print("    ✗ User ID passthrough failed")

    # Even with empty cache, ID returns itself
    total += 1
    if get_user_id("UABCDEFGH") == "UABCDEFGH":
        passed += 1
    else:
        print("    ✗ User ID passthrough (empty cache) failed")

    # Handle that's NOT in cache returns None
    total += 1
    if get_user_id("nonexistent") is None:
        passed += 1
    else:
        print("    ✗ Non-cached handle should return None")

    print(f"    ✓ Passed {passed}/{total} unit tests")
    return passed == total


def test_get_user_caches_result(user_id: str | None):
    """Integration test: verify get_user() caches the result."""
    print(f"\n16. Testing get_user() caching (user_id={user_id})...")
    print("    Required scopes: users:read")

    if not user_id:
        print("    ○ Skipped - no user ID available")
        return None

    if not is_caching_enabled():
        print("    ○ Skipped - caching is disabled in config")
        return None

    try:
        # Clear cache first
        clear_mappings()

        # Fetch user (should populate cache)
        user = get_user(user_id)
        handle = user.get("name")
        display_name = get_user_display_name(user)

        # Verify cache was populated
        cached_id = get_user_id(handle) if handle else None
        cached_name = get_cached_user_display_name(user_id)

        passed = 0
        total = 2

        if cached_id == user_id:
            passed += 1
            print(f"    ✓ Handle '{handle}' -> ID '{cached_id}' cached correctly")
        else:
            print(f"    ✗ Handle->ID cache mismatch: {cached_id} != {user_id}")

        if cached_name == display_name:
            passed += 1
            print(f"    ✓ ID '{user_id}' -> display_name '{cached_name}' cached correctly")
        else:
            print(f"    ✗ ID->display_name cache mismatch: {cached_name} != {display_name}")

        return passed == total

    except Exception as e:
        print(f"    ✗ Failed: {e}")
        return False


def test_find_user_by_handle_uses_cache(user: dict | None):
    """Integration test: verify find_user_by_handle() uses cache."""
    print("\n17. Testing find_user_by_handle() cache usage...")
    print("    Required scopes: users:read")

    if not user:
        print("    ○ Skipped - no user available")
        return None

    if not is_caching_enabled():
        print("    ○ Skipped - caching is disabled in config")
        return None

    handle = user.get("name")
    user_id = user.get("id")

    if not handle or not user_id:
        print("    ○ Skipped - user has no handle or ID")
        return None

    try:
        # Clear cache and pre-populate with known mapping
        clear_mappings()
        set_user_mapping(handle, user_id)

        # Now find_user_by_handle should use cached ID to fetch user
        # (instead of iterating through all users)
        found = find_user_by_handle(handle)

        if found and found.get("id") == user_id:
            print(f"    ✓ Found user @{handle} using cached mapping")
            return True
        else:
            print(f"    ✗ User not found or ID mismatch")
            return False

    except Exception as e:
        print(f"    ✗ Failed: {e}")
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

    # Test 6: Find unanswered messages
    if channel_id:
        results["find_unanswered_messages"] = test_find_unanswered_messages(channel_id)
    else:
        print("\n   Skipping find_unanswered_messages (no channel available)")
        results["find_unanswered_messages"] = None

    # Test 7: Get thread replies (find a thread first)
    thread_ts = None
    if channel_id:
        try:
            msg_result = list_messages(channel_id, limit=20)
            for msg in msg_result.get("messages", []):
                if msg.get("reply_count", 0) > 0:
                    thread_ts = msg.get("ts")
                    break
        except Exception:
            pass

    if channel_id:
        results["get_thread_replies"] = test_get_thread_replies(channel_id, thread_ts)
    else:
        print("\n   Skipping get_thread_replies (no channel available)")
        results["get_thread_replies"] = None

    # Test 8: Get channel day summary
    if channel_id:
        results["get_channel_day_summary"] = test_get_channel_day_summary(channel_id)
    else:
        print("\n   Skipping get_channel_day_summary (no channel available)")
        results["get_channel_day_summary"] = None

    # Test 9: List users
    user_id = test_list_users()
    results["list_users"] = user_id is not None

    # Test 10: Get user
    user = test_get_user(user_id)
    results["get_user"] = user is not None

    # Test 11: Find user by handle
    results["find_user_by_handle"] = test_find_user_by_handle(user)

    # Test 12: Slack links unit tests (no API required)
    results["slack_links_unit"] = test_slack_links_unit()

    # Test 13-15: User mapping cache unit tests (no API required)
    results["user_mapping_cache_basic"] = test_user_mapping_cache_basic()
    results["user_cache_normalization"] = test_user_cache_normalization()
    results["user_cache_passthrough"] = test_user_cache_passthrough()

    # Test 16-17: User caching integration tests
    results["get_user_caches_result"] = test_get_user_caches_result(user_id)
    results["find_user_by_handle_uses_cache"] = test_find_user_by_handle_uses_cache(user)

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
        print("  - users:read        (list and get user info)")
        print("\nTo add scopes, go to api.slack.com/apps > Your App > OAuth & Permissions")
    
    print("=" * 60)
    
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

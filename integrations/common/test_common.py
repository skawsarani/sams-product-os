#!/usr/bin/env python3
"""Test script for common utilities: URL parser.

Run from project root:
  uv run python integrations/common/test_common.py

These are unit tests that don't require API credentials.
"""

import sys
from pathlib import Path

# Add project root to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from integrations.common.url_parser import (
    parse_input,
    parse_slack_url,
    parse_notion_url,
    parse_linear_url,
    parse_avoma_url,
    parse_google_url,
    build_url,
    extract_keywords_from_text,
    is_url,
)


def test_slack_url_parsing():
    """Test Slack URL parsing."""
    print("\n1. Testing Slack URL parsing...")

    tests = [
        {
            "url": "https://myteam.slack.com/archives/C12345678/p1700000000000123",
            "expected_type": "slack-thread",
            "expected_channel": "C12345678",
            "expected_ts": "1700000000.000123",
        },
        {
            "url": "https://team.slack.com/archives/C98765432/p1705123456789012?thread_ts=1705000000.000001",
            "expected_type": "slack-thread",
            "expected_channel": "C98765432",
            "expected_thread_ts": "1705000000.000001",
        },
    ]

    passed = 0
    for test in tests:
        result = parse_input(test["url"])
        if result.type == test["expected_type"]:
            if result.channel_id == test["expected_channel"]:
                passed += 1
                print(f"   ✓ Parsed: {test['url'][:50]}...")
            else:
                print(f"   ✗ Channel mismatch: expected {test['expected_channel']}, got {result.channel_id}")
        else:
            print(f"   ✗ Type mismatch: expected {test['expected_type']}, got {result.type}")

    print(f"   Passed {passed}/{len(tests)} tests")
    return passed == len(tests)


def test_notion_url_parsing():
    """Test Notion URL parsing."""
    print("\n2. Testing Notion URL parsing...")

    tests = [
        {
            "url": "https://www.notion.so/workspace/Page-Title-abc123def456789012345678901234567",
            "expected_type": "notion-page",
            "expected_workspace": "workspace",
        },
        {
            "url": "https://notion.so/abc123def456789012345678901234567",
            "expected_type": "notion-page",
        },
    ]

    passed = 0
    for test in tests:
        result = parse_input(test["url"])
        if result.type == test["expected_type"]:
            if result.notion_page_id:
                passed += 1
                print(f"   ✓ Parsed: {test['url'][:50]}...")
            else:
                print(f"   ✗ Missing page_id")
        else:
            print(f"   ✗ Type mismatch: expected {test['expected_type']}, got {result.type}")

    print(f"   Passed {passed}/{len(tests)} tests")
    return passed == len(tests)


def test_linear_url_parsing():
    """Test Linear URL parsing."""
    print("\n3. Testing Linear URL parsing...")

    tests = [
        {
            "url": "https://linear.app/myworkspace/issue/ENG-123",
            "expected_type": "linear-issue",
            "expected_identifier": "ENG-123",
        },
        {
            "url": "https://linear.app/myworkspace/project/my-project-12345678-1234-1234-1234-123456789012",
            "expected_type": "linear-project",
        },
        {
            "url": "https://linear.app/myworkspace/initiative/my-initiative-12345678-1234-1234-1234-123456789012",
            "expected_type": "linear-initiative",
        },
    ]

    passed = 0
    for test in tests:
        result = parse_input(test["url"])
        if result.type == test["expected_type"]:
            passed += 1
            print(f"   ✓ Parsed: {test['url'][:50]}...")
        else:
            print(f"   ✗ Type mismatch: expected {test['expected_type']}, got {result.type}")

    print(f"   Passed {passed}/{len(tests)} tests")
    return passed == len(tests)


def test_avoma_url_parsing():
    """Test Avoma URL parsing."""
    print("\n4. Testing Avoma URL parsing...")

    tests = [
        {
            "url": "https://app.avoma.com/meeting/abc-123-def-456",
            "expected_type": "avoma-meeting",
            "expected_meeting_id": "abc-123-def-456",
        },
        {
            "url": "https://app.avoma.com/meeting/12345678-90ab-cdef-1234-567890abcdef",
            "expected_type": "avoma-meeting",
            "expected_meeting_id": "12345678-90ab-cdef-1234-567890abcdef",
        },
    ]

    passed = 0
    for test in tests:
        result = parse_input(test["url"])
        if result.type == test["expected_type"]:
            if result.avoma_meeting_id == test["expected_meeting_id"]:
                passed += 1
                print(f"   ✓ Parsed: {test['url']}")
            else:
                print(f"   ✗ Meeting ID mismatch: expected {test['expected_meeting_id']}, got {result.avoma_meeting_id}")
        else:
            print(f"   ✗ Type mismatch: expected {test['expected_type']}, got {result.type}")

    # Test rebuild URL
    result = parse_input("https://app.avoma.com/meeting/test-uuid-123")
    rebuilt = build_url(result)
    if rebuilt == "https://app.avoma.com/meeting/test-uuid-123":
        passed += 1
        print(f"   ✓ Rebuild URL works")
    else:
        print(f"   ✗ Rebuild URL failed: {rebuilt}")

    print(f"   Passed {passed}/{len(tests) + 1} tests")
    return passed == len(tests) + 1


def test_google_url_parsing():
    """Test Google Docs/Sheets/Slides URL parsing."""
    print("\n5. Testing Google URL parsing...")

    tests = [
        {
            "url": "https://docs.google.com/document/d/1abc123xyz/edit",
            "expected_type": "google-doc",
            "expected_file_id": "1abc123xyz",
            "expected_file_type": "document",
        },
        {
            "url": "https://docs.google.com/spreadsheets/d/sheet-file-id-123/edit#gid=0",
            "expected_type": "google-sheet",
            "expected_file_id": "sheet-file-id-123",
            "expected_file_type": "spreadsheet",
        },
        {
            "url": "https://docs.google.com/presentation/d/slide-file-456/edit",
            "expected_type": "google-slide",
            "expected_file_id": "slide-file-456",
            "expected_file_type": "presentation",
        },
    ]

    passed = 0
    for test in tests:
        result = parse_input(test["url"])
        if result.type == test["expected_type"]:
            if result.google_file_id == test["expected_file_id"]:
                if result.google_file_type == test["expected_file_type"]:
                    passed += 1
                    print(f"   ✓ Parsed: {test['url'][:50]}...")
                else:
                    print(f"   ✗ File type mismatch: expected {test['expected_file_type']}, got {result.google_file_type}")
            else:
                print(f"   ✗ File ID mismatch: expected {test['expected_file_id']}, got {result.google_file_id}")
        else:
            print(f"   ✗ Type mismatch: expected {test['expected_type']}, got {result.type}")

    # Test rebuild URLs
    for url_type, test_url, expected_rebuilt in [
        ("doc", "https://docs.google.com/document/d/doc123/edit", "https://docs.google.com/document/d/doc123/edit"),
        ("sheet", "https://docs.google.com/spreadsheets/d/sheet123/edit", "https://docs.google.com/spreadsheets/d/sheet123/edit"),
        ("slide", "https://docs.google.com/presentation/d/slide123/edit", "https://docs.google.com/presentation/d/slide123/edit"),
    ]:
        result = parse_input(test_url)
        rebuilt = build_url(result)
        if rebuilt == expected_rebuilt:
            passed += 1
            print(f"   ✓ Rebuild {url_type} URL works")
        else:
            print(f"   ✗ Rebuild {url_type} URL failed: {rebuilt}")

    print(f"   Passed {passed}/{len(tests) + 3} tests")
    return passed == len(tests) + 3


def test_raw_text_fallback():
    """Test raw text fallback and keyword extraction."""
    print("\n6. Testing raw text fallback...")

    # Test raw text with keywords
    result = parse_input("Need to implement user authentication for the login page")
    if result.type == "raw-text":
        if "user" in result.keywords or "authentication" in result.keywords or "login" in result.keywords:
            print(f"   ✓ Raw text parsed with keywords: {result.keywords[:5]}...")
            return True
        else:
            print(f"   ✗ Keywords not extracted properly: {result.keywords}")
            return False
    else:
        print(f"   ✗ Expected raw-text, got {result.type}")
        return False


def test_is_url():
    """Test URL detection."""
    print("\n7. Testing is_url()...")

    tests = [
        ("https://example.com", True),
        ("http://test.com/path", True),
        ("not a url", False),
        ("ftp://files.com", False),  # Only http(s)
        ("  https://spaced.com  ", True),
    ]

    passed = 0
    for text, expected in tests:
        result = is_url(text)
        if result == expected:
            passed += 1
        else:
            print(f"   ✗ is_url('{text}'): expected {expected}, got {result}")

    print(f"   ✓ Passed {passed}/{len(tests)} tests")
    return passed == len(tests)


def test_invalid_urls():
    """Test that invalid URLs fall back to raw text."""
    print("\n8. Testing invalid URL handling...")

    invalid_urls = [
        "https://random-site.com/page",
        "https://github.com/user/repo",
        "https://app.avoma.com/",  # No meeting path
        "https://docs.google.com/forms/d/123/edit",  # Forms not supported
        "https://linear.app/workspace",  # No resource type
    ]

    passed = 0
    for url in invalid_urls:
        result = parse_input(url)
        if result.type == "raw-text":
            passed += 1
        else:
            print(f"   ✗ Expected raw-text for '{url}', got {result.type}")

    print(f"   ✓ Passed {passed}/{len(invalid_urls)} tests")
    return passed == len(invalid_urls)


def main():
    """Run all tests."""
    print("=" * 60)
    print("Common Utilities Test Suite")
    print("=" * 60)
    print("\nThese are unit tests that don't require API credentials.")

    results = {}

    # URL Parser tests
    print("\n" + "-" * 40)
    print("URL PARSER TESTS")
    print("-" * 40)

    results["slack_url"] = test_slack_url_parsing()
    results["notion_url"] = test_notion_url_parsing()
    results["linear_url"] = test_linear_url_parsing()
    results["avoma_url"] = test_avoma_url_parsing()
    results["google_url"] = test_google_url_parsing()
    results["raw_text"] = test_raw_text_fallback()
    results["is_url"] = test_is_url()
    results["invalid_urls"] = test_invalid_urls()

    # Summary
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)

    passed = 0
    failed = 0

    for test_name, result in results.items():
        if result:
            status = "✓ PASSED"
            passed += 1
        else:
            status = "✗ FAILED"
            failed += 1
        print(f"   {test_name}: {status}")

    print(f"\nTotal: {passed} passed, {failed} failed")
    print("=" * 60)

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

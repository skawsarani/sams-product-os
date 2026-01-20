#!/usr/bin/env python3
"""Test script to verify all Notion integration functions work.

Run from project root:
  uv run python integrations/notion/test_notion.py
"""

import sys
from pathlib import Path

# Add project root to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from integrations.notion import (
    search,
    get_page,
    get_database,
    query_database,
    get_block,
    get_block_children,
)
from integrations.notion.client import get_client


def test_client():
    """Test that the client initializes and can make requests."""
    print("\n0. Testing client initialization...")
    try:
        client = get_client()
        # Make a simple search to verify auth works
        result = client.post("/search", {"page_size": 1})
        print(f"   ✓ Client initialized successfully")
        print(f"   API returned {len(result.get('results', []))} result(s)")
        return True
    except Exception as e:
        print(f"   ✗ Failed: {e}")
        return False


def test_search():
    """Test searching across the workspace."""
    print("\n1. Testing search()...")
    try:
        result = search(page_size=5)
        results = result.get("results", [])
        has_more = result.get("has_more", False)
        print(f"   ✓ Success! Found {len(results)} items (has_more: {has_more})")
        
        pages = []
        databases = []
        
        for item in results:
            obj_type = item.get("object")
            item_id = item.get("id")
            
            # Extract title based on object type
            if obj_type == "page":
                title = _extract_page_title(item)
                pages.append({"id": item_id, "title": title})
                print(f"      - [Page] {title[:50]}...")
            elif obj_type == "database":
                title = _extract_database_title(item)
                databases.append({"id": item_id, "title": title})
                print(f"      - [Database] {title[:50]}...")
        
        return {"pages": pages, "databases": databases}
    except Exception as e:
        print(f"   ✗ Failed: {e}")
        return None


def test_search_pages():
    """Test searching for pages only."""
    print("\n2. Testing search(filter_type='page')...")
    try:
        result = search(filter_type="page", page_size=3)
        results = result.get("results", [])
        print(f"   ✓ Success! Found {len(results)} pages")
        for item in results[:3]:
            title = _extract_page_title(item)
            print(f"      - {title[:60]}...")
        return True
    except Exception as e:
        print(f"   ✗ Failed: {e}")
        return False


def test_search_databases():
    """Test searching for databases only."""
    print("\n3. Testing search(filter_type='database')...")
    try:
        result = search(filter_type="database", page_size=3)
        results = result.get("results", [])
        print(f"   ✓ Success! Found {len(results)} databases")
        for item in results[:3]:
            title = _extract_database_title(item)
            print(f"      - {title[:60]}...")
        return results
    except Exception as e:
        print(f"   ✗ Failed: {e}")
        return None


def test_search_with_query():
    """Test searching with a query string."""
    print("\n4. Testing search(query='test')...")
    try:
        result = search(query="test", page_size=3)
        results = result.get("results", [])
        print(f"   ✓ Success! Found {len(results)} results matching 'test'")
        return True
    except Exception as e:
        print(f"   ✗ Failed: {e}")
        return False


def test_get_page(page_id: str):
    """Test getting a specific page."""
    print(f"\n5. Testing get_page(page_id='{page_id[:8]}...')...")
    try:
        result = get_page(page_id)
        title = _extract_page_title(result)
        created = result.get("created_time", "unknown")[:10]
        last_edited = result.get("last_edited_time", "unknown")[:10]
        print(f"   ✓ Success! Got page: {title[:50]}...")
        print(f"      Created: {created}, Last edited: {last_edited}")
        return True
    except Exception as e:
        print(f"   ✗ Failed: {e}")
        return False


def test_get_database(database_id: str):
    """Test getting a specific database."""
    print(f"\n6. Testing get_database(database_id='{database_id[:8]}...')...")
    try:
        result = get_database(database_id)
        title = _extract_database_title(result)
        properties = result.get("properties", {})
        print(f"   ✓ Success! Got database: {title[:50]}...")
        print(f"      Properties: {', '.join(list(properties.keys())[:5])}...")
        return True
    except Exception as e:
        print(f"   ✗ Failed: {e}")
        return False


def test_query_database(database_id: str):
    """Test querying a database."""
    print(f"\n7. Testing query_database(database_id='{database_id[:8]}...')...")
    try:
        result = query_database(database_id, page_size=5)
        results = result.get("results", [])
        has_more = result.get("has_more", False)
        print(f"   ✓ Success! Query returned {len(results)} rows (has_more: {has_more})")
        for item in results[:3]:
            title = _extract_page_title(item)
            print(f"      - {title[:60]}...")
        return True
    except Exception as e:
        print(f"   ✗ Failed: {e}")
        return False


def test_get_block_children(page_id: str):
    """Test getting block children of a page."""
    print(f"\n8. Testing get_block_children(block_id='{page_id[:8]}...')...")
    try:
        result = get_block_children(page_id, page_size=5)
        results = result.get("results", [])
        has_more = result.get("has_more", False)
        print(f"   ✓ Success! Found {len(results)} blocks (has_more: {has_more})")
        for block in results[:3]:
            block_type = block.get("type", "unknown")
            print(f"      - [{block_type}]")
        return True
    except Exception as e:
        print(f"   ✗ Failed: {e}")
        return False


def test_get_block(block_id: str):
    """Test getting a specific block."""
    print(f"\n9. Testing get_block(block_id='{block_id[:8]}...')...")
    try:
        result = get_block(block_id)
        block_type = result.get("type", "unknown")
        has_children = result.get("has_children", False)
        print(f"   ✓ Success! Got block of type: {block_type}")
        print(f"      Has children: {has_children}")
        return True
    except Exception as e:
        print(f"   ✗ Failed: {e}")
        return False


def _extract_page_title(page: dict) -> str:
    """Extract title from a page object."""
    properties = page.get("properties", {})
    
    # Try common title property names
    for prop_name in ["title", "Title", "Name", "name"]:
        if prop_name in properties:
            title_prop = properties[prop_name]
            if title_prop.get("type") == "title":
                title_array = title_prop.get("title", [])
                if title_array:
                    return "".join(t.get("plain_text", "") for t in title_array)
    
    # Fallback: look for any title type property
    for prop in properties.values():
        if prop.get("type") == "title":
            title_array = prop.get("title", [])
            if title_array:
                return "".join(t.get("plain_text", "") for t in title_array)
    
    return "(Untitled)"


def _extract_database_title(database: dict) -> str:
    """Extract title from a database object."""
    title_array = database.get("title", [])
    if title_array:
        return "".join(t.get("plain_text", "") for t in title_array)
    return "(Untitled Database)"


def main():
    """Run all tests."""
    print("=" * 60)
    print("Notion Integration Test Suite")
    print("=" * 60)
    
    results = {}
    
    # Test 0: Client initialization
    results["client"] = test_client()
    
    if not results["client"]:
        print("\n   ✗ Client initialization failed. Check your NOTION_TOKEN.")
        print("   Make sure the integration has access to your workspace.")
        print("\n" + "=" * 60)
        return 1
    
    # Test 1: General search
    search_results = test_search()
    results["search"] = search_results is not None
    
    # Test 2: Search pages only
    results["search_pages"] = test_search_pages()
    
    # Test 3: Search databases only
    databases = test_search_databases()
    results["search_databases"] = databases is not None
    
    # Test 4: Search with query
    results["search_query"] = test_search_with_query()
    
    # Get IDs for further tests
    page_id = None
    database_id = None
    
    if search_results:
        if search_results["pages"]:
            page_id = search_results["pages"][0]["id"]
        if search_results["databases"]:
            database_id = search_results["databases"][0]["id"]
    
    # If no database from general search, try from database-specific search
    if not database_id and databases:
        database_id = databases[0].get("id")
    
    # Test 5: Get page
    if page_id:
        results["get_page"] = test_get_page(page_id)
    else:
        print("\n5. Skipping get_page (no pages found)")
        results["get_page"] = None
    
    # Test 6: Get database
    if database_id:
        results["get_database"] = test_get_database(database_id)
    else:
        print("\n6. Skipping get_database (no databases found)")
        results["get_database"] = None
    
    # Test 7: Query database
    if database_id:
        results["query_database"] = test_query_database(database_id)
    else:
        print("\n7. Skipping query_database (no databases found)")
        results["query_database"] = None
    
    # Test 8: Get block children
    if page_id:
        results["get_block_children"] = test_get_block_children(page_id)
    else:
        print("\n8. Skipping get_block_children (no pages found)")
        results["get_block_children"] = None
    
    # Test 9: Get block (use page_id as block_id)
    if page_id:
        results["get_block"] = test_get_block(page_id)
    else:
        print("\n9. Skipping get_block (no pages found)")
        results["get_block"] = None
    
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
        print("Troubleshooting:")
        print("-" * 60)
        print("1. Verify NOTION_TOKEN is set correctly in .env")
        print("2. Ensure the integration is added to your workspace")
        print("3. Share pages/databases with the integration")
        print("\nTo set up a Notion integration:")
        print("  1. Go to notion.so/my-integrations")
        print("  2. Create a new integration")
        print("  3. Copy the 'Internal Integration Token'")
        print("  4. Add NOTION_TOKEN=<token> to your .env file")
        print("  5. In Notion, share pages with the integration")
    
    print("=" * 60)
    
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

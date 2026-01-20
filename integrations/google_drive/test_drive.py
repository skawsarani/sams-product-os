#!/usr/bin/env python3
"""Test script to verify Google Drive API integration is working.

Run from project root:
  uv run python integrations/google_drive/test_drive.py
"""

import sys
from pathlib import Path

# Add project root to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from integrations.google_drive import (
    list_files,
    get_file,
    list_folders,
    get_folder,
    search,
    list_permissions,
    download_file,
    export_file,
)


def test_list_files():
    """Test listing files."""
    print("\n1. Testing list_files()...")
    try:
        result = list_files(page_size=10)
        files = result.get("files", [])
        print(f"   ✓ Success! Found {len(files)} file(s)")
        
        for f in files[:5]:
            name = f.get("name", "Unnamed")
            mime = f.get("mimeType", "unknown")
            # Shorten mime type for display
            short_mime = mime.split(".")[-1] if "." in mime else mime.split("/")[-1]
            print(f"      - {name} ({short_mime})")
        
        return files[0] if files else None
    except Exception as e:
        print(f"   ✗ Failed: {e}")
        return None


def test_get_file(file_info: dict | None):
    """Test getting file metadata."""
    print("\n2. Testing get_file()...")
    
    if not file_info:
        print("   ○ Skipped - no file available from list_files()")
        return None
    
    try:
        file_id = file_info.get("id")
        file_name = file_info.get("name", "Unknown")
        print(f"   Fetching: {file_name}")
        
        result = get_file(file_id)
        
        if result:
            print(f"   ✓ Success!")
            print(f"      Name: {result.get('name')}")
            print(f"      Type: {result.get('mimeType')}")
            print(f"      Modified: {result.get('modifiedTime', 'N/A')}")
            if result.get("webViewLink"):
                print(f"      Link: {result.get('webViewLink')[:60]}...")
        else:
            print("   ✗ Could not retrieve file")
        
        return result
    except Exception as e:
        print(f"   ✗ Failed: {e}")
        return None


def test_list_folders():
    """Test listing folders."""
    print("\n3. Testing list_folders()...")
    try:
        result = list_folders(page_size=10)
        folders = result.get("folders", [])
        print(f"   ✓ Success! Found {len(folders)} folder(s)")
        
        for f in folders[:5]:
            name = f.get("name", "Unnamed")
            print(f"      - {name}/")
        
        return folders[0] if folders else None
    except Exception as e:
        print(f"   ✗ Failed: {e}")
        return None


def test_get_folder(folder_info: dict | None):
    """Test getting folder metadata."""
    print("\n4. Testing get_folder()...")
    
    if not folder_info:
        print("   ○ Skipped - no folder available from list_folders()")
        return None
    
    try:
        folder_id = folder_info.get("id")
        folder_name = folder_info.get("name", "Unknown")
        print(f"   Fetching: {folder_name}/")
        
        result = get_folder(folder_id)
        
        if result:
            print(f"   ✓ Success!")
            print(f"      Name: {result.get('name')}")
            print(f"      Created: {result.get('createdTime', 'N/A')}")
        else:
            print("   ✗ Could not retrieve folder")
        
        return result
    except Exception as e:
        print(f"   ✗ Failed: {e}")
        return None


def test_search():
    """Test searching for files."""
    print("\n5. Testing search()...")
    try:
        # Search for any file (broad search)
        result = search(query="name contains 'a' or name contains 'e'", page_size=5)
        files = result.get("files", [])
        print(f"   ✓ Success! Found {len(files)} file(s)")
        
        for f in files[:3]:
            name = f.get("name", "Unnamed")
            print(f"      - {name}")
        
        return result
    except Exception as e:
        print(f"   ✗ Failed: {e}")
        return None


def test_list_permissions(file_info: dict | None):
    """Test listing permissions on a file."""
    print("\n6. Testing list_permissions()...")
    
    if not file_info:
        print("   ○ Skipped - no file available")
        return None
    
    try:
        file_id = file_info.get("id")
        file_name = file_info.get("name", "Unknown")
        print(f"   Checking permissions on: {file_name}")
        
        result = list_permissions(file_id)
        permissions = result.get("permissions", [])
        print(f"   ✓ Success! Found {len(permissions)} permission(s)")
        
        for p in permissions[:5]:
            role = p.get("role", "unknown")
            ptype = p.get("type", "unknown")
            email = p.get("emailAddress", p.get("domain", "N/A"))
            print(f"      - {role} ({ptype}): {email}")
        
        return result
    except Exception as e:
        print(f"   ✗ Failed: {e}")
        return None


def test_download_file(file_info: dict | None):
    """Test downloading a file's content."""
    print("\n7. Testing download_file()...")
    
    if not file_info:
        print("   ○ Skipped - no file available")
        return None
    
    # Only works with non-Google files (e.g., .md, .pdf, .txt)
    mime_type = file_info.get("mimeType", "")
    if mime_type.startswith("application/vnd.google-apps"):
        print("   ○ Skipped - file is a Google format (use export_file instead)")
        return None
    
    try:
        file_id = file_info.get("id")
        file_name = file_info.get("name", "Unknown")
        print(f"   Downloading: {file_name}")
        
        content = download_file(file_id)
        
        print(f"   ✓ Success!")
        print(f"      Size: {len(content)} bytes")
        # Show preview for text files
        if mime_type.startswith("text/"):
            preview = content[:100].decode("utf-8", errors="replace")
            print(f"      Preview: {preview}...")
        
        return content
    except Exception as e:
        print(f"   ✗ Failed: {e}")
        return None


def test_export_file():
    """Test exporting a Google Doc as markdown."""
    print("\n8. Testing export_file()...")
    
    try:
        # Search for a Google Doc
        result = search(
            query="mimeType = 'application/vnd.google-apps.document'",
            page_size=1
        )
        docs = result.get("files", [])
        
        if not docs:
            print("   ○ Skipped - no Google Docs found")
            return None
        
        doc = docs[0]
        file_id = doc.get("id")
        file_name = doc.get("name", "Unknown")
        print(f"   Exporting: {file_name}")
        
        content = export_file(file_id, mime_type="text/markdown")
        
        print(f"   ✓ Success!")
        print(f"      Size: {len(content)} bytes")
        # Show preview
        preview = content[:150].decode("utf-8", errors="replace")
        print(f"      Preview: {preview}...")
        
        return content
    except Exception as e:
        print(f"   ✗ Failed: {e}")
        return None


def main():
    """Run all tests."""
    print("=" * 60)
    print("Google Drive Integration Test Suite")
    print("=" * 60)
    
    results = {}
    
    # Test 1: List files
    first_file = test_list_files()
    results["list_files"] = first_file is not None
    
    # Test 2: Get file
    results["get_file"] = test_get_file(first_file) is not None
    
    # Test 3: List folders
    first_folder = test_list_folders()
    results["list_folders"] = first_folder is not None
    
    # Test 4: Get folder
    if first_folder:
        results["get_folder"] = test_get_folder(first_folder) is not None
    else:
        print("\n4. Testing get_folder()...")
        print("   ○ Skipped - no folders found")
        results["get_folder"] = None
    
    # Test 5: Search
    results["search"] = test_search() is not None
    
    # Test 6: List permissions
    results["list_permissions"] = test_list_permissions(first_file) is not None
    
    # Test 7: Download file (need a non-Google file that's downloadable)
    # Find a downloadable file by searching for common file extensions
    downloadable_file = None
    try:
        # Search for markdown files specifically (most likely to exist and be downloadable)
        result = search(query="name contains '.md'", page_size=5)
        files = result.get("files", [])
        # Filter to only non-Google formats
        for f in files:
            if not f.get("mimeType", "").startswith("application/vnd.google-apps"):
                downloadable_file = f
                break
    except Exception:
        pass
    results["download_file"] = test_download_file(downloadable_file) is not None
    
    # Test 8: Export file (Google Doc to markdown)
    results["export_file"] = test_export_file() is not None
    
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
    print("=" * 60)
    
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

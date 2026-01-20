#!/usr/bin/env python3
"""Test script to verify Linear API integration is working.

Run from project root:
  uv run python integrations/linear/test_linear.py
"""

import sys
from pathlib import Path

# Add project root to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from integrations.linear.issues import list_issues, get_issue
from integrations.linear.projects import list_projects, get_project
from integrations.linear.initiatives import list_initiatives, get_initiative
from integrations.linear.labels import list_labels, get_label
from integrations.linear.cycles import list_cycles, get_cycle
from integrations.linear.comments import list_comments, get_comment


def test_list_operation(name: str, func, **kwargs):
    """Test a list operation and return first item ID if available."""
    print(f"\n{'='*60}")
    print(f"Testing: {name}")
    print(f"{'='*60}")
    try:
        results = func(**kwargs)
        print(f"✓ Success! Found {len(results)} items")
        if results:
            first = results[0]
            print(f"  First item: {first.get('name') or first.get('title') or first.get('identifier', 'N/A')}")
            return first.get("id")
        return None
    except Exception as e:
        print(f"✗ Failed: {e}")
        return None


def test_get_operation(name: str, func, item_id: str | None):
    """Test a get operation."""
    if not item_id:
        print(f"\n[SKIP] {name} - no ID available from list")
        return
    
    print(f"\n{'-'*40}")
    print(f"Testing: {name} (id: {item_id[:8]}...)")
    print(f"{'-'*40}")
    try:
        result = func(item_id)
        if result:
            print(f"✓ Success!")
            # Print some fields
            for key in ["name", "title", "identifier", "body", "state"]:
                if key in result:
                    val = result[key]
                    if isinstance(val, dict):
                        val = val.get("name", val)
                    print(f"  {key}: {val}")
        else:
            print(f"✗ Returned None (item might not exist)")
    except Exception as e:
        print(f"✗ Failed: {e}")


def main():
    print("\n" + "="*60)
    print("LINEAR API INTEGRATION TEST")
    print("="*60)
    
    # Test Issues
    issue_id = test_list_operation("list_issues", list_issues, first=5)
    test_get_operation("get_issue", get_issue, issue_id)
    
    # Test Projects
    project_id = test_list_operation("list_projects", list_projects, first=5)
    test_get_operation("get_project", get_project, project_id)
    
    # Test Initiatives
    initiative_id = test_list_operation("list_initiatives", list_initiatives, first=5)
    test_get_operation("get_initiative", get_initiative, initiative_id)
    
    # Test Labels
    label_id = test_list_operation("list_labels", list_labels, first=5)
    test_get_operation("get_label", get_label, label_id)
    
    # Test Cycles
    cycle_id = test_list_operation("list_cycles", list_cycles, first=5)
    test_get_operation("get_cycle", get_cycle, cycle_id)
    
    # Test Comments
    comment_id = test_list_operation("list_comments", list_comments, first=5)
    test_get_operation("get_comment", get_comment, comment_id)
    
    print("\n" + "="*60)
    print("TEST COMPLETE")
    print("="*60)
    print("\nIf you see ✓ marks above, the integration is working!")
    print("Some operations may return 0 items if your workspace is empty.")


if __name__ == "__main__":
    main()

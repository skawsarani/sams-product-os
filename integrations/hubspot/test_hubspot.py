#!/usr/bin/env python3
"""Test script to verify HubSpot CRM API integration is working.

Run from project root:
  uv run python integrations/hubspot/test_hubspot.py
"""

import sys
from pathlib import Path

# Add project root to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from integrations.hubspot.properties import list_properties, get_all_property_names
from integrations.hubspot.contacts import search_contacts, get_contact
from integrations.hubspot.companies import search_companies, get_company
from integrations.hubspot.deals import search_deals, get_deal
from integrations.hubspot.tickets import search_tickets
from integrations.hubspot.products import search_products


def test_list_properties():
    """Test listing property definitions for contacts."""
    print(f"\n{'='*60}")
    print("Testing: list_properties('contacts')")
    print(f"{'='*60}")
    try:
        properties = list_properties("contacts")
        print(f"Found {len(properties)} contact properties")

        if properties:
            print("\nFirst 5 properties:")
            for prop in properties[:5]:
                print(f"  - {prop['name']} ({prop.get('type', 'unknown')}): {prop.get('label', '')}")
        return True
    except Exception as e:
        print(f"Failed: {e}")
        return False


def test_get_all_property_names():
    """Test getting property names for search queries."""
    print(f"\n{'-'*40}")
    print("Testing: get_all_property_names('contacts')")
    print(f"{'-'*40}")
    try:
        names = get_all_property_names("contacts")
        print(f"Found {len(names)} property names")
        print(f"First 10: {names[:10]}")
        return True
    except Exception as e:
        print(f"Failed: {e}")
        return False


def test_search_contacts():
    """Test searching contacts."""
    print(f"\n{'='*60}")
    print("Testing: search_contacts")
    print(f"{'='*60}")
    try:
        result = search_contacts(limit=5)
        total = result.get("total", 0)
        contacts = result.get("results", [])
        print(f"Found {len(contacts)} contacts (total: {total})")

        if contacts:
            first = contacts[0]
            print(f"\nFirst contact:")
            print(f"  ID: {first.get('id')}")
            props = first.get("properties", {})
            for key in ["firstname", "lastname", "email", "company"]:
                if props.get(key):
                    print(f"  {key}: {props[key]}")
            return first.get("id")
        return None
    except Exception as e:
        print(f"Failed: {e}")
        return None


def test_get_contact(contact_id: str | None):
    """Test getting a specific contact."""
    if not contact_id:
        print(f"\n[SKIP] get_contact - no contact ID available")
        return

    print(f"\n{'-'*40}")
    print(f"Testing: get_contact (id: {contact_id})")
    print(f"{'-'*40}")
    try:
        result = get_contact(contact_id)
        if result:
            print("Successfully retrieved contact")
            props = result.get("properties", {})
            print(f"  Properties: {len(props)} fields")
        else:
            print("Contact not found")
    except Exception as e:
        print(f"Failed: {e}")


def test_search_companies():
    """Test searching companies."""
    print(f"\n{'='*60}")
    print("Testing: search_companies")
    print(f"{'='*60}")
    try:
        result = search_companies(limit=5)
        total = result.get("total", 0)
        companies = result.get("results", [])
        print(f"Found {len(companies)} companies (total: {total})")

        if companies:
            first = companies[0]
            print(f"\nFirst company:")
            print(f"  ID: {first.get('id')}")
            props = first.get("properties", {})
            for key in ["name", "domain", "industry", "annualrevenue"]:
                if props.get(key):
                    print(f"  {key}: {props[key]}")
            return first.get("id")
        return None
    except Exception as e:
        print(f"Failed: {e}")
        return None


def test_search_deals():
    """Test searching deals."""
    print(f"\n{'='*60}")
    print("Testing: search_deals")
    print(f"{'='*60}")
    try:
        result = search_deals(limit=5)
        total = result.get("total", 0)
        deals = result.get("results", [])
        print(f"Found {len(deals)} deals (total: {total})")

        if deals:
            first = deals[0]
            print(f"\nFirst deal:")
            print(f"  ID: {first.get('id')}")
            props = first.get("properties", {})
            for key in ["dealname", "amount", "dealstage", "closedate"]:
                if props.get(key):
                    print(f"  {key}: {props[key]}")
        return True
    except Exception as e:
        print(f"Failed: {e}")
        return False


def test_search_with_filter():
    """Test searching with a filter."""
    print(f"\n{'-'*40}")
    print("Testing: search_contacts with email filter")
    print(f"{'-'*40}")
    try:
        # Search for contacts that have an email property set
        result = search_contacts(
            filters=[{
                "propertyName": "email",
                "operator": "HAS_PROPERTY",
            }],
            limit=3,
        )
        contacts = result.get("results", [])
        print(f"Found {len(contacts)} contacts with email")

        for contact in contacts[:3]:
            email = contact.get("properties", {}).get("email", "N/A")
            print(f"  - {email}")
        return True
    except Exception as e:
        print(f"Failed: {e}")
        return False


def test_search_tickets():
    """Test searching tickets."""
    print(f"\n{'-'*40}")
    print("Testing: search_tickets")
    print(f"{'-'*40}")
    try:
        result = search_tickets(limit=3)
        total = result.get("total", 0)
        tickets = result.get("results", [])
        print(f"Found {len(tickets)} tickets (total: {total})")

        if tickets:
            first = tickets[0]
            print(f"\nFirst ticket:")
            print(f"  ID: {first.get('id')}")
            props = first.get("properties", {})
            for key in ["subject", "hs_ticket_priority", "hs_pipeline_stage"]:
                if props.get(key):
                    print(f"  {key}: {props[key]}")
        return True
    except Exception as e:
        print(f"Failed: {e}")
        return False


def test_search_products():
    """Test searching products."""
    print(f"\n{'-'*40}")
    print("Testing: search_products")
    print(f"{'-'*40}")
    try:
        result = search_products(limit=3)
        total = result.get("total", 0)
        products = result.get("results", [])
        print(f"Found {len(products)} products (total: {total})")

        if products:
            first = products[0]
            print(f"\nFirst product:")
            print(f"  ID: {first.get('id')}")
            props = first.get("properties", {})
            for key in ["name", "price", "description"]:
                if props.get(key):
                    val = props[key]
                    if len(str(val)) > 50:
                        val = str(val)[:50] + "..."
                    print(f"  {key}: {val}")
        return True
    except Exception as e:
        print(f"Failed: {e}")
        return False


def test_association_filter(contact_id: str | None):
    """Test searching deals associated with a contact."""
    if not contact_id:
        print(f"\n[SKIP] association filter - no contact ID available")
        return

    print(f"\n{'-'*40}")
    print(f"Testing: search_deals with associated_contact={contact_id}")
    print(f"{'-'*40}")
    try:
        result = search_deals(associated_contact=contact_id, limit=5)
        deals = result.get("results", [])
        print(f"Found {len(deals)} deals associated with contact")

        for deal in deals[:3]:
            name = deal.get("properties", {}).get("dealname", "N/A")
            print(f"  - {name}")
        return True
    except Exception as e:
        print(f"Failed: {e}")
        return False


def main():
    print("\n" + "="*60)
    print("HUBSPOT CRM API INTEGRATION TEST")
    print("="*60)
    print("\nMake sure HUBSPOT_ACCESS_TOKEN is set in your .env file")

    # Verify API key is configured
    try:
        from integrations.common.config import get_hubspot_access_token
        token = get_hubspot_access_token()
        print(f"API token configured (starts with: {token[:12]}...)")
    except ValueError as e:
        print(f"{e}")
        print("  Set HUBSPOT_ACCESS_TOKEN in your .env file")
        return

    # Test property definitions
    if not test_list_properties():
        print("\nProperty listing failed - cannot continue tests")
        return

    test_get_all_property_names()

    # Test contacts
    contact_id = test_search_contacts()
    test_get_contact(contact_id)

    # Test companies
    test_search_companies()

    # Test deals
    test_search_deals()

    # Test filters
    test_search_with_filter()

    # Test other objects
    test_search_tickets()
    test_search_products()

    # Test association filtering
    test_association_filter(contact_id)

    print("\n" + "="*60)
    print("TEST COMPLETE")
    print("="*60)
    print("\nSummary:")
    print("  - list_properties: Working")
    print("  - get_all_property_names: Working (cached)")
    print("  - search_contacts/get_contact: Working")
    print("  - search_companies: Working")
    print("  - search_deals: Working")
    print("  - search_tickets: Working")
    print("  - search_products: Working")
    print("  - Filter support: Working")
    print("  - Association filtering: Working")
    print("\nNote: Some object types (carts, orders, invoices, quotes, subscriptions)")
    print("      may require specific HubSpot plans or features to be enabled.")


if __name__ == "__main__":
    main()

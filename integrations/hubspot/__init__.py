"""HubSpot CRM API integration - read-only access to CRM objects via Search API."""

from .properties import (
    list_properties,
    get_all_property_names,
    clear_property_cache,
)
from .contacts import (
    search_contacts,
    get_contact,
)
from .companies import (
    search_companies,
    get_company,
)
from .deals import (
    search_deals,
    get_deal,
)
from .tickets import (
    search_tickets,
    get_ticket,
)
from .carts import (
    search_carts,
    get_cart,
)
from .products import (
    search_products,
    get_product,
)
from .orders import (
    search_orders,
    get_order,
)
from .line_items import (
    search_line_items,
    get_line_item,
)
from .invoices import (
    search_invoices,
    get_invoice,
)
from .quotes import (
    search_quotes,
    get_quote,
)
from .subscriptions import (
    search_subscriptions,
    get_subscription,
)

__all__ = [
    # Properties
    "list_properties",
    "get_all_property_names",
    "clear_property_cache",
    # Contacts
    "search_contacts",
    "get_contact",
    # Companies
    "search_companies",
    "get_company",
    # Deals
    "search_deals",
    "get_deal",
    # Tickets
    "search_tickets",
    "get_ticket",
    # Carts
    "search_carts",
    "get_cart",
    # Products
    "search_products",
    "get_product",
    # Orders
    "search_orders",
    "get_order",
    # Line Items
    "search_line_items",
    "get_line_item",
    # Invoices
    "search_invoices",
    "get_invoice",
    # Quotes
    "search_quotes",
    "get_quote",
    # Subscriptions
    "search_subscriptions",
    "get_subscription",
]

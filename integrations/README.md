# Integrations

Read-only API clients for external services used by PM Co-Pilot.

## Prerequisites

Install all integration dependencies:

```bash
uv sync --all-extras
```

## Available Integrations

### Avoma

Meeting intelligence platform.

| Module | Functions |
|--------|-----------|
| Meetings | `get_meeting`, `list_meetings`, `search_meetings` |
| Notes | `get_notes`, `get_meeting_insights` |
| Transcripts | `get_transcript`, `get_transcription` |

### Google Calendar

| Module | Functions |
|--------|-----------|
| Events | `get_event`, `list_events` |
| Calendars | `get_calendar`, `list_calendars` |

### Google Drive

| Module | Functions |
|--------|-----------|
| Files | `get_file`, `list_files`, `download_file`, `export_file` |
| Folders | `get_folder`, `list_folders` |
| Permissions | `list_permissions` |
| Search | `search` |

### Linear

GraphQL-based project management.

| Module | Functions |
|--------|-----------|
| Issues | `get_issue`, `list_issues` |
| Projects | `get_project`, `list_projects` |
| Initiatives | `get_initiative`, `list_initiatives` |
| Comments | `get_comment`, `list_comments` |
| Labels | `get_label`, `list_labels` |
| Cycles | `get_cycle`, `list_cycles` |
| Customers | `get_customer`, `list_customers`, `list_customer_needs` |

### Notion

| Module | Functions |
|--------|-----------|
| Pages | `get_page` |
| Databases | `get_database`, `query_database` |
| Blocks | `get_block`, `get_block_children` |
| Search | `search` |

### Slack

| Module | Functions |
|--------|-----------|
| Messages | `list_messages`, `find_unanswered_messages` |
| Channels | `list_channels`, `get_channel_info` |
| Search | `search_messages`, `search_files` |
| Users | `get_user`, `list_users`, `find_user_by_handle`, `get_user_display_name` |
| Threads | `get_thread_replies`, `get_all_thread_replies` |
| Links | `parse_slack_message_link`, `build_slack_message_url`, `is_slack_url` |
| Channel Summary | `get_channel_day_summary` |
| Mapping | Cache utilities for channel/user ID resolution |

### HubSpot

CRM search and read operations.

| Module | Functions |
|--------|-----------|
| Contacts | `search_contacts`, `get_contact` |
| Companies | `search_companies`, `get_company` |
| Deals | `search_deals`, `get_deal` |
| Tickets | `search_tickets`, `get_ticket` |
| Carts | `search_carts`, `get_cart` |
| Products | `search_products`, `get_product` |
| Orders | `search_orders`, `get_order` |
| Line Items | `search_line_items`, `get_line_item` |
| Invoices | `search_invoices`, `get_invoice` |
| Quotes | `search_quotes`, `get_quote` |
| Subscriptions | `search_subscriptions`, `get_subscription` |
| Properties | `list_properties`, `get_all_property_names`, `clear_property_cache` |

### Common Utilities

Shared helpers for all integrations.

| Module | Functions |
|--------|-----------|
| Config | `get_linear_api_key`, `get_slack_token`, `get_notion_token`, `get_avoma_api_key`, `get_hubspot_access_token` |
| Utils | `paginate`, `format_output`, `APIError` |
| Google Auth | `build_calendar_service`, `build_drive_service` |
| URL Parser | `parse_input`, `parse_slack_url`, `parse_notion_url`, `parse_linear_url`, `parse_avoma_url`, `parse_google_url`, `build_url`, `is_url` |

## Configuration

Each integration requires API credentials configured via environment variables (`.env`). See `.env.example` in the project root for required variables.

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
| Messages | `list_messages` |
| Channels | `list_channels`, `get_channel_info` |
| Search | `search_messages`, `search_files` |

## Configuration

Each integration requires API credentials configured via environment variables (`.env`). See `.env.example` in the project root for required variables.

# Tools Reference

MCP tools and CLI integrations available to Sams Product OS.

## MCP Tools

MCP (Model Context Protocol) provides direct tool access. Prefer MCP tools over file operations when available.

### PM Tasks (`mcp__pm-tasks__*`)

| Tool | Purpose |
|------|---------|
| `list_tasks` | List and filter tasks by priority, status, category, age |
| `get_task` | Get full details of a specific task |
| `create_task` | Create new task with auto-categorization |
| `update_task_status` | Update task status (n/s/b/d) |
| `update_task_priority` | Update task priority (P0-P3) |
| `get_task_summary` | Task statistics by priority, status, category |
| `find_stale_tasks` | Find started tasks not updated recently |
| `find_overdue_tasks` | Find tasks past due date |
| `prune_completed_tasks` | Delete old completed tasks |
| `check_duplicates` | Check for similar existing tasks before creating |
| `process_backlog` | Process BACKLOG.md with categorization and deduplication |
| `clear_backlog` | Archive and reset BACKLOG.md |

### Linear (`mcp__linear-server__*`)

| Tool | Purpose |
|------|---------|
| `list_issues` | List/search issues with `query` param for text search |
| `get_issue` | Get full issue details by identifier |
| `create_issue` | Create new issue |
| `update_issue` | Update issue fields |
| `list_projects` | List projects |
| `get_project` | Get project details |
| `list_comments` | List comments on an issue |
| `create_comment` | Add comment to an issue |

### Notion (`mcp__notion__*`)

| Tool | Purpose |
|------|---------|
| `notion-search` | Semantic/AI search across workspace and connected sources |
| `notion-fetch` | Get page or database content by URL/ID |
| `notion-create-pages` | Create new pages |
| `notion-update-page` | Update page properties |
| `notion-create-comment` | Add comment to a page |

## CLI Integrations

Python modules in `tools/integrations/` for external services. Run via `uv run -m tools.integrations.<name>`.

**Note:** For Linear and Notion, prefer MCP tools above. Use CLI only for features without MCP equivalent.

| Integration | CLI Used For |
|-------------|--------------|
| **Linear** | Customers, customer needs, initiatives (no MCP) |
| **Slack** | All operations (search, threads, channels, unanswered) |
| **Notion** | Fallback only - prefer MCP |
| **Google Calendar** | Events, calendars |
| **Google Drive** | Search, files, folders |
| **HubSpot** | Companies, deals, tickets, contacts |
| **Common** | URL parser (Slack, Linear, Google, Notion) |

### QMD Local Search (CLI)

On-device semantic search across all PM OS markdown content.

| Command | Purpose |
|---------|---------|
| `qmd search "query"` | Fast keyword search (BM25) |
| `qmd vsearch "query"` | Semantic similarity search |
| `qmd query "query"` | Hybrid search with re-ranking (best quality) |
| `qmd get <path>` | Retrieve full document by path or docid |
| `qmd embed` | Re-index after adding new content |

**Flags:** `-n 10` (result count), `-c knowledge` (filter collection), `--json` (structured output), `--md` (markdown)

Use `query` for open-ended questions. Use `search` for exact keyword lookups. Use `-c` to scope to a collection.

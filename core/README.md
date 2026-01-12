# PM Co-Pilot Core System

This folder contains core system components for PM Co-Pilot. These files provide the foundation for task management, evaluation testing, and configuration.

## What's in core/

- **config.yaml** - System configuration (customizable by users)
  - Priority caps (P0≤3, P1≤7, P2≤15)
  - Task categories and auto-categorization keywords
  - Deduplication settings
  - Task aging rules

- **evals/** - Automated evaluation suite
  - Validates backlog processing workflow
  - Tests categorization, priority caps, auto-categorization
  - Run with: `cd core/evals && ./run_evals.sh`

- **task-manager-mcp/** - Task management MCP server
  - `server.py` - MCP server with 12 tools for task operations
  - `requirements.txt` - Python dependencies
  - `README.md` - Detailed tool documentation and testing guide
  - Programmatic access to tasks via MCP protocol
  - Auto-categorization, priority enforcement, backlog processing

## Task Management MCP Server

The task management MCP server provides fast, programmatic access to your tasks through the Model Context Protocol.

### Features

- **CRUD Operations**: Create, read, update, delete tasks
- **Smart Deduplication**: Prevents duplicate tasks using similarity scoring
- **Priority Enforcement**: Enforces caps (P0≤3, P1≤7, P2≤15)
- **Auto-Categorization**: Uses keywords from config.yaml to assign categories
- **Backlog Processing**: Automated BACKLOG.md processing with ambiguity detection
- **Smart Templates**: Category-specific task templates (technical, outreach, research, writing, admin)
- **Task Health**: Find stale tasks, overdue tasks, prune completed ones
- **Statistics**: Get task counts by priority, status, category

### Setup

#### 1. Install Dependencies

```bash
cd core/task-manager-mcp
uv sync
```

#### 2. Configure MCP Client

Add to your MCP client configuration (e.g., Claude Code, Cursor):

**For Claude Code** (`.mcp.json` in project root):

```json
{
  "mcpServers": {
    "pm-tasks": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "./core/task-manager-mcp",
        "python",
        "server.py"
      ]
    }
  }
}
```

**For Cursor** (`.cursor/mcp.json` in project root):

```json
{
  "mcpServers": {
    "pm-tasks": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "./core/task-manager-mcp",
        "python",
        "server.py"
      ]
    }
  }
}
```

#### 3. Restart Your MCP Client

Restart Claude Code, Cursor, or your MCP client to load the server.

### Available Tools

The MCP server exposes 12 tools:

1. **list_tasks** - Filter tasks by priority, status, category, age
2. **get_task** - Read single task details with full metadata
3. **create_task** - Create new task with smart category templates
4. **update_task_status** - Change status (n/s/b/d)
5. **update_task_priority** - Change priority (P0-P3)
6. **get_task_summary** - Statistics (counts by priority, status, category)
7. **find_stale_tasks** - Tasks with status 's' but inactive 14+ days
8. **find_overdue_tasks** - Tasks past their due_date
9. **prune_completed_tasks** - Delete tasks with status 'd' older than 90 days
10. **check_duplicates** - Check for similar tasks with actionable suggestions
11. **process_backlog** - Automated BACKLOG.md processing with dedup and ambiguity detection
12. **clear_backlog** - Archive BACKLOG.md to knowledge/notes/ and reset

See `task-manager-mcp/README.md` for detailed documentation of each tool.

### Usage Examples

**List all P0 tasks:**
```
AI uses list_tasks tool with priority="P0"
```

**Create a new task:**
```
AI uses create_task tool with:
- title: "Fix authentication bug"
- priority: "P0"
- category: "technical"
- description: "Users cannot log in with email"
```

**Find stale tasks:**
```
AI uses find_stale_tasks tool
Returns tasks marked as started but not updated in 14+ days
```

**Check for duplicates before creating:**
```
AI uses check_duplicates tool with title and keywords
Returns similar existing tasks to prevent duplicates
```

## Customizing config.yaml

The config.yaml file in this folder is **user-customizable**. You can adjust:

### Priority Caps

```yaml
priority_caps:
  P0: 3   # Adjust max P0 tasks (default: 3)
  P1: 7   # Adjust max P1 tasks (default: 7)
  P2: 15  # Adjust max P2 tasks (default: 15)
  P3: 999 # Unlimited backlog
```

### Task Categories

Add or remove categories to match your workflow:

```yaml
task_categories:
  - technical    # Engineering work
  - outreach     # People/communication
  - research     # Discovery/analysis
  - writing      # Documentation
  - admin        # Ops/planning
  - your-custom-category  # Add your own
```

### Auto-Categorization Keywords

Teach the AI to auto-categorize tasks based on keywords:

```yaml
category_keywords:
  technical:
    - bug
    - fix
    - api
    - code
  outreach:
    - email
    - meeting
    - call
  your-custom-category:
    - keyword1
    - keyword2
```

### Task Aging

Control when tasks are flagged or pruned:

```yaml
task_aging:
  prune_completed_after: 90  # Days before deleting done tasks
  flag_stale_after: 14       # Days before flagging stale tasks
```

### Deduplication

Fine-tune duplicate detection:

```yaml
deduplication:
  similarity_threshold: 0.6  # 0-1 scale (higher = stricter)
  check_categories: true     # Consider category when matching
  check_keywords: true       # Use keyword overlap for matching
```

## Running Evals

Test that your system is working correctly:

```bash
cd core/evals
./run_evals.sh
```

This validates:
- Task categorization
- Auto-categorization based on keywords
- Priority caps enforcement
- File format and structure

See `core/evals/README.md` for details.

## System vs User Folders

**Core System Components** (this folder):
- Configuration (`config.yaml`)
- Evaluation suite (`evals/`)
- Task management MCP (`task-manager-mcp/`)

**User Workspace** (root level):
- `knowledge/` - Your knowledge base
- `tasks/` - Your task files
- `skills/` - Custom AI skills
- `templates/` - Document templates
- `workflows/` - Workflow definitions
- `mcp/` -  MCP servers

## Maintenance

### Update MCP Server

If you make changes to `task-manager-mcp/server.py`, restart your MCP client to reload.

### Update Config

Changes to `config.yaml` take effect on next backlog processing or MCP tool call.

### Run Evals After Changes

Run evals after modifying:
- `core/config.yaml`
- `AGENTS.md`
- `workflows/process-backlog.md`
- Task management logic

This ensures your changes don't break existing functionality.

## Troubleshooting

### MCP Server Not Loading

1. Check absolute paths in MCP client config
2. Verify Python dependencies: `pip list | grep mcp`
3. Check MCP client logs for errors

### Config Changes Not Working

1. Verify YAML syntax is valid
2. Restart MCP client if using MCP tools
3. Re-run `/backlog` to apply new settings

### Evals Failing

1. Check if you modified expected behavior (update expected outputs)
2. Review `core/evals/results/` for details
3. See `core/evals/README.md` troubleshooting section

---

**Note**: This folder contains system infrastructure but config.yaml remains fully customizable. Adjust settings to match your workflow.

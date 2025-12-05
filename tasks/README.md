# Tasks

This folder contains your actionable tasks. Tasks are created when processing your backlog or can be created directly.

## Task Structure

Each task file uses frontmatter with the following fields:

- **title**: Actionable task name
- **category**: One of the categories from `config.yaml` (technical, outreach, research, writing, admin, other)
- **priority**: P0 (Critical), P1 (High), P2 (Normal), P3 (Low)
- **status**: n (not_started), s (started), b (blocked), d (done)
- **created_date**: YYYY-MM-DD
- **due_date**: YYYY-MM-DD (optional)
- **resource_refs**: Links to related knowledge files

Each task also includes:
- **Context**: Tie to goals and reference material
- **Next Actions**: Checklist of steps to complete
- **Progress Log**: Notes, blockers, decisions over time

## Managing Tasks

### Update Task Status

Ask the AI:
- "Mark task [name] as complete"
- "Change task [name] status to [n/s/b/d]"
- "Change task [name] priority to [P0/P1/P2/P3]"
- "Change task [name] category to [category]"
- "Update task [name]" (for multiple field updates)

### Find Tasks

- "Find tasks older than [N] days"
- "Find stale tasks" (started but inactive)
- "Show task aging report"

### Prune Tasks

- "Prune completed tasks older than [N] days"

## Task Completion

Tasks are marked complete by updating `status: d` in the task file. No file movement is needed.

## Future Integration

MCP server integration for syncing with external todo apps (Todoist, Asana, etc.) is planned.


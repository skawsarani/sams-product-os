---
name: task-views
description: Displays task views. Invoked via /today (tasks due today or overdue), /upcoming (tasks due in next 7 days), /tasks (all tasks with optional filtering by priority, status, category). Also triggered by "what's due today", "show my tasks".
allowed-tools: find_overdue_tasks, list_tasks, get_task_summary, Glob, Read
argument-hint: [optional filters: priority, status, category, or number of days for upcoming]
---

## Context

Tasks are stored in markdown files in the `tasks/` directory with YAML frontmatter containing priority, status, due_date, category.
Today's date: $TODAY
Arguments: $ARGUMENTS

---

## /today — Due Today & Overdue

Show all tasks that are due today or overdue, prioritized by urgency.

**Steps:**

1. **Try MCP first**: Use `find_overdue_tasks` and `list_tasks` MCP tools

2. **Failover if needed**: If MCP tools fail or aren't available:
   - Use `Glob` to find all files in `tasks/*.md`
   - Use `Read` to parse each task file's frontmatter
   - Filter for tasks where `due_date` is today ($TODAY) or earlier
   - Note: "Using direct file reading (MCP unavailable)"

3. **Combine and prioritize**: Sort by:
   - Overdue tasks first (most overdue at top)
   - Today's tasks second
   - Within each group, sort by priority (P0 → P1 → P2 → P3)

4. **Format output**:
```
Due Today & Overdue Tasks

OVERDUE
  [s] Task name (P0, Category) - 3 days overdue
      tasks/filename.md

  [n] Task name (P1, Category) - 1 day overdue
      tasks/filename.md

DUE TODAY
  [s] Task name (P0, Category)
      tasks/filename.md

---
Total: X overdue, Y due today
```

- If no tasks are due/overdue, say so clearly and suggest reviewing P0/P1 tasks
- Recommend specific next actions based on what's found

---

## /upcoming — Due in Next 7 Days

Show all tasks due in the next 7 days (or custom timeframe if specified).

**Steps:**

1. **Determine timeframe**:
   - Default: next 7 days
   - If $ARGUMENTS contains a number, use that many days instead

2. **Try MCP first**: Use `list_tasks` MCP tool and filter by date range

3. **Failover if needed**: If MCP tools fail:
   - Use `Glob` to find all files in `tasks/*.md`
   - Use `Read` to parse each task file's frontmatter
   - Filter for tasks where `due_date` is between today and end of timeframe
   - Exclude overdue tasks (those are for /today)
   - Note: "Using direct file reading (MCP unavailable)"

4. **Group by date**: Organize tasks by their due date in chronological order

5. **Format output**:
```
Upcoming Tasks (Next 7 Days)

Tomorrow (YYYY-MM-DD)
  [n] Task name (P0, Category)
      tasks/filename.md

Wednesday (YYYY-MM-DD)
  [s] Task name (P1, Category)
      tasks/filename.md
  [n] Task name (P2, Category)
      tasks/filename.md

Friday (YYYY-MM-DD)
  [n] Task name (P1, Category)
      tasks/filename.md

---
Total: X tasks across Y days
```

- Use relative dates when helpful (Tomorrow, This Friday, etc.)
- Highlight P0/P1 tasks for visibility
- If no tasks in timeframe, suggest reviewing task priorities and deadlines

---

## /tasks — All Tasks

Display all tasks with their details in a clear, organized format.

**Steps:**

1. **Try MCP first**: Use `get_task_summary` and `list_tasks` MCP tools

2. **Failover if needed**: If MCP tools fail:
   - Use `Glob` to find all files in `tasks/*.md`
   - Use `Read` to parse each task file's frontmatter
   - Note: "Using direct file reading (MCP unavailable)"

3. **Apply filters**: If $ARGUMENTS provided, filter by:
   - Priority: P0, P1, P2, P3
   - Status: n (not started), s (started), b (blocked), d (done)
   - Category

4. **Format output**: Display tasks grouped by priority (P0 → P1 → P2 → P3):
```
Task Summary: X total tasks (P0: X/3, P1: X/7, P2: X/15, P3: X)

P0 (Critical) - Max 3
  [s] Task name (Category) - Due: YYYY-MM-DD
      tasks/filename.md

P1 (High) - Max 7
  [n] Task name (Category)
      tasks/filename.md

...
```

5. **Highlight important items**:
   - Flag overdue tasks (compare due_date to $TODAY)
   - Show P0 tasks prominently
   - Indicate blocked tasks
   - Show priority cap status (P0: max 3, P1: max 7, P2: max 15)

- If no tasks found, suggest checking BACKLOG.md or creating new tasks

## Manage Tasks

### Update Task Status

```
Mark task [name] as complete
Change task [name] status to [n/s/b/d]
Change task [name] priority to [P0/P1/P2/P3]
Change task [name] category to [category]
Update task [name]
```

**What it does**:
- Updates task file frontmatter fields
- Status codes: n (not_started), s (started), b (blocked), d (done)
- Can update multiple fields at once

**When to use**: As you work on tasks, mark progress

**Detailed Steps**:

**Task Status Updates**:
- "Mark task [name/id] as complete" → Update task file `status: d`
- "Change task [name/id] status to [n/s/b/d]" → Update status field (n=not_started, s=started, b=blocked, d=done)
- "Change task [name/id] priority to [P0/P1/P2/P3]" → Update priority field
- "Change task [name/id] category to [category]" → Update category field
- "Update task [name/id]" → Allow multiple field updates at once

**Task Pruning & Aging**:
- "Find tasks older than [N] days" → List tasks with created_date older than N days
- "Find stale tasks" → Tasks with status 's' (started) but no progress log updates in last 14 days (configurable via config.yaml)
- "Prune completed tasks older than [N] days" → Move tasks with status 'd' and created_date older than N days to archive
- "Show task aging report" → Summary of tasks by age, status, and category

**Categorization Learning**:
- When user corrects categorization, note the correction
- Suggest updating `config.yaml` keywords if pattern emerges
- Learn from context (e.g., if "email Sarah" is categorized as outreach, similar patterns should follow)

---

### Find Tasks

```
Find tasks older than [N] days
Find stale tasks
Show task aging report
```

**What it does**:
- Lists tasks by age, status, or category
- Identifies stale tasks (started but inactive)
- Shows summary report of task health

**When to use**: Weekly review, identifying work that needs attention

---

### Prune Tasks

```
Prune completed tasks older than [N] days
```

**What it does**:
- Moves completed tasks (status: d) older than N days to archive
- Keeps task folder clean and focused

**When to use**: Monthly cleanup

---

### Task Creation

Tasks are automatically created when processing backlog, or you can ask:

```
Create a task: [description]
```

**What it does**:
- Creates new task file in `tasks/` folder
- Auto-categorizes using keywords from `config.yaml`
- Sets default priority and status

**When to use**: When you need to track a specific action item

---

## Task Structure

Each task file includes:
- **Frontmatter**: title, category, priority, status, dates, resource_refs
- **Context**: Why this task exists, ties to goals
- **Next Actions**: Checklist of steps
- **Progress Log**: Notes over time

See `examples/example_files/task-example.md` for format.

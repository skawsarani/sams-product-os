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

---

### Prioritize Tasks

```
What should I work on today based on our priorities?
```

**What it does**:
- Reviews P0/P1 tasks
- Checks deadlines and dependencies
- Suggests focus areas
- Considers team capacity

**When to use**: Daily planning

**Detailed Steps**:

1. **Review Strategy Docs**: Check `knowledge/product-strategy/`
2. **Apply Framework**: 
   - Impact vs. Effort matrix
   - RICE scoring (Reach, Impact, Confidence, Effort)
   - Value vs. Complexity
   - Strategic alignment assessment
3. **Generate Recommendation**: Clear rationale with tradeoffs
4. **Create Visual**: Table or matrix showing options
5. **Define Next Steps**: What decisions need to be made

---

### Prioritize Task List

```
Help me prioritize these tasks: [paste list or reference file]
```

**What it does**:
- Applies prioritization framework (RICE, Impact/Effort, etc.)
- References product strategy
- Provides rationale for each priority

**When to use**: Planning sessions, task reviews

---

### Weekly Planning

```
Help me plan this week's work
```

**What it does**:
1. Reviews last week's progress
2. Checks task priorities
3. Considers upcoming deadlines
4. Suggests weekly focus areas
5. Creates weekly plan document

**When to use**: Monday mornings

---

## Task Structure

Each task file includes:
- **Frontmatter**: title, category, priority, status, dates, resource_refs
- **Context**: Why this task exists, ties to goals
- **Next Actions**: Checklist of steps
- **Progress Log**: Notes over time

See `examples/example_files/task-example.md` for format.

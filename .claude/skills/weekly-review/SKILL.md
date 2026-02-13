---
name: weekly-review
description: Reviews the past week, checks goal progress, identifies blockers and stalled work, and plans next week's priorities. Internal reflection tool. Invoked via /weekly-review or "review my week", "plan next week".
allowed-tools: list_tasks, get_task_summary, find_stale_tasks, Glob, Read, Bash(qmd:*)
argument-hint: [optional: "quick" for condensed version]
---

## Context

Tasks are in `tasks/` with YAML frontmatter (priority, status, due_date, category).
Goals are in `GOALS.md`.
Today's date: $TODAY

**Recommended timing:**
- Friday afternoon (reflection while fresh)
- Sunday evening (prep mode for Monday)
- Monday morning (clarity before week starts)

## Your Task

Help the user reflect on the past week, track goal progress, identify blockers, and plan next week.

If user says "quick" or wants condensed version → Combine all steps into brief summary (1-2 paragraphs per section).

## Step 1: Review Completed Work

**Actions:**
1. Read `tasks/` for tasks with status `d` (done) updated in past 7 days
2. Group by goal alignment (reference `GOALS.md`)

**Output format:**
```
## This Week's Completed Work

### Aligned to Goal: [Goal Name]
- [Task 1] (P0) - Completed [Date]
- [Task 2] (P1) - Completed [Date]

### Aligned to Goal: [Goal Name]
- [Task 3] (P1) - Completed [Date]

### Other Work
- [Task 4] (P2) - Completed [Date]

**Highlights:**
- [Major win or milestone]
- [Concerning pattern or gap, if any]
```

## Step 2: Check Goal Progress

**Actions:**
1. Read `GOALS.md`
2. For each goal, assess:
   - Tasks completed toward this goal
   - Tasks in progress (status `s`)
   - Tasks not started (status `n`)
   - Blockers affecting this goal

**Output format:**
```
## Quarterly Goal Progress

### Goal 1: [Goal Name]
**Target:** [Target date]
**Status:** On Track | At Risk | Behind

**This week:**
- Completed: [X tasks]
- In progress: [Y tasks]
- Not started: [Z tasks]

**Progress toward success criteria:**
- [x] [Completed milestone]
- [ ] [Incomplete milestone]

**Velocity:** [Assessment - "Ahead of schedule", "Need to accelerate", etc.]
```

## Step 3: Identify Blockers

**Actions:**
1. Find tasks with status `b` (blocked)
2. Find tasks with status `s` (started) but no updates in 7+ days (stale)

**Output format:**
```
## Blockers & Stalled Work

### Blocked Tasks
**[Task name]** (P0) - Blocked on: [Dependency]
- Affects: [Goal name]
- Impact: [High/Medium/Low] - [Brief explanation]
- Recommended action: [Suggestion]

### Stalled Tasks (started but inactive 7+ days)
**[Task name]** (P1) - Last updated: [Date]
- Why stalled: [Assessment]
- Recommended: [Continue / Deprioritize / Break down]
```

## Step 4: Plan Next Week

**Actions:**
1. Review tasks with status `n` (not started) or `s` (in progress)
2. Consider goal alignment, priority levels, due dates, dependencies

**Output format:**
```
## Next Week's Priorities

### Must Complete (P0)
1. **[Task]** - Goal: [Goal name]
   - Why critical: [Brief context]

### Should Complete (P1)
1. **[Task]** - Goal: [Goal name]
2. **[Task]** - Goal: [Goal name]

### Nice to Have (P2)
1. **[Task]**

**Capacity check:** [Realistic / Overloaded / Light week]

**Recommendations:**
- [Specific suggestion based on capacity/goals]
- [Risk or opportunity to flag]
```

---

## Quick Version

If user wants condensed output, combine all 4 steps into:

```
## Week in Review

**Completed:** [X tasks] toward [Goal A], [Y tasks] toward [Goal B]
**Goal status:** [Goal A] on track, [Goal B] at risk
**Blockers:** [N blocked], [M stalled]
**Next week focus:** [Top 2-3 priorities]
**Watch out for:** [Key risk or recommendation]
```

---

## Best Practices

- Emphasize goal alignment over task quantity
- Track velocity against quarterly OKRs
- Flag capacity constraints proactively
- Make tradeoffs explicit (what are we NOT doing?)
- Aim for 10-15 minutes reflection time

# Weekly Review Workflow

When user says: "Run weekly review", "Review this week", or "Weekly reflection"

---

## Purpose

Reflect on the past week, track goal progress, identify blockers, and plan priorities for next week. This is your strategic checkpoint to maintain alignment and momentum.

**Recommended timing:**
- Friday afternoon (reflection while fresh)
- Sunday evening (prep mode for Monday)
- Monday morning (clarity before week starts)

---

## Workflow Steps

### Step 1: Review Completed Work

**Prompt the user:**
> Let me review what you accomplished this week.

**Actions:**
1. Read `tasks/` directory for tasks with status `d` (done) updated in past 7 days
2. Group completed work by:
   - Goal alignment (reference GOALS.md)
   - Category (technical, outreach, research, writing, admin)
   - Priority level

**Output format:**
```
## This Week's Completed Work

### ✅ Aligned to Goal: [Goal Name]
- [Task 1] (P0) - Completed [Date]
- [Task 2] (P1) - Completed [Date]

### ✅ Aligned to Goal: [Goal Name]
- [Task 3] (P1) - Completed [Date]

### ✅ Other Work
- [Task 4] (P2) - Completed [Date]

**Highlights:**
- 🎯 [Major win or milestone]
- ⚠️ [Concerning pattern or gap]
```

---

### Step 2: Check Goal Progress

**Prompt the user:**
> Let me check your quarterly goal progress.

**Actions:**
1. Read GOALS.md
2. For each goal, check:
   - Tasks completed toward this goal (from Step 1)
   - Tasks in progress (status `s`)
   - Tasks not started (status `n`)
   - Blockers affecting this goal

**Output format:**
```
## Quarterly Goal Progress

### Goal 1: [Goal Name]
**Target:** [Target date]
**Status:** 🟢 On Track | 🟡 At Risk | 🔴 Behind

**This week:**
- ✅ Completed: [X tasks]
- 🔄 In progress: [Y tasks]
- 📋 Not started: [Z tasks]

**Progress toward success criteria:**
- [x] [Completed milestone]
- [ ] [Incomplete milestone]

**Velocity:** [Assessment - e.g., "Ahead of schedule", "Need to accelerate"]

---

[Repeat for each goal]
```

---

### Step 3: Identify Blockers

**Prompt the user:**
> Let me identify what's blocked or stalled.

**Actions:**
1. Find tasks with status `b` (blocked)
2. Find tasks with status `s` (started) but no updates in 7+ days
3. For each blocker:
   - What's blocking it?
   - Which goal does it affect?
   - What's the impact if it stays blocked?

**Output format:**
```
## Blockers & Stalled Work

### 🚧 Blocked Tasks
**[Task name]** (P0) - Blocked on: [Dependency]
- Affects: [Goal name]
- Impact: [High/Medium/Low] - [Brief explanation]
- Recommended action: [Suggestion]

### ⏸️ Stalled Tasks (started but inactive 7+ days)
**[Task name]** (P1) - Last updated: [Date]
- Why stalled: [Assessment]
- Recommended: [Continue / Deprioritize / Break down]
```

---

### Step 4: Plan Next Week

**Prompt the user:**
> Let me help you prioritize next week.

**Actions:**
1. Review tasks with status `n` (not started) or `s` (in progress)
2. Consider:
   - Goal alignment
   - Priority levels (P0, P1, P2)
   - Due dates
   - Dependencies cleared
   - Capacity (realistic time available)

**Output format:**
```
## Next Week's Priorities

### 🎯 Must Complete (P0)
1. **[Task]** - [Time estimate] - Goal: [Goal name]
   - Why critical: [Brief context]

### 🔥 Should Complete (P1)
1. **[Task]** - [Time estimate] - Goal: [Goal name]
2. **[Task]** - [Time estimate] - Goal: [Goal name]

### 💡 Nice to Have (P2)
1. **[Task]** - [Time estimate]

**Total estimated time:** [X hours/days]
**Capacity check:** [Assessment - e.g., "Realistic", "Overloaded", "Light week"]

**Recommendations:**
- [Specific suggestion based on capacity/goals]
- [Risk or opportunity to flag]
```

---

## Quick Alternative

If user wants condensed version:
> "What did I finish this week, what's blocked, and what's priority next week?"

Combine all 4 steps into single concise response (1-2 paragraphs max per section).

---

## Best Practices

**For PM-specific weekly reviews:**
- Emphasize goal alignment over task quantity
- Track velocity against quarterly OKRs
- Map dependencies when identifying blockers
- Consider stakeholder impact in priorities
- Flag capacity constraints proactively

**Frequency:**
- Run consistently same day/time each week
- Aim for 10-15 minutes reflection time
- Use insights to update GOALS.md quarterly

---

## Related Files

- `GOALS.md` - Quarterly goals referenced throughout
- `tasks/` - All task files with frontmatter
- `workflows/daily-planning.md` - Daily prioritization
- `workflows/process-backlog.md` - Backlog processing

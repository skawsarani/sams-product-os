# Config Example

Example configuration file for task management. Copy this to `config.yaml` at the root of your workspace and customize for your workflow.

---

## File Location

Copy this file to: `config.yaml` (at workspace root)

---

## Example Config

```yaml
# Task Management System Configuration

# Task categories - modify based on your needs
categories:
  - technical      # Development, coding, debugging
  - outreach       # Emails, meetings, networking
  - research       # Learning, analysis, investigation
  - writing        # Documentation, blogs, reports
  - admin          # Administrative, organizational
  - other          # Miscellaneous

# Priority levels
priorities:
  - P0  # Critical/Urgent - do immediately
  - P1  # Important - has deadlines
  - P2  # Normal - regular work
  - P3  # Low - nice to have

# Status codes
statuses:
  n: not_started
  s: started
  b: blocked
  d: done

# Deduplication settings
deduplication:
  similarity_threshold: 0.6  # How similar before flagging (0-1)
  check_categories: true     # Consider category in matching
  check_keywords: true       # Use keyword overlap

# Priority limits (warning thresholds)
priority_limits:
  P0: 3  # Warn if more than 3 P0 tasks
  P1: 5  # Warn if more than 5 P1 tasks

# Task aging (in days)
task_aging:
  prune_completed_after: 30  # Delete done tasks after 30 days
  flag_stale_after: 14       # Flag inactive tasks after 14 days

# Category keywords for auto-categorization
category_keywords:
  technical:
    - code
    - api
    - database
    - deploy
    - fix
    - bug
    - implement
    - develop
    - debug
    - server
  outreach:
    - email
    - contact
    - reach
    - meeting
    - call
    - follow
    - introduce
    - connect
  research:
    - research
    - study
    - learn
    - investigate
    - analyze
    - explore
    - understand
    - evaluate
  writing:
    - write
    - draft
    - document
    - blog
    - article
    - report
    - proposal
    - outline
  admin:
    - schedule
    - organize
    - expense
    - invoice
    - calendar
    - filing
    - review
```

---

## Customization

### Add Your Own Categories

```yaml
categories:
  - technical
  - outreach
  - research
  - writing
  - admin
  - product      # Your custom category
  - design        # Another custom category
```

### Add Category Keywords

```yaml
category_keywords:
  product:
    - feature
    - roadmap
    - spec
    - prd
    - user story
  design:
    - mockup
    - wireframe
    - prototype
    - ui
    - ux
```

### Adjust Deduplication Sensitivity

```yaml
deduplication:
  similarity_threshold: 0.7  # Higher = less sensitive (fewer duplicates flagged)
  check_categories: true
  check_keywords: true
```

### Change Task Aging Settings

```yaml
task_aging:
  prune_completed_after: 60  # Keep completed tasks longer
  flag_stale_after: 7         # Flag stale tasks sooner
```

---

## How It's Used

- **Auto-categorization**: AI uses `category_keywords` to assign categories when creating tasks
- **Deduplication**: AI uses `deduplication` settings to find similar items across initiatives, tasks, and references
- **Task management**: AI uses `priorities`, `statuses`, and `task_aging` for task operations
- **Warnings**: AI warns if you exceed `priority_limits` (too many P0/P1 tasks)

---

## Tips

- Start with the default categories and keywords
- Add keywords as you notice patterns in your work
- Adjust thresholds based on how the AI categorizes your items
- Review and refine monthly


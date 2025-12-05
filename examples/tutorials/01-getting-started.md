# Tutorial 1: Getting Started with PM Co-Pilot

**Time**: 15 minutes  
**Goal**: Set up your workspace and run your first workflow

---

## What You'll Learn

- How to add your context
- How to use the BACKLOG
- How to process ideas into initiatives
- How to use workflows (slash commands)

---

## Step 1: Add Your Context (5 min)

### Your Company & Product

Create `knowledge/company-context/company-overview.md`:

```markdown
# Company Overview

## Mission
[Your company's mission]

## Product
- **What we build**: [Brief description]
- **Target customers**: [Who uses it]
- **Stage**: [Startup / Growth / Enterprise]

## Team
- **Size**: [Number of people]
- **Structure**: [How organized]
```

### About You

Create `knowledge/about-me/about-me.md`:

```markdown
# About Me

## Background
- **Role**: Senior PM
- **Experience**: 5 years in B2B SaaS
- **Strengths**: User research, data analysis

## Working Style
- Prefer concise updates
- Data-driven decisions
- Collaborative approach

## Current Focus
- Q1 Goal: Improve user onboarding
- Learning: Enterprise sales cycles
```

---

## Step 2: Brain Dump Ideas (3 min)

Open `BACKLOG.md` and add ideas, tasks, notes - everything:

```markdown
## Mobile App Crashes
- **Source**: Support tickets (20 this week)
- **Context**: Users on Android 12 experiencing crashes
- **Why now**: Affecting conversion rates

## Enterprise SSO Request
- **Source**: Sales team (Acme Corp deal)
- **Context**: Need SAML SSO for 500 users
- **Why now**: Blocker for $500K deal

## Follow up with Sarah about Q4 goals
- Need to align on OKRs
- Due: End of week

## Meeting notes: Engineering sync
- Discussed API rate limiting
- Need to follow up on infrastructure costs
```

Don't worry about categorizing - just capture everything. The AI will categorize when you process.

---

## Step 3: Process Your Backlog (5 min)

### In Cursor:
```
/backlog
```

Or tell AI:
```
"Process my backlog - read BACKLOG.md and create initiative opportunity assessments in the initiatives/ folder"
```

### What Happens:

AI will:
1. Read your backlog items
2. **Categorize each item** into:
   - **Initiatives** → `initiatives/` folder
   - **Tasks** → `tasks/` folder
   - **References** → `knowledge/references/`
   - **Uncategorized** → Archived in `knowledge/notes/YYYY-MM-DD.md`
3. **Deduplication** across all categories
4. Create structured files for each category
5. Archive remaining inbox to `knowledge/notes/YYYY-MM-DD.md`
6. Clear `BACKLOG.md` for next day

### Result:

You'll get files like:
```
initiatives/
├── mobile-app-crashes.md
└── enterprise-sso-request.md

tasks/
└── follow-up-sarah-q4-goals.md

knowledge/notes/
└── 2024-12-02.md  # Archived inbox snapshot
```

**Initiatives** include:
- Objective, Target customer, Success metrics
- What we know, Research needed
- Solution ideas, Risks, Questions to validate
- Priority (P0-P3)

**Tasks** include:
- Frontmatter: title, category, priority, status, dates
- Context, Next Actions, Progress Log

---

## Step 4: Review an Initiative (2 min)

Open `initiatives/mobile-app-crashes.md`

You'll see something like:

```markdown
# Initiative: Mobile App Crashes

**Priority**: P0
**Status**: Evaluating

## Objective
Reduce mobile app crash rate from 1.8% to <0.5%

## Target Customer
- Mobile-first users (20% of user base)
- Android 12 users specifically

## Success Metrics
| Metric | Current | Target |
|--------|---------|--------|
| Crash Rate | 1.8% | <0.5% |
| Conversion | 62% | 75% |

## What We Know
- 80% of crashes on Android 12
- Affecting 20% of users
- $120K/month revenue impact

## What We Should Research
- [ ] Root cause of Android 12 crashes
- [ ] User tolerance for bugs
- [ ] Competitive benchmarks

... (more sections)
```

---

## Step 5: Try More Workflows

### Get Daily Plan
```
/plan
"What should I work on today?"
```

### Create a Spec
```
/spec mobile-app-crashes
"Generate a product spec from the mobile-app-crashes initiative"
```

### Prioritize Work
```
/prioritize
"Help me prioritize my initiatives based on ROI"
```

---

## What You've Accomplished

✅ Added your context  
✅ Created your first backlog  
✅ Processed ideas into structured initiatives  
✅ Learned how to use workflows  
✅ Created your first spec

---

## Next Steps

- **Tutorial 2**: Working with Initiatives
- **Tutorial 3**: Research and Decision Making
- **Tutorial 4**: Stakeholder Communication

Or explore:
- `examples/workflows/` - See all available workflows
- `examples/example_files/` - View example documents
- `BACKLOG.md` - Keep dumping ideas here

---

## Common Issues

**Q: AI isn't finding my files**
- Use @ mentions: `@BACKLOG.md`, `@knowledge/company-context/`
- Check file paths are correct

**Q: Initiatives are too generic**
- Add more context to your knowledge base
- Be specific in BACKLOG.md about sources and data

**Q: How often should I process backlog?**
- Daily is recommended (keeps inbox clean)
- Weekly if lower volume
- Ad-hoc when needed

**Q: What happens to meeting notes and random thoughts?**
- They get archived in `knowledge/notes/YYYY-MM-DD.md` with the inbox snapshot
- You can search archived notes later if needed

---

**🎉 Congratulations!** You've set up your PM Co-Pilot workspace. Keep using it daily and it becomes your strategic thinking partner.


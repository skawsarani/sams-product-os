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

Open `BACKLOG.md` and add some ideas:

```markdown
## Mobile App Crashes
- **Source**: Support tickets (20 this week)
- **Context**: Users on Android 12 experiencing crashes
- **Why now**: Affecting conversion rates

## Enterprise SSO Request
- **Source**: Sales team (Acme Corp deal)
- **Context**: Need SAML SSO for 500 users
- **Why now**: Blocker for $500K deal

## Dashboard Redesign
- **Source**: User feedback
- **Context**: Current dashboard cluttered, low engagement
- **Why now**: Competitor just launched cleaner version
```

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
2. Create initiative files (one per item)
3. Add opportunity assessment structure
4. Prioritize as P0-P3
5. Clear processed items from BACKLOG.md

### Result:

You'll get files like:
```
initiatives/
├── mobile-app-crashes.md
├── enterprise-sso-request.md
└── dashboard-redesign.md
```

Each with:
- Objective
- Target customer
- Success metrics
- What we know
- Research needed
- Solution ideas
- Risks
- Questions to validate

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
- Weekly is typical
- Daily if high volume
- Ad-hoc when needed

---

**🎉 Congratulations!** You've set up your PM Co-Pilot workspace. Keep using it daily and it becomes your strategic thinking partner.


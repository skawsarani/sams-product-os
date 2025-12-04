# Initiatives

Structured opportunity assessments for potential features, projects, and improvements. Each initiative follows a consistent format to help you evaluate and prioritize work.

## What Goes Here

- Processed backlog items (from `BACKLOG.md`)
- Feature opportunities
- Strategic initiatives
- Problem explorations
- Customer requests (evaluated)

## Initiative Format

Each initiative is an **Opportunity Assessment** with:

1. **Objective** - What we're trying to achieve
2. **Target Customer** - Who this serves
3. **Success Metrics** - How we measure impact
4. **What We Know** - Current data, insights, evidence
5. **What We Should Research** - Open questions, validation needed
6. **Solution Ideas** - Potential approaches (not decisions yet)
7. **Risks** - What could go wrong
8. **Questions to Validate** - Key assumptions to test

## Workflow

### 1. Create Initiative

From backlog:
```
"Process my backlog"
→ AI creates initiative files
```

From scratch:
```
"Create an initiative for [idea/problem]"
→ AI creates opportunity assessment
```

### 2. Expand Details

Before creating PRD or spec:
```
"Expand initiative [name] with more research and details"
→ AI adds depth, flags gaps, suggests next steps
```

### 3. Move to Execution

When ready:
```
"Generate a PRD from initiative [name]"
"Create user stories from initiative [name]"
"Generate spec from initiative [name]"
```

## File Naming

Use descriptive, kebab-case names:
- `mobile-performance-optimization.md`
- `enterprise-sso-integration.md`
- `dashboard-redesign-v2.md`
- `api-rate-limiting.md`

## Priority Levels

Each initiative should have a priority:

- **P0 (Critical)** - Urgent, blocking, or major opportunity
- **P1 (High)** - Important, clear value, should do soon
- **P2 (Medium)** - Valuable but can wait, needs more research
- **P3 (Low)** - Someday/maybe, exploring

## Organization

### Single File
Start with one file per initiative in this folder.

### Subdirectories (Optional)
As initiatives grow complex, create subdirectories:

```
initiatives/
├── mobile-redesign/
│   ├── opportunity-assessment.md
│   ├── user-research.md
│   ├── technical-spec.md
│   └── launch-plan.md
├── enterprise-features/
│   ├── sso-assessment.md
│   ├── rbac-assessment.md
│   └── audit-logs-assessment.md
└── other-initiatives.md
```

## Lifecycle

1. **Raw Idea** → `BACKLOG.md`
2. **Opportunity Assessment** → `initiatives/[name].md`
3. **Expanded** → Add research, details, validate assumptions
4. **Prioritized** → P0-P3
5. **Execution** → Generate PRD, specs, stories
6. **Completed** → Move to `archive/`

## Example

See `examples/example_files/initiative-example.md` for a complete example.

## Commands

From anywhere in the project:

```
"Process my backlog"
→ Creates initiative files from BACKLOG.md

"Create initiative for [idea]"
→ New opportunity assessment

"Expand initiative [name]"
→ Add research, detail, validation plan

"Prioritize initiatives"
→ Rank by value/effort/strategic fit

"Generate PRD from initiative [name]"
→ Convert to full product requirements

"List P0 initiatives"
→ Show critical items

"Archive completed initiatives"
→ Move done items to archive/
```

## Tips

1. **Start lean** - Opportunity assessment first, details later
2. **Research before committing** - Use "expand initiative" workflow
3. **One file per initiative** - Easy to find and reference
4. **Keep it current** - Update as you learn
5. **Archive when done** - Keep this folder focused on active work

---

**Remember**: Initiatives are about evaluation, not commitment. They help you decide what to build, not how to build it.


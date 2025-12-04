# Tutorial 2: Working with Initiatives

**Time**: 20 minutes  
**Goal**: Master the initiative workflow from idea to execution

---

## The Initiative Lifecycle

```
Raw Idea → Opportunity Assessment → Expanded Details → PRD → Execution
   ↓              ↓                       ↓            ↓         ↓
BACKLOG.md   initiatives/         Research Phase   Spec    Build
```

---

## Part 1: Expanding an Initiative (10 min)

You've processed your backlog and have initiative files. Now make them actionable.

### Start with Basic Initiative

You have `initiatives/mobile-app-crashes.md` from Tutorial 1.

### Expand with Research

Tell AI:
```
"Expand the mobile-app-crashes initiative with more details. 
Add:
- Technical analysis needed
- User research plan  
- Competitive benchmarks
- Detailed solution evaluation"
```

Or use slash command:
```
/expand-initiative mobile-app-crashes
```

### What Gets Added:

**More detailed research questions**:
- Specific technical investigations
- User interview guides
- Data analysis needed

**Solution evaluation**:
- Multiple options with pros/cons
- Effort estimates
- Risk analysis
- ROI calculations

**Validation plan**:
- What to test
- How to measure
- Success criteria

---

## Part 2: From Initiative to PRD (10 min)

Once your initiative is well-researched, convert to execution docs.

### Generate PRD

```
/prd mobile-app-crashes
"Generate a comprehensive PRD from the mobile-app-crashes initiative"
```

Or:
```
"Create a PRD from @initiatives/mobile-app-crashes.md using @templates/spec-template.md"
```

### What You Get:

Full PRD with:
- Executive summary
- Problem statement (from initiative objective)
- Requirements (from solution ideas)
- Success metrics (from initiative)
- User stories
- Technical considerations
- Launch plan

### Create Supporting Docs

**User Stories**:
```
/stories mobile-app-crashes
```

**Technical Requirements**:
```
/tech-req mobile-app-crashes  
```

**Launch Plan**:
```
/launch-plan mobile-app-crashes
```

---

## Part 3: Managing Multiple Initiatives

### View All Initiatives

```
"List all my initiatives with their priorities"
```

Result:
```
P0 Initiatives (3):
- mobile-app-crashes.md
- enterprise-sso-request.md
- security-audit.md

P1 Initiatives (5):
- dashboard-redesign.md
- api-rate-limiting.md
...
```

### Prioritize

```
/prioritize
"Help me prioritize my initiatives based on:
- Revenue impact
- User impact  
- Strategic alignment with @knowledge/product-strategy/"
```

### Compare Initiatives

```
"Compare mobile-app-crashes vs dashboard-redesign initiatives. 
Which should I do first?"
```

AI analyzes:
- Impact scores
- Effort estimates
- Strategic fit
- Dependencies
- Recommends priority

---

## Part 4: Initiative Organization

### Single Files (Start Here)

```
initiatives/
├── mobile-performance.md
├── enterprise-sso.md
├── dashboard-redesign.md
└── api-improvements.md
```

### Subdirectories (As They Grow)

When an initiative gets complex:

```
initiatives/
├── mobile-performance/
│   ├── opportunity-assessment.md  ← Original
│   ├── technical-analysis.md      ← Research
│   ├── user-research-findings.md  ← Research
│   ├── prd.md                     ← Execution doc
│   └── launch-plan.md             ← Execution doc
├── enterprise-features/
│   ├── sso-assessment.md
│   ├── rbac-assessment.md
│   └── audit-logs-assessment.md
└── other-simple-initiatives.md
```

---

## Part 5: Common Workflows

### Weekly Review

```
"Review all P0 and P1 initiatives.
For each, tell me:
- Status
- Blockers
- Next steps
- Should priority change?"
```

### Monthly Cleanup

```
"Archive completed initiatives from last month"
```

### Quarterly Planning

```
"Based on my initiatives and @knowledge/product-strategy/,
create a Q2 roadmap"
```

---

## Best Practices

### 1. Start Lean
Don't over-detail initially. Basic opportunity assessment first.

### 2. Expand Before Committing
Use the expand workflow before generating PRDs.

### 3. Keep It Current
Update initiatives as you learn. They're living documents.

### 4. Link Everything
Reference related docs:
```markdown
**Related**:
- Research: @knowledge/briefs-and-specs/mobile-study.md
- Metrics: @knowledge/product-analytics/mobile-dashboard.md
- Initiative: @initiatives/checkout-redesign.md
```

### 5. Archive When Done
Move completed initiatives to `archive/` to keep folder focused.

---

## Examples

### Example 1: Quick Win Initiative

```markdown
# Initiative: Add Social Sharing

**Priority**: P2
**Effort**: Small (1 week)

## Objective
Let users share achievements on social media

## Target Customer
Power users (top 10% activity)

## Success Metrics
- 5% of power users share monthly
- 10% viral coefficient

## What We Know
- Requested by 50+ users
- Competitor has this
- Simple implementation

## Solution
Add share buttons to achievement page

## Next Steps
- [ ] Design mockups
- [ ] 1-week sprint
- [ ] Launch with A/B test
```

### Example 2: Complex Strategic Initiative

```markdown
# Initiative: Enterprise Platform

**Priority**: P0
**Effort**: Large (6 months)

## Objective
Build enterprise-grade features to move upmarket

## Components
1. SSO (SAML, OIDC)
2. RBAC (role-based access)
3. Audit logs
4. Advanced security
5. White-label options

(See subdirectory for detailed assessments of each)
```

---

## Exercises

Try these to practice:

1. **Expand an initiative**: Take one of yours and expand it with research
2. **Generate PRD**: Convert expanded initiative to full PRD
3. **Compare two**: Have AI help you choose between two initiatives
4. **Organize**: If you have 10+ initiatives, try subdirectories

---

## Next Tutorial

**Tutorial 3**: Research and Decision Making
- Synthesizing user research
- Documenting decisions
- Creating frameworks

---

**Key Takeaway**: Initiatives are your "thinking" documents. PRDs/specs are your "doing" documents. Spend time getting initiatives right before rushing to execution.


## GTM Launch Expert

Expert workflow for planning and executing GTM launch plans. Ensures comprehensive coverage of all gaps based on knowledge of product, market, and team.

---

### Create a Launch Plan

```
Create a launch plan for [feature]
```

**What it does**:
- Pre-launch checklist
- Launch timeline and phases
- Go/no-go criteria
- Rollback plan
- Post-launch monitoring
- Ensures all gaps are covered

**When to use**: 2-4 weeks before launch

---

### Launch Checklist

```
Generate a launch checklist for [feature]
```

**What it does**:
- All teams' tasks (product, eng, design, marketing, support)
- Organized by timeline (1 week before, launch day, 1 week after)
- Owners and status tracking
- Validates completeness against knowledge base

**When to use**: Planning launches

---

### Create Implementation Plan

```
Create a phased implementation plan for @initiatives/[name].md
```

**What it does**:
- Creates phased implementation plan
- Breaks down into phases (Foundation, Core Features, Polish & Launch Prep)
- For each phase: deliverables, dependencies, success criteria, testing approach, risk mitigation
- Technical risks and mitigation strategies
- Resource requirements (team, tools, infrastructure)
- Launch criteria and rollout plan

**When to use**: After technical spec is complete, before execution

**Detailed Steps**:

1. **Review Initiative**: Read initiative file and any specs
2. **Define Phases**:
   - Phase 1: Foundation (core infrastructure, setup)
   - Phase 2: Core Features (primary functionality)
   - Phase 3: Polish & Launch Prep (edge cases, optimization, QA)
3. **For Each Phase**:
   - Specific deliverables
   - Dependencies
   - Success criteria
   - Testing approach
   - Risk mitigation
4. **Add Overall Considerations**:
   - Technical risks and mitigation
   - Resource requirements
   - Launch criteria
   - Rollout plan
5. **Consider Capacity**: Reference `knowledge/company-context/` for team capacity

---

### Generate Execution Checklist

```
Create a detailed execution checklist for Phase [N] of @initiatives/[name].md
```

**What it does**:
- Creates detailed checklist for a phase
- Setup tasks (environment, dependencies, tooling)
- Implementation tasks (broken down by component)
- Testing tasks (unit, integration, manual)
- Documentation tasks
- Review & quality checks

**When to use**: Ready to start building a phase

**Detailed Steps**:

1. **Review Phase Plan**: Read implementation plan for the phase
2. **Create Setup Tasks**: Environment, dependencies, tooling, access
3. **Break Down Implementation**: By component, specific tasks
4. **Add Testing**: Unit, integration, manual testing checklists
5. **Add Documentation**: Code comments, API docs, README updates
6. **Add Quality Checks**: Code review, performance, security, accessibility

---

### Post-Launch Review

```
Help me conduct a post-launch review for [feature]
```

**What it does**:
- Metrics vs. targets
- User feedback summary
- What went well / what didn't
- Lessons learned
- Next steps

**When to use**: 2-4 weeks after launch

---

### Validate Launch Readiness

```
Validate that [feature] is ready for launch
```

**What it does**:
- Reviews launch checklist completion
- Validates go/no-go criteria
- Checks all teams are ready
- Identifies any gaps or blockers
- Provides readiness assessment

**When to use**: Final check before launch

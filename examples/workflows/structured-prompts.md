# Structured Workflow Prompts

Step-by-step prompts for moving from idea to execution, inspired by [from-thinking-to-coding](https://github.com/talsraviv/from-thinking-to-coding).

---

## The Workflow

```
1. Opportunity Assessment → 2. Technical Spec → 3. Implementation Plan → 4. Execute
```

Use these prompts in sequence for a complete idea-to-execution flow.

---

## Step 1: Create Opportunity Assessment

**When**: Starting with a raw idea or customer request

**Prompt**:
```
I want your help creating an opportunity assessment for [IDEA/FEATURE].

Interview me conversationally to understand:
- The objective (what we're trying to achieve)
- Target customer (who this serves)
- Success metrics (how we measure impact)
- What we know (current data/insights)
- What we need to research (open questions)
- Solution directions (potential approaches)
- Risks to validate (what could go wrong)

Ask me questions one at a time. Pull insights out of me. Brainstorm together.

When we're done, create the assessment in initiatives/[name].md using the 
initiative format from @initiatives/README.md

Keep it succinct but capture all the gold. Use our conversation words for 
vivid/evocative parts.
```

---

## Step 2: Create Technical Specification

**When**: After opportunity assessment is complete

**Prompt**:
```
Let's create a detailed technical specification for @initiatives/[name].md

Based on the opportunity assessment, generate a comprehensive spec including:

**Product Requirements**:
- User stories and acceptance criteria
- Functional requirements (must-have, should-have, nice-to-have)
- Non-functional requirements (performance, security, accessibility)

**Technical Design**:
- System architecture overview
- Key components and their interactions
- Data models and schemas
- API endpoints (if applicable)
- Integration points

**Implementation Details**:
- Technology stack recommendations
- Third-party dependencies
- Security considerations
- Performance requirements
- Testing strategy

**User Experience**:
- Key user flows
- UI/UX considerations
- Mobile vs desktop differences

Add this as a new section in the initiative file.

Reference @knowledge/product-strategy/ for strategic alignment.
Reference @knowledge/frameworks/ for technical standards.
```

---

## Step 3: Create Implementation Plan

**When**: After technical spec is complete

**Prompt**:
```
Now let's create a phased implementation plan for @initiatives/[name].md

Create a plan with:

**Phase 1: Foundation (Week 1-2)**
- Core infrastructure
- Data models
- Basic authentication
- Development environment setup

**Phase 2: Core Features (Week 3-4)**
- Primary user flows
- Essential functionality
- Basic UI/UX

**Phase 3: Polish & Launch Prep (Week 5-6)**
- Edge cases
- Error handling
- Performance optimization
- Testing and QA

**For each phase, specify**:
- Specific deliverables
- Dependencies
- Success criteria
- Testing approach
- Risk mitigation

**Add**:
- Technical risks and mitigation strategies
- Resource requirements (team, tools, infrastructure)
- Launch criteria and rollout plan

Add this as an "Implementation Plan" section in the initiative file.

Consider team capacity from @knowledge/company-context/ and current workload.
```

---

## Step 4: Generate Execution Checklist

**When**: Ready to start building

**Prompt**:
```
Create a detailed execution checklist for Phase 1 of @initiatives/[name].md

For each deliverable in Phase 1, create:

**Setup Tasks**:
- [ ] Environment configuration
- [ ] Dependencies installed
- [ ] Development tooling ready
- [ ] Access to required services/APIs

**Implementation Tasks** (break down by component):
- [ ] [Component 1]: [Specific task]
- [ ] [Component 1]: [Specific task]
- [ ] [Component 2]: [Specific task]

**Testing Tasks**:
- [ ] Unit tests for [component]
- [ ] Integration tests for [flow]
- [ ] Manual testing checklist

**Documentation Tasks**:
- [ ] Code comments and documentation
- [ ] API documentation (if applicable)
- [ ] README updates

**Review & Quality**:
- [ ] Code review completed
- [ ] Performance tested
- [ ] Security review
- [ ] Accessibility check

Save as initiatives/[name]/phase-1-checklist.md
```

---

## Step 5: Execute with Agent

**When**: Ready to build

**Prompt**:
```
Let's execute Phase 1 of @initiatives/[name].md

Follow the implementation plan in the initiative file.
Use the checklist in initiatives/[name]/phase-1-checklist.md

As we work:
1. Check off completed items in the checklist
2. Flag any blockers or decisions needed
3. Update the initiative file with learnings
4. Document any deviations from the plan

Let's start with the first task: [first item from checklist]
```

---

## Alternative: Condensed Flow

For smaller features or faster iteration:

### Single Prompt for Quick Start

```
Help me quickly scope and plan [FEATURE/IDEA].

First, interview me briefly (5-10 questions) to understand:
- The goal and user need
- Success criteria  
- Technical approach
- Risks and unknowns

Then create:
1. Brief opportunity assessment (1 page)
2. High-level technical approach
3. Simple 2-phase plan (MVP → Polish)
4. Execution checklist for MVP phase

Save assessment in initiatives/[name].md
Save checklist in initiatives/[name]/mvp-checklist.md

Let's keep this lightweight - we can add detail as we learn.
```

---

## Adaptation for Research Synthesis

When starting with research instead of an idea:

```
I have user research in @knowledge/transcripts/

Help me:
1. Synthesize key insights and patterns
2. Identify opportunity areas
3. For top 2-3 opportunities, create opportunity assessments
4. Recommend which to pursue first based on @knowledge/product-strategy/

Then for the top opportunity, let's create a spec and plan.
```

---

## Tips for Using These Prompts

### 1. Customize for Context
Add references to your specific files:
```
Reference @knowledge/about-me/ for my working style preferences
Reference @knowledge/frameworks/ for our prioritization method
Reference @knowledge/product-analytics/ for current metrics
```

### 2. Break Down Large Features
For complex features, create multiple initiatives:
```
initiatives/
├── enterprise-features/
│   ├── sso-assessment.md
│   ├── rbac-assessment.md
│   └── audit-logs-assessment.md
```

### 3. Iterate as You Learn
```
"Update @initiatives/[name].md with what we learned from user testing"
"Revise the technical spec based on engineering feedback"
"Adjust the plan - Phase 1 took longer, let's resequence"
```

### 4. Use for Different Scales
- **Large initiative**: All 5 steps with detailed phases
- **Medium feature**: Steps 1-3, lighter detail
- **Small improvement**: Condensed flow
- **Exploration**: Steps 1-2 only, decide later

---

## Related Workflows

- **Process BACKLOG.md**: See @examples/workflows/backlog.md
- **Expand Initiative**: See @examples/workflows/planning.md
- **Generate PRD**: See @examples/workflows/documents.md
- **Research Synthesis**: See @examples/workflows/research.md

---

## Comparison: Tal's Flow vs PM Co-Pilot

### Tal's from-thinking-to-coding
1. Opportunity assessment
2. `/1-create-a-spec/`
3. `/2-create-a-plan/`
4. `/3-create-agent-instructions/`
5. Execute

### PM Co-Pilot Equivalent
1. Brain dump → `BACKLOG.md`
2. `/backlog` → creates `initiatives/[name].md`
3. Use prompts above → adds spec & plan to initiative
4. `AGENTS.md` (already exists)
5. `/prd [name]` or execute directly

**Key Difference**: We use initiatives as the central artifact that grows from assessment → spec → plan, rather than separate prompt directories.

---

**Credit**: This approach is inspired by [Tal Raviv's from-thinking-to-coding](https://github.com/talsraviv/from-thinking-to-coding) repository. We've adapted the workflow for product management contexts.


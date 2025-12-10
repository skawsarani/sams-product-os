## Product Documentation Expert

Expert workflow for creating and managing briefs, specs, PRDs, and their lifecycle, including decision documentation.

---

### Generate a Spec

```
Generate a spec for [feature name] using @templates/spec-template.md
```

**What it does**:
- Creates comprehensive product spec
- Includes problem statement, requirements, success metrics
- References product strategy for alignment

**When to use**: Starting work on new features

**Detailed Steps**:

1. **Understand the Problem**
   - What user need are we solving?
   - What business goal does this support?
   - What's the current experience vs. desired?

2. **Define Success**
   - What metrics will improve?
   - What does success look like for users?
   - What's the business impact?

3. **Generate Structure** (Use template from `templates/`)
   - Executive Summary
   - Problem Statement
   - User Stories & Jobs-to-be-Done
   - Functional Requirements
   - Non-Functional Requirements
   - Technical Considerations
   - Success Metrics
   - Open Questions
   - Out of Scope

4. **Validate Alignment**
   - Check against product strategy
   - Ensure metrics alignment
   - Flag any conflicts with existing work

---

### Create a Brief

```
Create a project brief for [project name]
```

**What it does**:
- Generates one-pager project overview
- Includes goals, scope, timeline, stakeholders
- Uses `templates/brief-template.md`

**When to use**: Kicking off new initiatives

---

### Write a PRD (Product Requirements Document)

```
Write a PRD for [feature] based on @knowledge/briefs-and-specs/[research-file].md
```

**What it does**:
- Detailed product requirements
- User stories and use cases
- Technical considerations
- Success criteria

**When to use**: Detailed feature planning

---

### Generate User Stories

```
Generate user stories for [feature] targeting [persona]
```

**What it does**:
- Creates "As a [user], I want [goal], so that [benefit]" stories
- Includes acceptance criteria
- Prioritizes by user impact

**When to use**: Sprint planning, feature breakdown

---

### Create Technical Specification

```
Create a detailed technical specification for @initiatives/[name].md
```

**What it does**:
- Creates comprehensive technical spec based on opportunity assessment
- Includes product requirements, technical design, implementation details, user experience

**When to use**: After opportunity assessment is complete

**Detailed Steps**:

1. **Review Initiative**: Read opportunity assessment from initiative file
2. **Generate Product Requirements**:
   - User stories and acceptance criteria
   - Functional requirements (must-have, should-have, nice-to-have)
   - Non-functional requirements (performance, security, accessibility)
3. **Create Technical Design**:
   - System architecture overview
   - Key components and their interactions
   - Data models and schemas
   - API endpoints (if applicable)
   - Integration points
4. **Add Implementation Details**:
   - Technology stack recommendations
   - Third-party dependencies
   - Security considerations
   - Performance requirements
   - Testing strategy
5. **Define User Experience**:
   - Key user flows
   - UI/UX considerations
   - Mobile vs desktop differences
6. **Reference Context**: Use `knowledge/product-strategy/` for strategic alignment, `knowledge/frameworks/` for technical standards

---

### Create a One-Pager

```
Create a one-pager for [project] for [audience: execs/engineers/stakeholders]
```

**What it does**:
- Concise project summary
- Tailored to audience
- Key points, timeline, asks

**When to use**: Stakeholder alignment, approvals

---

### Document a Decision

```
Document the decision to [decision made]
```

**What it does**:
- Creates decision record in `knowledge/proposals/`
- Captures: decision, context, options considered, rationale, tradeoffs
- Includes success criteria
- Tags with date and owner

**When to use**: After key decisions

**Detailed Steps**:

1. Create entry in `knowledge/proposals/` or appropriate location
2. Use format:
   - **Decision**: What was decided
   - **Context**: Why this came up
   - **Options Considered**: What else we looked at
   - **Rationale**: Why we chose this
   - **Tradeoffs**: What we're giving up
   - **Success Criteria**: How we'll know it was right
   - **Date & Owner**: When and who

---

### Evaluate Options

```
Help me evaluate these options: [Option A: ..., Option B: ..., Option C: ...]
```

**What it does**:
- Creates comparison framework
- Assesses pros/cons
- Scores against criteria
- Provides recommendation with rationale

**When to use**: Decision-making

---

### Should We Build This?

```
Should we build [feature]? Here's the context: [paste details]
```

**What it does**:
- Evaluates against product strategy
- Assesses ROI (impact vs. effort)
- Considers alternatives
- Provides clear recommendation

**When to use**: Feature evaluation

---

### Update Document Lifecycle

```
Update the status of [document name] to [status: draft/review/approved/archived]
```

**What it does**:
- Updates document status
- Tracks version history
- Manages document lifecycle
- Archives outdated versions

**When to use**: As documents evolve through their lifecycle

---

### Manage Document Versions

```
Create a new version of [document] with these changes: [changes]
```

**What it does**:
- Creates versioned copy
- Maintains version history
- Tracks changes between versions
- Preserves previous versions for reference

**When to use**: When documents need updates but history is important

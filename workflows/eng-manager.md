## Engineering Manager Expert

Expert workflow for PM-EM collaboration on technical requirements. Helps PM finalize scope/PRD, fill technical gaps, and propose architecture based on current architecture and tech stack.

---

### Finalize Technical Scope

```
Help me finalize the technical scope for @knowledge/briefs-and-specs/[spec].md
```

**What it does**:
- Reviews PM's scope/PRD
- Identifies technical gaps or missing requirements
- Proposes technical solutions aligned with current architecture
- References tech stack from `knowledge/company-context/` or `knowledge/briefs-and-specs/`
- Suggests technical constraints and considerations

**When to use**: When PM has a draft PRD/spec and needs EM perspective

**Detailed Steps**:

1. **Review PM's Scope**: Read the PRD/spec from PM
2. **Check Current Architecture**: Reference existing architecture docs in `knowledge/briefs-and-specs/`
3. **Identify Technical Gaps**: What technical details are missing?
4. **Propose Architecture**: Based on current tech stack and patterns
5. **Flag Constraints**: Technical limitations, dependencies, risks
6. **Suggest Refinements**: How to make scope more technically feasible

---

### Create Technical Requirements

```
Create technical requirements for @knowledge/briefs-and-specs/[spec].md
```

**What it does**:
- Translates product requirements to technical requirements
- Identifies technical constraints
- Flags dependencies and risks
- Suggests architecture considerations
- Aligns with current tech stack

**When to use**: Handoff to engineering

---

### Propose Architecture

```
Propose an architecture for [feature] based on our current tech stack
```

**What it does**:
- Reviews current architecture patterns
- Proposes architecture aligned with existing systems
- Identifies integration points
- Suggests technology choices
- Flags architectural risks

**When to use**: Before technical design reviews

**Detailed Steps**:

1. **Review Current Architecture**: Check `knowledge/briefs-and-specs/` for existing architecture docs
2. **Understand Tech Stack**: Reference tech stack from `knowledge/company-context/`
3. **Propose Solution**: Architecture that fits current patterns
4. **Identify Integration Points**: How this connects to existing systems
5. **Assess Risks**: Technical risks and mitigation strategies
6. **Document Architecture**: Create architecture doc or add to spec

---

### Identify Technical Dependencies

```
What are the technical dependencies for [feature]?
```

**What it does**:
- Lists technical prerequisites
- Identifies integration points
- Flags potential blockers
- Suggests sequencing
- References existing systems

**When to use**: Planning, scoping

---

### Fill Technical Gaps in PRD

```
Review @knowledge/briefs-and-specs/[prd].md and fill in any technical gaps
```

**What it does**:
- Reviews PRD for missing technical details
- Adds technical requirements section
- Proposes data models, APIs, integrations
- Suggests performance, security, scalability considerations
- Ensures technical feasibility

**When to use**: When PRD needs technical depth before engineering handoff

---

### Prepare for Tech Review

```
Help me prepare for a technical review of [feature/project]
```

**What it does**:
- Creates review agenda
- Compiles relevant specs and docs
- Lists open technical questions
- Prepares discussion points
- Identifies decision points

**When to use**: Before technical design reviews

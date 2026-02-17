---
name: write-doc
description: Generates PM documents (PRDs, specs, briefs, user stories, decision docs) from templates and knowledge base context. Supports two modes — auto-generate for immediate first drafts, or co-authoring for guided iterative writing. Invoked when asked to write, generate, or co-author product documents.
argument-hint: [doc-type] [name] — types: prd, brief, spec, user-stories, decision
---

# Product Documentation Generator

Generate comprehensive product documentation (PRDs, briefs, specs, user stories, decision docs) with full context from your knowledge base.

## Contents

- [Modes](#modes)
- [Quick Start](#quick-start)
- [Core Workflow](#core-workflow) (Steps 1-6: Request, Context, Template, Draft, Validate, Present)
- [PRD Generation](#prd-generation)
- [Brief Generation](#brief-generation)
- [Spec Generation](#spec-generation)
- [User Stories Generation](#user-stories-generation)
- [Decision Documentation](#decision-documentation)
- [Quality Checklist](#quality-checklist)
- [Advanced Usage](#advanced-usage)
- [Assets Reference](#assets-reference)

## Modes

This skill supports two modes:

**Auto-Generate Mode** (default): Generates a complete first draft from templates and knowledge base context. Use when you want an immediate, comprehensive document.
- Triggered by: `/write-doc prd feature-name`, `/write-doc spec feature-name`, or "generate a PRD for X"

**Co-Authoring Mode**: Guided, iterative document creation through structured conversation — context gathering, section-by-section refinement, and reader testing. Use when you want collaborative, high-quality writing.
- Triggered by: `/write-doc` with collaborative intent, "co-author a doc", "help me write a spec", or "let's work on a PRD together"
- See `references/coauthoring-workflow.md` for the full co-authoring workflow

**How to choose:**
- Need a quick first draft? → Auto-generate
- Want to iterate and refine together? → Co-authoring
- Not sure? → Auto-generate first, then switch to co-authoring for refinement

## Quick Start

**Arguments:** `$ARGUMENTS`

Parse `$ARGUMENTS` to determine:
1. **Document type**: prd, brief, spec, user-stories, decision
2. **Subject name**: The feature/project name
3. **Mode hint**: If user language suggests collaboration ("help me write", "let's co-author", "work together on"), use co-authoring mode

If document type is not specified, ask the user which type they need.

**How it works (auto-generate):**
1. Identify document type needed (or ask if ambiguous)
2. Gather context from knowledge base and existing files
3. Select appropriate template from assets/
4. Generate complete first draft
5. Present for review and iteration

**How it works (co-authoring):**
1. Follow the workflow in `references/coauthoring-workflow.md`
2. Three stages: Context Gathering → Refinement & Structure → Reader Testing

## Core Workflow

Follow this workflow for auto-generate mode:

### Step 1: Understand the Request

Identify:
- Document type (PRD, brief, spec, user stories, decision doc)
- Subject (feature/project name, decision made)
- Any specific requirements or constraints mentioned
- Target audience (if specified)

If document type is ambiguous, ask the user which type they need using the table above as reference.

### Step 2: Gather Context

**Always pull information from these sources (in order of priority):**

1. **Existing related documents**:
   - Check `initiatives/` for related strategic opportunities and initiatives
   - Look for existing specs/briefs/initiatives
   - Look for related PRDs, specs, or briefs that might provide context

2. **Product strategy and frameworks**:
   - `knowledge/product-strategy/` - Product vision, roadmap, strategic pillars
   - `knowledge/frameworks/` - PM frameworks and methodologies to apply
   - `knowledge/company-context/` - Company vision, mission, values

3. **User research**:
   - `meetings/` - User interviews, stakeholder meetings
   - Look for relevant user insights, pain points, quotes

4. **Writing style**:
   - `knowledge/voice-samples/` - Match writing tone and style
   - `knowledge/about-me/` - Personal preferences and communication style

5. **Process and standards**:
   - `knowledge/processes/` - Team rituals, decision-making frameworks
   - `knowledge/product-analytics/` - Current metrics, KPIs (if available)

**Context gathering approach:**
- Use `qmd query "topic"` for semantic search across knowledge/, meetings/, and initiatives/ (best for open-ended context gathering)
- Use `qmd search "keyword"` for exact term lookups
- Use Glob/Grep only for known file patterns or after qmd narrows the search space
- Focus on recent and relevant documents
- Prioritize quality over quantity - better to deeply understand 2-3 key docs than skim 20
- If user references specific files with @ mentions, prioritize those

### Step 3: Select Template

Load the appropriate template from this skill's `assets/` directory:
- `assets/prd-template.md` - For PRDs
- `assets/brief-template.md` - For project briefs
- `assets/spec-template.md` - For product specs
- `assets/user-stories-template.md` - For user stories
- `assets/decision-doc-template.md` - For decision documentation

### Step 4: Generate Complete First Draft

**Critical: Generate a COMPLETE first draft.** Do not leave placeholder text or TODOs unless genuinely unknown.

**For each section in the template:**
1. Fill with specific, contextual content based on gathered information
2. Use actual data, metrics, and insights from the knowledge base
3. Include concrete examples and specific details
4. Match writing style from voice samples
5. Flag genuine unknowns as "Open Questions" rather than leaving blank
6. If a section truly doesn't apply, either remove it or explain why it's N/A

**Quality standards:**
- Every statement should be specific and actionable
- Replace template placeholders with real content
- Use actual user quotes from transcripts when available
- Include real metrics from product-analytics (or note current/target as TBD)
- Cross-reference related documents for consistency
- Ensure strategic alignment with product-strategy files

### Step 5: Validate Before Presenting

Run through the Quality Checklist (below) before showing the document. Fix any issues found. If a section feels thin or generic, revisit context sources for richer content rather than presenting filler.

### Step 6: Present and Iterate

Present the generated document with:
1. **Summary**: Brief overview of what was generated
2. **What was included**: Key sections populated and their sources
3. **What needs review**: Sections that need user input or validation
4. **Open questions**: Genuine unknowns that surfaced during generation
5. **Next steps**: Suggested actions (e.g., "Review success metrics", "Add technical details")

Then iterate based on user feedback. After each round of revisions, re-validate against the Quality Checklist before presenting updates.

## PRD Generation

**Template:** `assets/prd-template.md`

**Comprehensive PRD structure:**
- Executive Summary (TL;DR, problem, solution, metrics, stakeholders)
- Market & Competitive Context
- User Research & Insights
- Product Strategy & Alignment
- Product Requirements (must-have, should-have, nice-to-have)
- Success Criteria & Metrics
- User Experience & Design
- Technical Considerations
- Go-to-Market Strategy
- Timeline & Milestones
- Risks & Mitigations

**PRD-specific guidelines:**
1. **Start with "Why"**: Always lead with business value and user impact
2. **Be comprehensive but scannable**: Use tables, bullets, clear headers
3. **Include competitive context**: Reference market research if available
4. **Define success clearly**: Specific metrics with current → target values
5. **Call out scope**: Explicitly state what's out of scope
6. **Add evidence**: Support claims with user research, data, or market insights
7. **Consider cross-functional needs**: Marketing, sales, support, legal

**Context sources for PRDs:**
- Primary: `initiatives/`
- Supporting: `knowledge/product-strategy/`, `meetings/`, `knowledge/product-analytics/`

## Brief Generation

**Template:** `assets/brief-template.md`

**Project brief structure:**
- TL;DR
- Overview (what, why, who)
- Goals & Success Metrics
- Scope (in/out)
- Timeline & Milestones
- Team & Stakeholders
- Context & Background
- Approach
- Risks & Open Questions
- Decision Log & Updates

**Brief-specific guidelines:**
1. **Keep it concise**: Briefs are 1-2 pages, high-level overviews
2. **Focus on alignment**: Getting everyone on the same page about goals
3. **Clear scope**: What's in and out should be crystal clear
4. **Actionable next steps**: What needs to happen to move forward
5. **Stakeholder clarity**: Who's involved and their roles

**When to create from opportunities:**
- If user provides an opportunity file, expand it into initiative format
- Add structured assessment: target customer, success metrics, research questions
- Link back to original opportunity

## Spec Generation

**Template:** `assets/spec-template.md`

**Product spec structure:**
- Executive Summary
- Context & Background
- User Research & Insights
- User Stories & Jobs-to-be-Done
- Functional Requirements (P0, P1, P2)
- Non-Functional Requirements
- User Experience & Design
- Technical Considerations
- Success Criteria & Metrics
- Launch & Rollout Plan
- Timeline & Milestones
- Risks & Open Questions

**Spec-specific guidelines:**
1. **User-centric**: Lead with user stories and JTBD
2. **Prioritized requirements**: Clear P0/P1/P2 prioritization
3. **Acceptance criteria**: Every requirement has testable criteria
4. **Design considerations**: Reference design files if available
5. **Technical feasibility**: High-level architecture, dependencies, risks
6. **Launch plan**: How we'll roll out (phased, beta, full launch)

**Spec workflow:**
1. Review related opportunities or initiatives
2. Extract user stories and pain points
3. Define functional requirements with acceptance criteria
4. Add non-functional requirements (performance, security, accessibility)
5. Outline user flows and design considerations
6. Document technical dependencies and risks

## User Stories Generation

**Template:** `assets/user-stories-template.md`

**User stories structure:**
- Feature Overview
- Target Personas
- Core User Stories (As a [user], I want [goal], so that [benefit])
- Acceptance Criteria
- Edge Cases & Error Handling
- Non-Functional Stories
- Story Prioritization
- Story Map / User Journey

**User stories guidelines:**
1. **Follow standard format**: "As a [user], I want [goal], so that [benefit]"
2. **Specific acceptance criteria**: Each story has 3-5 testable criteria
3. **Include edge cases**: Error handling, validation, boundary conditions
4. **Prioritize**: P0 (must-have), P1 (should-have), P2 (nice-to-have)
5. **Add non-functional stories**: Performance, accessibility, security
6. **Create story map**: Visualize user journey and story relationships
7. **Reference personas**: Target specific user types from knowledge base

**User stories workflow:**
1. Start with spec or PRD if available (or create minimal context)
2. Identify target user personas
3. Map user journey and key goals
4. Generate stories for each step in the journey
5. Add acceptance criteria for each story
6. Include edge cases and error scenarios
7. Prioritize by user impact and business value

**Can be generated from:**
- Existing spec or PRD
- Opportunity or initiative file
- Standalone feature request
- Backlog item

## Decision Documentation

**Template:** `assets/decision-doc-template.md`

**Decision doc structure:**
- Decision Summary
- Context (why this came up)
- Options Considered
- Decision Made
- Rationale
- Tradeoffs
- Success Criteria
- Implementation Plan
- Owner & Timeline

**Decision doc guidelines:**
1. **Clear decision statement**: What was decided, in one sentence
2. **Rich context**: Why this decision came up, what's changed
3. **Options evaluated**: What else was considered and why not chosen
4. **Explicit tradeoffs**: What we're giving up by choosing this
5. **Measurable success**: How we'll know this was the right call
6. **Owner assignment**: Who's responsible for implementation
7. **Save location**: Typically `initiatives/` or `initiatives/`

**Decision doc workflow:**
1. Capture the decision made
2. Document context and background
3. List all options that were considered
4. Explain rationale for chosen option
5. Call out tradeoffs and what we're giving up
6. Define success criteria
7. Assign owner and timeline

## Quality Checklist

Before presenting any generated document, verify:

- [ ] All template sections are filled (or explicitly marked N/A with reason)
- [ ] No placeholder text like [TODO], [X], [Name] remains
- [ ] Metrics have actual values (or marked as "Current: TBD, Target: TBD")
- [ ] References to user research include actual quotes or insights
- [ ] Strategic alignment is explicit and references actual strategy docs
- [ ] Writing style matches voice samples (if available)
- [ ] Open questions are captured in dedicated section (not as TODOs)
- [ ] Related documents are cross-referenced
- [ ] Document has clear owner, date, and status
- [ ] Success metrics are specific and measurable
- [ ] Out of scope items are explicitly called out

## Advanced Usage

### Generate from Opportunities

When user says "create a PRD/spec from [opportunity]":
1. Read the opportunity or initiative file from `initiatives/`
2. Extract key context: problem, target users, strategic value
3. Expand into full PRD/spec structure
4. Link back to original opportunity for traceability

### Generate from Initiatives

When user references an initiative file:
1. Read the initiative from `initiatives/` or wherever stored
2. Use as primary source of truth for context
3. Expand into requested document type
4. Maintain consistency with initiative content

### Expand Existing Documents

When user says "expand this spec into a PRD":
1. Read existing document
2. Identify gaps between current and target format
3. Fill in missing sections with researched content
4. Preserve all existing content
5. Note what was added in the changelog

### Update Document Lifecycle

When user says "update status to [approved/in-review/etc]":
1. Update status field in document header
2. Add changelog entry with date and change
3. Note in decision log if applicable

## Assets Reference

All templates are in this skill's `assets/` directory (NOT root `/templates/`):
- `assets/prd-template.md` - Comprehensive PRD (15+ sections)
- `assets/brief-template.md` - Project brief (1-2 pages)
- `assets/spec-template.md` - Product spec (10+ sections)
- `assets/user-stories-template.md` - User stories format
- `assets/decision-doc-template.md` - Decision documentation

**Note**: Root `/templates/` directory contains user-facing templates for voice samples, frameworks, and general PM templates.

Templates are used as structure but never modified. Generated documents are saved to user's preferred location (typically `initiatives/` or current directory).

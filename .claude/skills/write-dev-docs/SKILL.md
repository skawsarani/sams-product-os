---
name: write-dev-docs
description: Generates best-in-class developer documentation (API references, integration guides, code recipes, Postman collections) from OpenAPI specs, code, natural language, or PRDs. Stripe-quality output. Invoked when asked to write API docs, developer guides, code samples, quickstarts, or Postman collections.
argument-hint: [doc-type] [name] — types: api-reference, guide, recipe, postman
---

# Developer Documentation Generator

Generate Stripe-quality developer documentation — API references, integration guides, code recipes, and Postman collections — from any input source.

## Contents

- [Quick Start](#quick-start)
- [Doc Types](#doc-types)
- [Input Sources](#input-sources)
- [Core Workflow](#core-workflow) (Steps 1-6: Request, Context, Format, Generate, Validate, Present)
- [API Reference](#api-reference)
- [Integration Guide](#integration-guide)
- [Code Recipe](#code-recipe)
- [Postman Collection](#postman-collection)
- [Quality Checklist](#quality-checklist)
- [Assets Reference](#assets-reference)

## Quick Start

**Arguments:** `$ARGUMENTS`

Parse `$ARGUMENTS` to determine:
1. **Doc type**: api-reference, guide, recipe, postman
2. **Subject name**: The resource, feature, or API being documented
3. **Additional context**: Language preferences, audience level, specific endpoints

If doc type is not specified, ask the user which type they need.

**Triggers:**
- `/write-dev-docs api-reference payments` — API reference for payments resource
- `/write-dev-docs guide getting-started` — Integration quickstart guide
- `/write-dev-docs recipe create-payment` — Multi-language code recipe
- `/write-dev-docs postman payments-api` — Exportable Postman collection
- "Write API docs for..." / "Create a developer guide for..." / "Generate code samples for..."

**Scope — this skill is for:**
- API endpoint documentation (REST)
- Developer integration guides and tutorials
- Multi-language code samples and recipes
- Postman/API client collections

**NOT for:**
- PM documents (PRDs, specs, briefs) → use `write-doc`
- UX copy or UI text → use `write-ux-copy`
- SDK source code or library implementation
- Internal architecture docs

## Doc Types

| Type | Command | Output | Audience | Reference |
|------|---------|--------|----------|-----------|
| API Reference | `api-reference [resource]` | Endpoint-by-endpoint reference with params, responses, errors | Developers integrating the API | `references/api-reference-format.md` |
| Integration Guide | `guide [name]` | Step-by-step tutorial from zero to working code | Developers new to the platform | `references/guide-format.md` |
| Code Recipe | `recipe [use-case]` | Multi-language copy-paste snippets (cURL, Node.js, Python) | Developers building specific features | `references/code-recipe-format.md` |
| Postman Collection | `postman [api-name]` | Exportable Postman v2.1 JSON with test scripts | Developers testing and exploring the API | `references/postman-format.md` |

## Input Sources

The workflow adapts based on what the user provides:

| Source | Detection | Workflow Adaptation |
|--------|-----------|-------------------|
| **OpenAPI/Swagger spec** | User provides `.yaml`/`.json` file or URL | Parse spec → extract endpoints, schemas, auth → generate structured docs |
| **Existing code/routes** | User points to route files, controllers, or handlers | Infer API contracts from code → extract params, responses, middleware → document |
| **Natural language + knowledge base** | User describes the API verbally | Pull from `initiatives/`, `knowledge/` → construct API docs from requirements and context |
| **PRD/technical spec** | User references a spec or initiative file | Extract API requirements, resource models, error codes → generate developer-facing docs |

## Core Workflow

### Step 1: Understand the Request

Identify:
- **Doc type**: api-reference, guide, recipe, or postman
- **Subject**: Resource name, API name, or use case
- **Input source**: What information is available (spec, code, NL, PRD)
- **Target audience**: Experience level (beginner, intermediate, advanced)
- **Language preferences**: Which code languages to include (default: cURL, Node.js, Python)

If doc type is ambiguous, ask the user. If input source is unclear, ask what they have available.

### Step 2: Gather Context

**Always pull information from these sources (in order of priority):**

1. **User-provided input**:
   - OpenAPI specs, code files, PRDs, or natural language description
   - Any existing documentation to build on or replace

2. **Initiative and API context**:
   - Search `initiatives/` for files related to the API or resource being documented
   - `knowledge/references/` — API standards, conventions, and strategic context

3. **Goals and strategy**:
   - `GOALS.md` — Check for goals related to developer experience or this API
   - `knowledge/product-strategy/` — Product vision relevant to the API
   - `knowledge/processes/` — Technical standards and release processes

4. **Tasks and decisions**:
   - `tasks/` — Related developer experience tasks
   - Look for prior decisions on API design, naming, versioning

**Context gathering approach:**
- Use Glob and Grep to find relevant files — don't read everything
- Use `qmd query` for semantic search across knowledge base
- Focus on API contracts, resource models, and error definitions
- If user references specific files with @ mentions, prioritize those

### Step 3: Load Format Reference

Load the type-specific reference file from `references/`:
- `references/api-reference-format.md` — For API references
- `references/guide-format.md` — For integration guides
- `references/code-recipe-format.md` — For code recipes
- `references/postman-format.md` — For Postman collections

These contain the quality standards, conventions, and structural rules for each doc type.

### Step 4: Generate Using Template

Load the corresponding template from `assets/` and generate complete content:
- `assets/api-reference-template.md` — API reference scaffold
- `assets/guide-template.md` — Integration guide scaffold
- `assets/code-recipe-template.md` — Code recipe scaffold
- `assets/postman-collection-template.json` — Postman collection skeleton

**Critical: Generate COMPLETE content.** Every section must have real, specific content. No placeholders, no `[TODO]`, no `...` ellipsis in code samples.

**For each section:**
1. Fill with specific, contextual content based on gathered information
2. Write working code examples that use real endpoints and parameters
3. Include actual error codes and their resolutions
4. Use test/sandbox credentials in examples (never real keys)
5. Flag genuine unknowns as "Open Questions" rather than leaving blank

### Step 5: Validate Against Quality Checklist

Run through the Quality Checklist (below) before presenting. This is a **hard gate** — fix any failures before showing the document to the user. If a section is thin, revisit context sources rather than presenting filler.

### Step 6: Present and Iterate

Present the generated documentation with:
1. **Summary**: What was generated and for which API/resource
2. **Input sources used**: What context informed the output
3. **Assumptions made**: "I assumed X — is that right?"
4. **What needs review**: Sections requiring user validation (auth details, rate limits, error codes)
5. **Open questions**: Genuine unknowns that surfaced
6. **Next steps**: Related docs to generate (e.g., "Want me to create a guide for this API?")

Then iterate based on feedback. Re-validate against the Quality Checklist after each revision.

## API Reference

**Template:** `assets/api-reference-template.md`
**Format rules:** `references/api-reference-format.md`

**Structure per resource:**
- Resource overview (what it represents, when to use it)
- Authentication block (how to authenticate requests)
- Rate limits table
- The Resource Object (full attribute table)
- Per-endpoint sections:
  - Description and use case
  - Parameters table (name, type, required/optional, description)
  - Request examples (cURL, Node.js, Python)
  - Response object table
  - Response JSON example
  - Error table (code, status, description, resolution)
  - Related endpoints

**API Reference guidelines:**
1. **Auth first**: Every reference page starts with how to authenticate
2. **Every parameter documented**: No param left undescribed — include type, constraints, default values
3. **Every error has a resolution**: Don't just list error codes — tell developers how to fix them
4. **Working examples**: Code samples must be copy-paste ready with test credentials
5. **Stripe naming conventions**: snake_case for params, prefixed IDs (`pay_`, `txn_`, `mer_`), expandable objects
6. **Rate limits and pagination**: Always document these — developers need them for production code
7. **Idempotency**: Document idempotency key support where applicable
8. **Versioning**: Note API version in every page header

## Integration Guide

**Template:** `assets/guide-template.md`
**Format rules:** `references/guide-format.md`

**Structure:**
- Overview ("By the end of this guide, you'll have...")
- Prerequisites (exact versions, install commands)
- Sequential steps (each with code, expected output, error handling)
- Testing your integration (sandbox scenarios)
- Next steps and related resources

**Guide guidelines:**
1. **Outcome-first framing**: Lead with what the developer will accomplish
2. **Sequential atomic steps**: Each step does exactly one thing
3. **Expected output per step**: Show what success looks like after each step
4. **Inline error handling**: Address common mistakes right where they happen
5. **Sandbox-first**: Always use test/sandbox credentials in examples
6. **Progressive disclosure**: Quickstart (10 min) → Full guide (1 hr) → Reference docs
7. **Callout boxes**: Use NOTE, WARNING, TIP, SECURITY callouts for important asides

## Code Recipe

**Template:** `assets/code-recipe-template.md`
**Format rules:** `references/code-recipe-format.md`

**Structure:**
- Recipe title (outcome-oriented: "Accept a Payment", not "POST /payments")
- When to use / What you'll need
- Code in cURL, Node.js, Python (consistent variable names)
- What this does (plain-English explanation)
- Expected response JSON
- Variations (additive diffs from base)
- Error handling table
- Related recipes

**Recipe guidelines:**
1. **Outcome-oriented titles**: "Create a Refund", not "POST /refunds"
2. **Copy-paste ready**: Every snippet runs as-is with test credentials
3. **Consistent structure across languages**: Same variable names, same flow, same comments
4. **Complete not minimal**: Include headers, error handling, response parsing
5. **Variations as additive diffs**: Show what changes from the base recipe, not a full rewrite

## Postman Collection

**Template:** `assets/postman-collection-template.json`
**Format rules:** `references/postman-format.md`

**Structure:**
- Collection-level Bearer auth with `{{secret_key}}`
- Collection variables: `base_url`, `secret_key`, `publishable_key`, resource IDs
- Resource folders with Create/Retrieve/Update/List/Delete requests
- Test scripts with status checks and variable chaining
- Pre-filled example request bodies

**Postman guidelines:**
1. **Collection-level auth**: Auth inherits to all requests via `{{secret_key}}`
2. **Environment file shipped separately**: Collection variables for defaults, environment file for secrets
3. **Test scripts on every request**: Minimum 3 assertions per request (status, content-type, body structure)
4. **Variable chaining**: Create → save ID to variable → use in subsequent requests
5. **CRUD folder ordering**: Create, Retrieve, Update, List, Delete
6. **Pre-filled bodies**: Example request bodies with realistic test data, not empty objects

## Quality Checklist

Before presenting any generated documentation, verify all applicable items. This is a **hard gate** — fix failures before presenting.

### Completeness
- [ ] All template sections are filled with real content (no placeholders)
- [ ] No `[TODO]`, `[placeholder]`, `[NAME]`, or `...` text remains
- [ ] Every endpoint has request examples in all specified languages
- [ ] Every parameter is documented with type, constraints, and description
- [ ] Every error code has a resolution (not just a description)

### Authentication
- [ ] Auth section appears before any endpoint documentation
- [ ] Examples use test/sandbox credentials (never real keys)
- [ ] Auth method is explicitly stated (Bearer token, API key, OAuth)
- [ ] Key format and placement documented (header, query param, body)

### Developer Experience
- [ ] Code samples are copy-paste ready (complete, runnable)
- [ ] Expected responses shown for every request example
- [ ] Error scenarios include resolution steps
- [ ] Rate limits documented where applicable
- [ ] Pagination pattern documented for list endpoints

### Correctness
- [ ] HTTP methods match the operation (GET for read, POST for create, etc.)
- [ ] Status codes are correct (201 for create, 200 for retrieve, 204 for delete)
- [ ] Request/response JSON is valid and consistent
- [ ] Parameter types match between documentation and examples
- [ ] Endpoint paths are consistent throughout the document

### Format
- [ ] Resource names use snake_case
- [ ] IDs use prefixed format where applicable (`pay_`, `txn_`, `mer_`)
- [ ] Code samples follow language-specific conventions
- [ ] Tables are properly formatted with consistent columns
- [ ] Headers follow logical hierarchy (H1 → H2 → H3)

### Guide-Specific (when applicable)
- [ ] Opens with outcome statement ("By the end of this guide...")
- [ ] Prerequisites list exact versions and install commands
- [ ] Each step has expected output
- [ ] Callout boxes used for warnings and tips
- [ ] Next steps section links to related docs

### Postman-Specific (when applicable)
- [ ] Collection uses Postman v2.1 schema
- [ ] Auth is set at collection level with `{{secret_key}}`
- [ ] Test scripts on every request (minimum 3 assertions)
- [ ] Variable chaining works across requests in sequence
- [ ] Environment variables separated from collection variables
- [ ] JSON is valid and importable

## Assets Reference

All templates are in this skill's `assets/` directory:
- `assets/api-reference-template.md` — Endpoint-by-endpoint API reference
- `assets/guide-template.md` — Step-by-step integration guide
- `assets/code-recipe-template.md` — Multi-language code recipe
- `assets/postman-collection-template.json` — Postman v2.1 collection

Format references are in `references/`:
- `references/api-reference-format.md` — Stripe-level endpoint documentation rules
- `references/guide-format.md` — Tutorial and guide writing standards
- `references/code-recipe-format.md` — Per-language code sample conventions
- `references/postman-format.md` — Collection architecture and test script rules

Templates are used as structure but never modified. Generated documents are saved to user's preferred location (typically `initiatives/` or current directory).

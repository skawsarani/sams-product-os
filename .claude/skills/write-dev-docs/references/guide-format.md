# Integration Guide Format Guide

Standards for writing developer tutorials and integration guides.

## Guide Taxonomy

| Type | Time | Audience | Purpose |
|------|------|----------|---------|
| **Quickstart** | ~10 min | New developers | Get something working fast — minimum viable integration |
| **Integration Guide** | ~1 hr | Developers building features | Complete walkthrough from zero to production-ready |
| **Conceptual Guide** | ~15 min | Developers learning the system | Explain how something works without step-by-step instructions |

When in doubt, default to **Integration Guide**. Quickstarts are subsets; conceptual guides are companions.

## Step Structure Rules

### Atomic Steps

Each step does exactly one thing. A developer should be able to:
1. Read the step title and know what they'll do
2. Execute the code/action
3. See the expected output
4. Know they succeeded before moving on

### Step Titles

- **Always start with an action verb**: Install, Configure, Create, Send, Verify, Test
- **Include the object**: "Install the SDK", not just "Install"
- **Be specific**: "Create Your First Payment", not "Use the API"

**Good:** "Step 3: Create Your First Payment"
**Bad:** "Step 3: Getting Started with Payments"

### Step Body Structure

```markdown
## Step N: [Verb] [Object]

[1-2 sentences: Why this step is necessary. What it accomplishes.]

[Code block or action]

**Expected output:**

[What success looks like — console output, dashboard state, etc.]

[Optional: Error handling table for common mistakes at this step]
```

### Expected Output

Every step that produces output must show what the developer should see. This is non-negotiable.

- Console output: Show the exact text
- API responses: Show the JSON
- Dashboard changes: Describe what to look for
- File changes: Show the relevant diff or file state

## Prerequisites Format

Prerequisites are a checklist with exact versions and install commands:

```markdown
## Prerequisites

Before you begin, make sure you have:

- [ ] **Account**: A sandbox account ([sign up here](link))
- [ ] **API Key**: Secret key from Settings → API Keys (starts with `sk_test_`)
- [ ] **Node.js** v18+ (`node --version`)
- [ ] **npm** v9+ (`npm --version`)
```

Rules:
- Include the verification command in parentheses
- Link to download/signup pages
- Specify minimum versions, not exact versions
- List account/credential prereqs first, then tooling

## Language Choices

- Default to **Node.js** for primary code examples in guides
- Include cURL for any standalone API call
- Offer Python as an alternative when the guide is language-agnostic
- If the guide is framework-specific, use that framework's language

## Callout Boxes

Use these sparingly — max 2-3 per guide:

| Type | When to Use | Format |
|------|------------|--------|
| **NOTE** | Additional context that's helpful but not critical | `> **NOTE**: ...` |
| **WARNING** | Something that could cause errors if missed | `> **WARNING**: ...` |
| **TIP** | Best practice or shortcut | `> **TIP**: ...` |
| **SECURITY** | Credential handling, key exposure, auth concerns | `> **SECURITY**: ...` |

### Rules for Callouts

- Place immediately after the relevant instruction, not before
- Keep to 1-2 sentences max
- Never put critical steps inside a callout — if it's required, it belongs in the main flow
- Don't stack callouts back-to-back

## Progressive Disclosure

Structure documentation in layers:

```
Quickstart (10 min)
  → "Want more? See the full Integration Guide"

Integration Guide (1 hr)
  → "For all parameters and options, see the API Reference"

API Reference (complete)
  → "For a walkthrough, start with the Quickstart"
```

Each layer should:
1. Be complete at its level (no "you need to read X first" dependencies)
2. Link forward to deeper content
3. Link backward to simpler content
4. Serve a different need (try → build → reference)

## Guide Opening

Always start with an outcome statement:

**Good:**
```
By the end of this guide, you'll have a working integration that accepts
payments and sends confirmation emails to customers.
```

**Bad:**
```
This guide explains how to use the payments API.
```

Include:
- What the developer will accomplish (specific, measurable)
- Estimated time to complete
- Difficulty level (Beginner / Intermediate / Advanced)

## Testing Section

Every guide ends with a testing section before "Next Steps":

1. List 3-5 test scenarios in a table (scenario, input, expected result)
2. Include both success and failure cases
3. Point to sandbox/test environment specifically
4. Suggest running the complete example end-to-end

## Next Steps Section

Always end with 3-5 concrete next steps:

- Link to the next logical guide
- Link to the API reference for the resource used
- Link to production readiness / go-live checklist
- Suggest a related feature to explore

Each link should have a 1-sentence description of why the developer would want it.

## Writing Style for Guides

- **Second person**: "You" not "the developer" or "one"
- **Active voice**: "Create a payment" not "A payment is created"
- **Present tense**: "This returns a payment object" not "This will return..."
- **Short paragraphs**: 2-3 sentences max between code blocks
- **No jargon without definition**: If you use a term, define it on first use
- **Contractions are fine**: "You'll", "don't", "can't" — keeps it conversational

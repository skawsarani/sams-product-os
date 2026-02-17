---
name: write-ux-copy
description: Creates and reviews user-facing copy for software interfaces including buttons, labels, error messages, tooltips, notifications, onboarding flows, and empty states. Invoked when asked to write, review, or refine UI copy in English. For translation, use translate-i18n skill instead.
---

# UX Copywriting Expert

Create effective, user-friendly copy for software interfaces that guides users to success.

## Quick Start

**Common triggers:**
- "Create UI copy for [feature]"
- "Write error messages for [scenario]"
- "Review this copy for clarity and tone"
- "Create microcopy for [UI element]"
- "Write onboarding copy for [feature]"
- "Create notification copy for [event]"
- "Write empty state copy for [screen]"

**NOT for:**
- Translation (use i18n-translator skill instead)
- Localization (use i18n-translator skill instead)
- Bilingual content creation (use i18n-translator skill instead)

## Core Workflows

### 1. Create UI Copy for Feature

**When to use:** Generating complete UI copy set for new features or flows

**Process:**
1. **Understand the feature**
   - Review feature spec or brief if available
   - Identify all UI elements needing copy
   - Understand user flows and interactions
   - Note technical constraints (character limits, etc.)

2. **Generate copy elements**
   - Button labels (primary, secondary, destructive actions)
   - Form labels and placeholders
   - Error messages and validation text
   - Success messages and confirmations
   - Tooltips and help text
   - Page titles and headings
   - Navigation labels
   - Empty states
   - Loading states

3. **Organize by context**
   - Group by user flow or screen
   - Include context notes for developers
   - Provide character length limits if needed
   - Note dynamic content placeholders

**Output format:**

Organize as table or grouped list:

```markdown
## Login Screen

| Element | Copy | Notes |
|---------|------|-------|
| Heading | Sign in to your account | |
| Email field label | Email address | |
| Email placeholder | you@example.com | Show example format |
| Password field label | Password | |
| Primary button | Sign in | Action-oriented |
| Secondary link | Create account | |
| Forgot password link | Forgot password? | |
| Error (invalid email) | Please enter a valid email address | Specific and helpful |
| Error (wrong credentials) | Email or password is incorrect | Don't specify which for security |
| Success message | Welcome back! | Friendly confirmation |
```

For detailed patterns by copy type (errors, microcopy, onboarding, notifications, buttons/CTAs), see `references/copy-patterns.md`.

### 2. Review and Refine Copy

**When to use:** Before finalizing any user-facing copy

**Process:**
1. **Assess clarity**
   - Is the message clear and unambiguous?
   - Will users understand the action/information?
   - Are technical terms explained or avoided?
   - Is language appropriate for audience?

2. **Evaluate tone**
   - Does it match product voice?
   - Is it friendly/professional/technical as needed?
   - Is it consistent with other product copy?
   - Does it sound human, not robotic?

3. **Check UX best practices**
   - Is it concise enough for UI constraints?
   - Does it guide users to right action?
   - Are error messages helpful, not just descriptive?
   - Does it reduce cognitive load?

4. **Suggest improvements**
   - Provide revised copy with rationale
   - Offer alternatives if applicable
   - Flag concerns or questions

**Review against checklist** (from `references/ux-copy-best-practices.md`):
- [ ] Clear: Meaning immediately obvious
- [ ] Concise: No unnecessary words
- [ ] Helpful: Guides users to success
- [ ] Consistent: Matches terminology elsewhere
- [ ] Action-oriented: Uses active verbs
- [ ] Human: Sounds natural
- [ ] Accessible: Screen reader friendly
- [ ] On-brand: Matches product voice

**Output format:**

```markdown
## Original Copy Review

**Original:** "Error: Invalid input detected"

**Issues:**
- Too technical ("invalid input detected")
- Doesn't explain what's wrong
- Doesn't provide solution
- Sounds robotic

**Suggested revision:** "Please enter a valid email address"

**Rationale:**
- Specific about what field has the issue
- Clear about the requirement
- More human tone
- Action-oriented ("Please enter")

**Alternative:** "That doesn't look like an email address. Please check and try again."
- Even more human and friendly
- Explains the problem
- Provides gentle guidance
```

## Validation

Before delivering copy, run through the Quality Checklist below. For each failed item, revise the copy and re-check. Present the final copy only after all applicable checks pass.

## Quality Checklist

Before delivering any UX copy:

**Clarity:**
- [ ] Message is immediately clear
- [ ] No jargon or technical terms (unless necessary)
- [ ] Users will understand what to do
- [ ] Meaning is unambiguous

**Conciseness:**
- [ ] Every word earns its place
- [ ] No filler words ("just", "simply", "please" unless needed)
- [ ] Fits UI constraints
- [ ] Gets to the point quickly

**Helpfulness:**
- [ ] Guides users to success
- [ ] Provides context when needed
- [ ] Errors suggest solutions
- [ ] Reduces friction and anxiety

**Consistency:**
- [ ] Same terms used throughout
- [ ] Matches existing product copy
- [ ] Tone aligns with brand
- [ ] Follows established patterns

**Action-oriented:**
- [ ] Buttons use verbs
- [ ] Clear what will happen
- [ ] Specific, not vague
- [ ] Empowers user action

**Human:**
- [ ] Sounds natural, not robotic
- [ ] Shows empathy where appropriate
- [ ] Avoids corporate speak
- [ ] Conversational (when appropriate)

**Accessible:**
- [ ] Works for screen readers
- [ ] Plain language
- [ ] Descriptive link text (not "click here")
- [ ] No reliance on color alone to convey meaning

## Reference Files

| File | Contains |
|------|----------|
| `references/ux-copy-best-practices.md` | Core principles, copy type patterns, length guidelines, accessibility, common mistakes, review checklist |
| `references/copy-patterns.md` | Detailed patterns with examples: error messages, microcopy, onboarding, notifications, buttons/CTAs |
| `references/voice-tone-guidelines.md` | Product voice types, contextual tone (success, errors, warnings, info) |

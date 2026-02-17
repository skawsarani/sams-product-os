# UX Copy Best Practices

Guidelines and patterns for writing effective user interface copy.

## Table of Contents
- [Core Principles](#core-principles)
- [Copy Types & Patterns](#copy-types--patterns)
- [Voice & Tone](#voice--tone)
- [Length Guidelines](#length-guidelines)
- [Accessibility Considerations](#accessibility-considerations)
- [Localization Considerations](#localization-considerations)
- [Testing & Iteration](#testing--iteration)
- [Common Mistakes to Avoid](#common-mistakes-to-avoid)
- [Copy Review Checklist](#copy-review-checklist)

## Core Principles

### 1. Clarity Above All
- Every word should earn its place
- Users should understand immediately
- Avoid jargon and technical terms unless necessary
- Use plain language

### 2. Be Concise
- Shorter is better, but not at the expense of clarity
- Remove filler words: "please", "in order to", "just"
- Get to the point quickly
- Respect users' time and attention

### 3. Be Helpful
- Guide users to success
- Anticipate questions and answer them preemptively
- Provide context when needed
- Offer solutions, not just problems

### 4. Be Consistent
- Use the same terms throughout the product
- Maintain consistent tone across all touchpoints
- Follow established patterns
- Create and maintain a terminology glossary

### 5. Be Action-Oriented
- Use verbs for buttons and CTAs
- Tell users what will happen
- Make actions clear and specific
- "Save changes" not just "Save"

### 6. Be Human
- Write like you're talking to a person
- Use conversational tone (when appropriate)
- Show empathy, especially in error states
- Avoid robot-speak

## Copy Types & Patterns

### Button Labels

**Primary actions** (high emphasis):
- ✅ "Create account"
- ✅ "Save changes"
- ✅ "Continue to checkout"
- ❌ "OK"
- ❌ "Submit"

**Secondary actions** (lower emphasis):
- ✅ "Cancel"
- ✅ "Go back"
- ✅ "Skip for now"

**Destructive actions** (dangerous):
- ✅ "Delete account"
- ✅ "Remove file"
- ✅ "Discard changes"
- Always require confirmation

**Guidelines:**
- Use verb + object: "Save changes" not "Save"
- Be specific: "Create project" not "Create"
- Keep under 3-4 words when possible
- Match action to user's intent

### Form Labels

**Field labels:**
- ✅ Clear and concise: "Email address"
- ✅ No punctuation at end
- ✅ Sentence case: "First name" not "First Name"

**Placeholders:**
- ✅ Use for examples: "e.g., john@example.com"
- ✅ Use for format hints: "MM/DD/YYYY"
- ❌ Don't use instead of labels
- ❌ Don't use for instructions

**Help text:**
- ✅ Provide when needed: "We'll never share your email"
- ✅ Keep brief and specific
- ✅ Place near relevant field

**Required vs. optional:**
- Mark optional fields with "(optional)"
- Don't mark required fields if most fields are required
- Be consistent across the form

### Error Messages

**Anatomy of a good error message:**
1. What went wrong (clearly and specifically)
2. Why it happened (if helpful)
3. How to fix it (actionable next steps)

**Examples:**

❌ **Bad:** "Invalid input"
✅ **Good:** "Email address must include '@' symbol"

❌ **Bad:** "Error 404"
✅ **Good:** "Page not found. Try searching or return to the home page."

❌ **Bad:** "Username taken"
✅ **Good:** "This username is already in use. Try adding numbers or a different variation."

**Error types:**

**Validation errors:**
- Be specific about the requirement
- "Password must be at least 8 characters"
- "Please enter a valid phone number"

**System errors:**
- Be honest but not technical
- "We're having trouble connecting. Check your internet and try again."
- "Something went wrong on our end. We're working to fix it."

**Permission errors:**
- Explain clearly what's restricted
- "You don't have permission to delete this file. Contact the owner to request access."

**Business logic errors:**
- Explain the rule clearly
- "You can't delete your account while you have an active subscription. Cancel your subscription first."

**Tone:**
- Don't blame the user
- ❌ "You entered an invalid email"
- ✅ "Please enter a valid email address"
- Be empathetic, especially for frustrating errors
- Offer solutions when possible

### Success Messages

**Confirmation messages:**
- ✅ "Changes saved"
- ✅ "File uploaded successfully"
- ✅ "Email sent"

**Keep them:**
- Brief (2-4 words when possible)
- Specific (what succeeded)
- Positive
- Dismissible or auto-hiding

**Examples:**
- ✅ "✓ Profile updated"
- ✅ "✓ Invitation sent to sarah@example.com"
- ❌ "Success"
- ❌ "Your request has been successfully processed"

### Empty States

**Purpose:** Turn nothing into opportunity

**Good empty states include:**
1. Why it's empty
2. What users can do
3. Clear call to action

**Examples:**

❌ **Bad:** "No files"
✅ **Good:**
```
No files yet
Upload your first file to get started.
[Upload file]
```

❌ **Bad:** "0 results"
✅ **Good:**
```
No results for "xyz"
Try different keywords or check your spelling.
```

**Patterns:**
- **No items yet:** "Your inbox is empty. New messages will appear here."
- **No results:** "No results found. Try different search terms."
- **No data:** "No data for this time period. Select a different date range."
- **Feature introduction:** "Create your first project to organize your work."

### Loading States

**Purpose:** Set expectations and reduce anxiety

**Guidelines:**
- Tell users what's loading
- ✅ "Loading your projects..."
- ✅ "Sending email..."
- ❌ "Loading..."

**For long waits:**
- Show progress when possible: "Uploading... 45%"
- Give time estimates: "This might take a few minutes"
- Explain what's happening: "Processing your payment..."

**Skeleton screens:**
- Better than spinners for content loading
- Show structure of what's coming
- Reduce perceived wait time

### Tooltips & Help Text

**Tooltips:**
- Use for definitions or extra context
- Keep under 10 words when possible
- Avoid for critical information
- Example: "Workspace" → "A shared space for your team"

**Inline help:**
- Place near relevant controls
- Use for clarification or reassurance
- Example: "We'll never share your email address"

**Help text patterns:**
- **Format help:** "Must be at least 8 characters"
- **Reassurance:** "You can change this later"
- **Privacy:** "Only visible to you"
- **Clarification:** "This will cancel your subscription immediately"

### Microcopy

**Definition:** Small bits of copy that guide users

**Examples:**
- Link text: "Learn more" vs "Click here"
- Toggle labels: "Enable notifications"
- Character counters: "125/280 characters"
- Time stamps: "2 hours ago" vs "14:32"

**Best practices:**
- Be specific with link text
- ❌ "Click here"
- ✅ "View pricing details"
- Use present tense for current state
- Use future tense for actions
- Keep it scannable

### Onboarding Copy

**Purpose:** Welcome and educate users

**Welcome message:**
- Be warm and welcoming
- ✅ "Welcome to [Product]! Let's get you set up."
- ❌ "Welcome. Complete these steps."

**Tutorial steps:**
- Keep each step focused
- Use 3-5 steps maximum
- Be encouraging
- Show progress: "Step 2 of 4"

**Patterns:**
1. **Welcome:** "Welcome! Let's create your first project."
2. **Step 1:** "Add your team members to collaborate."
3. **Step 2:** "Upload your files to get started."
4. **Completion:** "You're all set! Start creating."

**Tone:**
- Encouraging, not demanding
- ✅ "Let's set up your profile"
- ❌ "You must complete your profile"
- Celebrate completion
- ✅ "Great! You're ready to go."

### Notification Copy

**Push notifications:**
- Ultra-concise (under 50 characters)
- Specific about what happened
- Include actionable verb
- ✅ "Sarah commented on your post"
- ❌ "You have a new notification"

**Email notifications:**
- **Subject line:** Clear and specific (30-50 chars)
- ✅ "Your order has shipped"
- ✅ "Sarah invited you to join Workspace"
- ❌ "Update"
- **Body:** Provide context and action

**In-app notifications:**
- **Success:** "✓ File uploaded"
- **Warning:** "⚠ Connection unstable"
- **Error:** "✗ Upload failed. Try again."
- **Info:** "ℹ New features available"

**Notification patterns:**

| Type | Pattern | Example |
|------|---------|---------|
| **Activity** | [Who] [did what] | "John shared a file" |
| **Status** | [What] [status] | "Export complete" |
| **Request** | [Who] [requests] | "Sarah invited you" |
| **Reminder** | [Action] [context] | "Meeting in 10 minutes" |
| **Achievement** | [Milestone] | "You reached 100 followers!" |

## Voice & Tone

### Voice vs. Tone

**Voice** (consistent across product):
- Your product's personality
- How you always sound
- Examples: Professional, Friendly, Playful, Authoritative

**Tone** (varies by context):
- Adjusts to situation
- How you sound in specific moments
- Success = cheerful, Error = empathetic, Warning = serious

### Tone by Context

**Celebrations (success states):**
- ✅ "Nice work! Changes saved."
- ✅ "🎉 You're all set!"

**Problems (error states):**
- ✅ "We couldn't save your changes. Please try again."
- ✅ "Something went wrong. Our team has been notified."

**Warnings (cautionary states):**
- ✅ "This action cannot be undone."
- ✅ "You have unsaved changes."

**Information (neutral states):**
- ✅ "Your plan renews on January 15."
- ✅ "Last saved 2 minutes ago."

### Formality Levels

**Formal** (professional tools, B2B, finance):
- Use "you" not "your"
- Avoid contractions
- Be precise and clear
- Example: "Your account has been created."

**Casual** (consumer apps, social, creative):
- Use contractions
- More conversational
- Warmer tone
- Example: "You're all set!"

**Choose based on:**
- Target audience
- Product category
- Company brand
- User expectations

## Length Guidelines

**Buttons:** 1-4 words
- "Save" or "Save changes"

**Headings:** 2-6 words
- "Create your account"

**Error messages:** 10-20 words
- "Email address must include '@' symbol"

**Empty states:** 20-40 words
- Title + description + CTA

**Tooltips:** 5-10 words
- "Your private workspace for saving ideas"

**Notifications:** 5-15 words
- "Sarah invited you to Project Alpha"

**Form help text:** 5-15 words
- "We'll send you a confirmation email"

## Accessibility Considerations

### Screen readers
- Use descriptive link text (not "click here")
- Provide alt text for icons used as buttons
- Make button labels self-explanatory
- Include ARIA labels when needed

### Plain language
- Use common words
- Short sentences (< 20 words)
- Active voice
- Avoid idioms that don't translate

### Readability
- Break up long text with headings
- Use lists for multiple items
- Keep paragraphs short (2-3 sentences)
- Use simple sentence structure

## Localization Considerations

**Write for translation:**
- Avoid idioms and cultural references
- Don't embed text in images
- Leave room for expansion (30-40% longer in some languages)
- Avoid puns and wordplay
- Use complete sentences (not fragments)

**Variables and placeholders:**
- Consider word order variations
- ✅ "Welcome, {name}!"
- ❌ "{name}, welcome!" (might not work in all languages)

**Pluralization:**
- Build proper plural support
- Not all languages use singular/plural like English
- Example: "1 file" / "2 files" needs different rules in different languages

## Testing & Iteration

**Test copy by:**
1. Reading aloud (does it sound natural?)
2. Testing with users (do they understand?)
3. Checking length (does it fit?)
4. Reviewing consistency (matches style guide?)
5. Accessibility check (screen reader friendly?)

**Iterate based on:**
- User feedback
- Support tickets (common confusion points)
- Analytics (where do users drop off?)
- A/B testing results

## Common Mistakes to Avoid

❌ **Using jargon**
- Bad: "Authenticate your credentials"
- Good: "Sign in"

❌ **Being vague**
- Bad: "Error occurred"
- Good: "Email address is required"

❌ **Blaming the user**
- Bad: "You entered invalid data"
- Good: "Please check your email format"

❌ **Over-explaining**
- Bad: "Click on the button labeled 'Save' below to save your changes to the database"
- Good: "Save changes"

❌ **Inconsistent terminology**
- Don't switch between "remove," "delete," "trash" for same action

❌ **Missing context**
- Bad: "Done" (done with what?)
- Good: "Profile updated"

❌ **Robot language**
- Bad: "Your request has been processed successfully"
- Good: "All set!"

## Copy Review Checklist

Before finalizing any UX copy:

- [ ] Clear: Is the meaning immediately obvious?
- [ ] Concise: Can any words be removed?
- [ ] Helpful: Does it guide users to success?
- [ ] Consistent: Matches terminology elsewhere?
- [ ] Action-oriented: Uses active verbs?
- [ ] Human: Sounds natural and conversational?
- [ ] Accessible: Works for screen readers?
- [ ] On-brand: Matches product voice and tone?
- [ ] Tested: Validated with users or team?
- [ ] Translatable: Works for localization?

# Copy Patterns Reference

Detailed patterns and examples for common UX copy types.

## Table of Contents
- [Error Messages](#error-messages)
- [Microcopy](#microcopy)
- [Onboarding Copy](#onboarding-copy)
- [Notification Copy](#notification-copy)
- [Button & CTA Copy](#button--cta-copy)

## Error Messages

### Error Message Anatomy
1. **What went wrong** (clear and specific)
2. **Why it happened** (if helpful)
3. **How to fix it** (actionable)

### Error Types and Patterns

**Validation errors:**
- "Password must be at least 8 characters"
- "Email address must include '@' symbol"
- "Please select a date in the future"
- Bad: "Invalid input"

**System errors:**
- "We're having trouble connecting. Check your internet and try again."
- "Something went wrong on our end. We're working to fix it."
- "This page isn't loading. Please refresh or try again later."
- Bad: "Error 500"

**Permission errors:**
- "You don't have permission to delete this file. Contact the owner to request access."
- "This action requires admin access. Ask your team admin for permission."
- Bad: "Access denied", "403 Forbidden"

**Business logic errors:**
- "You can't delete your account while you have an active subscription. Cancel your subscription first."
- "You've reached the maximum of 5 projects on the free plan. Upgrade to create more."
- Bad: "Cannot delete", "Limit reached"

**Network/connectivity errors:**
- "No internet connection. Check your network and try again."
- "Request timed out. Please try again."
- Bad: "Network error"

### Error Tone Guidelines
- **Don't blame the user**
  - Bad: "You entered invalid data"
  - Good: "Please check your email format"
- **Be empathetic for frustrating errors**
  - "We're sorry, but something went wrong. Our team has been notified."
- **Offer solutions when possible**
  - "...Check your internet and try again"
  - "...Contact support@example.com if this keeps happening"
- **Keep consistent format across all errors**

---

## Microcopy

### Tooltips
- Keep under 10 words
- "Your private workspace for saving ideas"
- "Visible to team members only"
- Use for definitions or extra context
- Don't use for critical information (might be missed)

### Inline Help
- "We'll never share your email address"
- "You can change this later"
- "Changes save automatically"
- Provide reassurance or clarification
- Reduce anxiety about actions

### Empty States
Structure: Why empty + What to do + CTA

```
No files yet
Upload your first file to get started.
[Upload file]

---

No team members
Invite people to collaborate on your projects.
[Invite team]

---

No notifications
You're all caught up! We'll notify you when there's something new.
```

### Loading States
- "Loading your projects..."
- "Uploading... 45%"
- "Processing payment..."
- "Saving changes..."
- Bad: "Loading..." (too vague)
- Tell users what's loading, not just "Loading..."

### Placeholders
- "Search by name or email..."
- "Enter your company name"
- "e.g., Annual Marketing Report"
- Show examples or format hints
- Don't repeat the label

### Character Counters
- "125/280 characters"
- "15 characters remaining"
- "280 characters max"

### Timestamps
- "2 hours ago"
- "Last saved at 2:30 PM"
- "Updated yesterday"
- "Edited just now"

---

## Onboarding Copy

### Structure
1. Welcome message (warm, inviting)
2. Step-by-step guidance (3-5 steps max)
3. Progress indicators (show advancement)
4. Completion celebration (encourage and celebrate)

### Tone
- Warm and welcoming
- Encouraging, not demanding
- "Welcome! Let's get you set up."
- "Great! You're ready to go."
- "Nice work! One more step."
- Bad: "You must complete these steps", "Required: Setup"

### Pattern
```
Welcome to [Product]!
Let's create your first project.

Step 1 of 3: Add team members
Invite your team to collaborate.
[Skip] [Invite team]

Step 2 of 3: Upload files
Drag and drop your files here.
[Skip] [Upload files]

Step 3 of 3: Set your preferences
Customize your workspace.
[Skip] [Continue]

You're all set! Start creating.
[Go to dashboard]
```

### Best Practices
- Keep it brief (users want to start using the product)
- Make it skippable (don't force it)
- Show progress (users know how much is left)
- Focus on value (why this step matters)
- Allow do-it-later option for non-critical setup

### Feature Announcements
```
New: Dark mode
Toggle between light and dark themes in Settings > Appearance.
[Try it now] [Dismiss]
```

---

## Notification Copy

### Push Notifications (ultra-concise, <50 chars)
- "Sarah commented on your post"
- "Your order has shipped"
- "New message from Alex"
- Bad: "You have a new notification", "Update available"

### Email Notifications
- **Subject:** Clear and specific (30-50 chars)
  - "Sarah invited you to join Workspace"
  - "Your export is ready"
  - Bad: "Notification"
- **Body:** Context + action
  - Short explanation
  - Clear call-to-action
  - Link to relevant page

### In-App Notifications
- **Success:** "File uploaded"
- **Warning:** "Connection unstable"
- **Error:** "Upload failed. Try again."
- **Info:** "New features available"

### Notification Patterns

| Type | Pattern | Example |
|------|---------|---------|
| Activity | [Who] [did what] | "John shared a file with you" |
| Status | [What] [status] | "Export complete" |
| Request | [Who] [requests what] | "Sarah invited you to join Team" |
| Reminder | [Action] [context] | "Meeting in 10 minutes" |
| Achievement | [What] [accomplished] | "You completed 10 tasks this week!" |

### Notification Best Practices
- **Be specific:** "Sarah commented" not "New activity"
- **Be timely:** Include time context if relevant
- **Be actionable:** Make it clear what to do next
- **Be scannable:** Users glance, not read
- **Be respectful:** Don't over-notify or use clickbait

---

## Button & CTA Copy

### Primary Actions (high emphasis)
- "Create account"
- "Save changes"
- "Continue to checkout"
- "Start free trial"
- Be specific about what happens

### Secondary Actions (medium emphasis)
- "Cancel"
- "Go back"
- "Skip for now"
- "Learn more"

### Destructive Actions (requires caution)
- "Delete account"
- "Remove file"
- "Discard changes"
- Be explicit about consequences

### Best Practices
- **Use verbs:** "Create", "Save", "Send", not nouns
- **Be specific:** "Save changes" not just "Save"
- **Keep short:** 1-3 words ideal, max 5 words
- **Front-load keywords:** "Create account" not "Account creation"
- **Avoid generic:** "Submit", "OK" (what does it do?)
- **Match voice:** Formal products use "Sign in", casual use "Log in"

### Examples

| Context | Bad | Good | Why |
|---------|-----|------|-----|
| Signup form | Submit | Create account | Specific action |
| File upload | OK | Upload | Clear intent |
| Delete confirm | Yes | Delete | Explicit consequence |
| Save form | Save | Save changes | Specific what's being saved |
| Cancel modal | No | Cancel | Clear what happens |
| Learn about feature | Click here | Learn more | Descriptive, not generic |

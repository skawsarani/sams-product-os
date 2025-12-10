## GitHub & Git Expert

Expert workflow for managing everything git-related using git or GitHub CLI.

---

### Create PR Description

```
Create a PR description for [feature/changes]
```

**What it does**:
- Summarizes changes made
- Explains why the changes were made
- Lists files modified
- Includes testing notes if applicable
- Suggests reviewers
- Adds relevant context

**When to use**: Before opening a PR on GitHub

---

### Prepare Changes for PR

```
Help me prepare a PR for [feature/branch]
```

**What it does**:
- Reviews changed files
- Suggests commit message
- Identifies what should be included
- Flags files that shouldn't be committed
- Ensures documentation is updated
- Checks for consistency

**When to use**: After making changes, before pushing

---

### Review PR Before Submit

```
Review this PR for [feature] - what should I check?
```

**What it does**:
- Creates PR checklist
- Verifies documentation updates
- Checks for breaking changes
- Ensures tests are included
- Validates commit messages
- Suggests improvements

**When to use**: Final review before submitting PR

---

### Write PR Summary

```
Write a concise PR summary for [changes]
```

**What it does**:
- One-line summary
- Key changes bulleted
- Impact statement
- Testing notes
- Deployment considerations

**When to use**: Quick PR creation

---

### Create Commit Message

```
Create a commit message for [changes]
```

**What it does**:
- Follows conventional commit format
- Summarizes changes concisely
- Includes scope if applicable
- Adds body with details if needed

**When to use**: Before committing changes

---

### Commit and Push Changes

```
Commit all changes and push
```

**What it does**:
- Stages all changes (including deletions and new files) with `git add -A`
- Creates a commit with an appropriate message summarizing the changes
- Pushes to the remote repository
- Handles renames, deletions, and new files correctly
- Provides summary of what was committed

**When to use**: When user wants to commit all current changes and push to remote

**Note**: If user asks to "commit and push" or "commit all changes and push", this workflow should:
1. Stage all changes: `git add -A`
2. Review what will be committed (or infer from context)
3. Create a descriptive commit message
4. Commit the changes
5. Push to remote

---

### Manage Branches

```
[Create/Delete/Merge] branch [name] for [purpose]
```

**What it does**:
- Creates feature branches
- Deletes merged branches
- Merges branches
- Lists branches
- Shows branch status

**When to use**: Branch management

---

### Review Git Status

```
Review my git status and suggest next steps
```

**What it does**:
- Shows current git status
- Identifies uncommitted changes
- Suggests what to commit
- Flags files that should be ignored
- Recommends next git actions

**When to use**: Check repository state

---

### Manage GitHub Issues

```
[Create/Update/Close] GitHub issue for [description]
```

**What it does**:
- Creates issues with proper labels
- Updates issue status
- Closes issues with resolution
- Links issues to PRs
- Manages issue lifecycle

**When to use**: Issue tracking and management

---

### Git Workflow Operations

```
Help me [rebase/merge/squash] [branch/commits]
```

**What it does**:
- Performs git operations safely
- Explains what will happen
- Suggests best practices
- Handles conflicts if needed

**When to use**: Advanced git operations

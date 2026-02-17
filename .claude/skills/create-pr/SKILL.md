---
name: create-pr
description: Creates a pull request for the current branch with comprehensive summary, test plan, and auto-push. Invoked when asked to create a PR, open a pull request, or submit changes for review.
disable-model-invocation: true
allowed-tools: Bash(git *), Bash(gh pr create:*)
argument-hint: [optional PR title]
---

## Context

- Current branch: !`git branch --show-current`
- Git status: !`git status --short`
- Staged diff: !`git diff --cached --stat`
- Recent commits: !`git log --oneline -5`
- Commits in this branch: !`git log main...HEAD --oneline`
- Full diff from main: !`git diff main...HEAD`

---

## Create Pull Request

Create a pull request for the current branch.

$ARGUMENTS

**Steps:**

1. **Analyze all changes**: Review ALL commits and the full diff (not just the latest commit) to understand the complete scope of changes

2. **Draft PR summary**: Create a comprehensive summary with:
   - Title: Clear, descriptive (use $ARGUMENTS if provided, otherwise generate from changes)
   - Summary: 1-3 bullet points covering what changed and why
   - Test plan: Bulleted checklist of how to test/verify the changes

3. **Push if needed**: If the branch needs to be pushed or updated, push to remote with `-u origin <branch-name>`

4. **Create PR**: Use `gh pr create` with:
   ```
   gh pr create --title "PR title here" --body "$(cat <<'EOF'
   ## Summary
   - Bullet point 1
   - Bullet point 2

   ## Test plan
   - [ ] Test item 1
   - [ ] Test item 2

   🤖 Generated with [Claude Code](https://claude.com/claude-code)
   EOF
   )"
   ```

5. **Return PR URL**: Show the created PR URL so the user can view it

**Important:**
- Analyze ALL commits in the branch, not just the most recent one
- Keep the summary concise but comprehensive
- Use HEREDOC format for the PR body to ensure proper formatting
- Don't use --no-verify or skip any hooks

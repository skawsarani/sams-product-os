---
name: committing-code
description: Handles git workflow operations including conventional commits with emoji, pushing branches, and creating pull requests. Invoked via /commit, /push, or /pr. Also triggered by "commit my changes", "push to remote", "create a PR".
disable-model-invocation: true
allowed-tools: Bash(git *), Bash(gh pr create:*)
argument-hint: [optional commit message, PR title, or flags like --force]
---

## Context

- Current branch: !`git branch --show-current`
- Git status: !`git status --short`
- Staged diff: !`git diff --cached --stat`
- Recent commits: !`git log --oneline -5`

---

## /commit — Create Conventional Commit

Create well-formatted commits using conventional commit messages with emoji.

**IMPORTANT:** If user provided arguments: $ARGUMENTS
- **If it's a commit message, USE IT DIRECTLY** - only add emoji/type prefix if missing
- If `--no-verify`, skip pre-commit verification
- **DO NOT auto-generate a different message when user provides one**

### Workflow

#### 1. Check User-Provided Message

**If user provided a message in $ARGUMENTS:**
1. Check if it already has emoji + type prefix (e.g., "🔧 chore: message")
2. If yes, use it exactly as-is
3. If no, analyze changes to determine appropriate emoji + type, then prepend to their message
4. Skip to step 5 (create commit)

**If no message provided, follow steps 2-4 below to auto-generate.**

#### 2. Check Staged Files
- Run `git status` to check staged files
- If nothing staged, stage all modified/new files with `git add -A`

#### 3. Analyze Changes
- Run `git diff --cached` to understand what's being committed
- Detect if changes span multiple concerns (see splitting guidelines below)

#### 4. Smart Commit Splitting
If changes touch multiple unrelated concerns, suggest splitting into separate commits:

**Split when:**
- Different types of changes (feature + docs + config)
- Unrelated file groups (src/ changes + test/ changes + docs/)
- Multiple logical units that could be reverted independently

#### 5. Create Commit Message (if auto-generating)

**Format:** `<emoji> <type>: <description>`

**Commit Types & Emoji:**

| Type | Emoji | Use for |
|------|-------|---------|
| feat | ✨ | New features |
| fix | 🐛 | Bug fixes |
| docs | 📝 | Documentation |
| style | 💄 | Formatting, UI styling |
| refactor | ♻️ | Code restructuring |
| perf | ⚡️ | Performance improvements |
| test | ✅ | Tests |
| chore | 🔧 | Config, tooling, maintenance |
| ci | 👷 | CI/CD changes |
| revert | 🗑️ | Reverting changes |

**Additional emoji modifiers:**

| Emoji | Meaning |
|-------|---------|
| 💥 | Breaking change |
| 🔒️ | Security fix |
| 🚑️ | Critical hotfix |
| 🌐 | Internationalization |
| 📱 | Mobile/responsive |
| 🏗️ | Architectural change |
| 📦️ | Dependencies |

**Message guidelines:**
- Present tense, imperative mood ("add" not "added")
- First line under 72 characters
- Focus on WHY, not just WHAT
- Be specific: "fix auth token expiry" > "fix bug"

**Important:**
- Do NOT push to remote unless explicitly asked
- If splitting commits, stage and commit each group separately
- Match existing commit style in the repository when possible
- Use `git commit -m "$(cat <<'EOF'` format for multi-line messages

---

## /push — Push to Remote

Push the current branch to the remote repository.

$ARGUMENTS

**Steps:**
1. Check current branch and status
2. If the branch doesn't have an upstream, set it with `-u origin <branch-name>`
3. If the user provided flags (like --force), include them: $ARGUMENTS
4. NEVER use `--force` on main/master branches unless explicitly confirmed by user
5. Show the push output to confirm success

---

## /pr — Create Pull Request

Create a pull request for the current branch.

$ARGUMENTS

**Context:**
- Commits in this branch: !`git log main...HEAD --oneline`
- Full diff from main: !`git diff main...HEAD`

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

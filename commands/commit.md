---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git diff:*), Bash(git branch:*), Bash(git log:*)
argument-hint: [optional commit message or --no-verify to skip checks]
description: Create a git commit with conventional commit format and emoji
---

## Context

- Current branch: !`git branch --show-current`
- Git status: !`git status --short`
- Staged diff: !`git diff --cached --stat`
- Recent commits: !`git log --oneline -5`

## Your Task

Create well-formatted commits using conventional commit messages with emoji.

If user provided arguments: $ARGUMENTS
- If it's a message, use it as the commit message
- If `--no-verify`, skip pre-commit verification

## Workflow

### 1. Check Staged Files
- Run `git status` to check staged files
- If nothing staged, stage all modified/new files with `git add -A`

### 2. Analyze Changes
- Run `git diff --cached` to understand what's being committed
- Detect if changes span multiple concerns (see splitting guidelines below)

### 3. Smart Commit Splitting
If changes touch multiple unrelated concerns, suggest splitting into separate commits:

**Split when:**
- Different types of changes (feature + docs + config)
- Unrelated file groups (src/ changes + test/ changes + docs/)
- Multiple logical units that could be reverted independently

**Example split:**
```
Instead of one large commit, suggest:
1. ✨ feat: add user authentication flow
2. ✅ test: add auth unit tests
3. 📝 docs: update API documentation
```

### 4. Create Commit Message

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

## Examples

**Good commits:**
```
✨ feat: add daily planning command with goal alignment
🐛 fix: resolve task duplication in backlog processing
📝 docs: update AGENTS.md with new command structure
♻️ refactor: consolidate workflows into slash commands
🔧 chore: update config with new category keywords
```

**Multi-commit example:**
```
When committing a large feature:
1. ✨ feat: add weekly review command structure
2. 📝 docs: add weekly review to AGENTS.md
3. ✅ test: add weekly review workflow tests
```

## Important

- Do NOT push to remote unless explicitly asked
- If splitting commits, stage and commit each group separately
- Match existing commit style in the repository when possible
- Use `git commit -m "$(cat <<'EOF'` format for multi-line messages

---
name: push
description: Pushes current branch to remote repository with upstream tracking and force-push safety checks. Invoked when asked to push code, push to remote, or update remote branch.
disable-model-invocation: true
allowed-tools: Bash(git *)
argument-hint: [optional flags like --force]
---

## Context

- Current branch: !`git branch --show-current`
- Git status: !`git status --short`
- Staged diff: !`git diff --cached --stat`
- Recent commits: !`git log --oneline -5`

---

## Push to Remote

Push the current branch to the remote repository.

$ARGUMENTS

**Steps:**
1. Check current branch and status
2. If the branch doesn't have an upstream, set it with `-u origin <branch-name>`
3. If the user provided flags (like --force), include them: $ARGUMENTS
4. NEVER use `--force` on main/master branches unless explicitly confirmed by user
5. Show the push output to confirm success

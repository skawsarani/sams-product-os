---
allowed-tools: Skill, Read, Write, Glob
argument-hint: [skill name or description]
description: Create or update a skill with guided workflow
---

## Context

Skills extend Claude's capabilities with specialized knowledge, workflows, or tool integrations.

The skill-creator skill provides expert guidance for building effective skills.

## Your task

Guide the user through creating a new skill or updating an existing one.

User input: $ARGUMENTS

**Steps:**

1. **Invoke skill-creator**: Use the Skill tool to launch the skill-creator skill

2. **Pass user context**: Include $ARGUMENTS to provide context about what skill they want to create

**Example invocation:**
- `/build-skill user research analyzer` → Create a skill for analyzing user research
- `/build-skill` → Interactive workflow to design a new skill
- `/build-skill update internal-comms` → Update existing internal-comms skill

**Important:**
- The skill-creator will handle the full workflow (asking questions, creating files, etc.)
- Skills are typically stored in `skills/` directory
- Each skill includes SKILL.md, knowledge files, and optional code
- Create the skill NOW. Do not explore the codebase first. Do not write a plan. Start by creating the SKILL.md file, then create any supporting files. If you need context, read only the specific files mentioned. Go.

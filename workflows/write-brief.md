---
allowed-tools: Skill, Read, Write, Glob
argument-hint: [project name]
description: Generate a Project Brief
---

## Context

Generate a project brief using the product-docs skill. This workflow automatically pulls context from your knowledge base.

- Today's date: $TODAY
- User arguments: $ARGUMENTS

## Your Task

1. Invoke the product-docs skill to generate a brief
2. Tell the user: "I'm using the product-docs skill to generate your project brief"
3. Pass the user's arguments as the project name

**Invoke skill:**
```
Skill(skill="product-docs", args="type:brief name:$ARGUMENTS")
```

The skill will:
- Gather context from knowledge base (product-strategy, opportunities, briefs-and-specs, transcripts)
- Select the brief template from `skills/product-docs/assets/brief-template.md`
- Generate a concise 1-2 page overview with goals, scope, and timeline
- Present for review with open questions and next steps

## If No Arguments Provided

Ask the user: "What project would you like to create a brief for?"

Then invoke the skill with their response.

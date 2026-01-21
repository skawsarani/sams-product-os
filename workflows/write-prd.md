---
allowed-tools: Skill, Read, Write, Glob
argument-hint: [feature name]
description: Generate a Product Requirements Document
---

## Context

Generate a comprehensive PRD using the product-docs skill. This workflow automatically pulls context from your knowledge base.

- Today's date: $TODAY
- User arguments: $ARGUMENTS

## Your Task

1. Invoke the product-docs skill to generate a PRD
2. Tell the user: "I'm using the product-docs skill to generate your PRD"
3. Pass the user's arguments as the feature/product name

**Invoke skill:**
```
Skill(skill="product-docs", args="type:prd name:$ARGUMENTS")
```

The skill will:
- Gather context from knowledge base (product-strategy, opportunities, briefs-and-specs, transcripts)
- Select the PRD template from `skills/product-docs/assets/prd-template.md`
- Generate a complete first draft
- Present for review with open questions and next steps

## If No Arguments Provided

Ask the user: "What feature or product would you like to create a PRD for?"

Then invoke the skill with their response.

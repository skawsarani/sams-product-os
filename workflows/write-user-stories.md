---
allowed-tools: Skill, Read, Write, Glob
argument-hint: [feature name]
description: Generate User Stories with acceptance criteria
---

## Context

Generate user stories using the product-docs skill. This workflow automatically pulls context from your knowledge base.

- Today's date: $TODAY
- User arguments: $ARGUMENTS

## Your Task

1. Invoke the product-docs skill to generate user stories
2. Tell the user: "I'm using the product-docs skill to generate your user stories"
3. Pass the user's arguments as the feature name

**Invoke skill:**
```
Skill(skill="product-docs", args="type:user-stories name:$ARGUMENTS")
```

The skill will:
- Gather context from knowledge base (product-strategy, opportunities, briefs-and-specs, transcripts)
- Select the user stories template from `skills/product-docs/assets/user-stories-template.md`
- Generate stories in "As a [user], I want [goal], so that [benefit]" format
- Include acceptance criteria, edge cases, and prioritization
- Present for review with open questions and next steps

## If No Arguments Provided

Ask the user: "What feature would you like to create user stories for?"

Then invoke the skill with their response.

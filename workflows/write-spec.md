---
allowed-tools: Skill, Read, Write, Glob
argument-hint: [feature name]
description: Generate a Product Specification
---

## Context

Generate a product specification using the product-docs skill. This workflow automatically pulls context from your knowledge base.

- Today's date: $TODAY
- User arguments: $ARGUMENTS

## Your Task

1. Invoke the product-docs skill to generate a spec
2. Tell the user: "I'm using the product-docs skill to generate your product spec"
3. Pass the user's arguments as the feature name

**Invoke skill:**
```
Skill(skill="product-docs", args="type:spec name:$ARGUMENTS")
```

The skill will:
- Gather context from knowledge base (product-strategy, opportunities, briefs-and-specs, transcripts)
- Select the spec template from `skills/product-docs/assets/spec-template.md`
- Generate a complete first draft with user stories, requirements, and acceptance criteria
- Present for review with open questions and next steps

## If No Arguments Provided

Ask the user: "What feature would you like to create a product spec for?"

Then invoke the skill with their response.

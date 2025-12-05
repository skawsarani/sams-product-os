# Contributing to PM Co-Pilot

Thank you for your interest in contributing! This document outlines how to contribute to PM Co-Pilot.

---

## Ways to Contribute

### 1. Share Your Templates
If you've created useful document templates that work well for your PM workflow.

### 2. Add Workflow Examples
Share workflows or slash commands that have been valuable in your practice.

### 3. Improve Documentation
- Fix typos or unclear instructions
- Add examples or clarifications
- Translate guides (if applicable)

### 4. Create Tutorials
Share how you use PM Co-Pilot in your workflow.

### 5. Suggest Improvements
Open an issue to discuss:
- New features or workflows
- Better organization
- Missing documentation

---

## Getting Started

### Prerequisites
- Familiarity with Markdown
- Experience using AI coding assistants (Cursor, Claude Code, etc.)
- Product management experience (for PM-specific contributions)

### Setup
1. Fork the repository
2. Clone your fork locally
3. Create a branch for your changes
4. Make your changes
5. Test with your AI assistant
6. Submit a pull request

---

## Contribution Guidelines

### Documentation
- Follow style guidance in [AGENTS.md](AGENTS.md)
- Use clear, concise language
- Include examples where helpful
- Test instructions before submitting

### File Organization
- Put examples in `examples/example_files/`
- Put tutorials in `examples/tutorials/`
- Put workflow docs in `examples/workflows/`
- Put templates in `templates/`

### Naming Conventions
- Files: `lowercase-with-hyphens.md`
- Directories: `lowercase/`
- Special docs: `UPPERCASE.md` (README, AGENTS, etc.)

### What to Include

**For Templates**:
- Clear structure with sections
- Inline instructions or comments
- Example content
- When to use this template

**For Workflows**:
- Natural language trigger
- What it does (bullet list)
- When to use it
- Example usage
- Expected output

**For Tutorials**:
- Time estimate
- Clear goal
- Step-by-step instructions
- Common issues section
- Key takeaway

---

## Content Standards

### What We Accept

✅ **Yes**:
- Generic PM workflows applicable to many teams
- Template structures (without proprietary content)
- Process frameworks (RICE, OKRs, etc.)
- Learning resources and tutorials
- Voice sample formats (with example content)

❌ **No**:
- Proprietary company information
- Confidential product details
- Personal identifying information
- Specific customer data
- API keys or secrets

### Quality Standards
- Tested with AI assistants
- Clear and well-organized
- Follows style guidance in AGENTS.md
- Includes examples
- No typos or broken links

---

## Submission Process

### 1. Create an Issue First (Optional but Recommended)
For significant changes, create an issue to discuss:
- What you want to add
- Why it's valuable
- How it fits into existing structure

### 2. Make Your Changes
- Work in a dedicated branch
- Follow the style guide
- Keep changes focused
- Write clear commit messages

### 3. Test Your Changes
- Test workflows with AI assistant
- Verify all links work
- Check formatting renders correctly
- Ensure examples are accurate

### 4. Submit Pull Request
**PR Title**: Clear, descriptive
- ✅ `feat: add RICE scoring framework template`
- ✅ `docs: improve voice training tutorial`
- ❌ `updates`

**PR Description**:
```markdown
## What
Brief description of changes

## Why
Why this improvement is valuable

## Changes
- Bullet list of specific changes
- What was added/modified/removed

## Testing
How you tested these changes

## Checklist
- [ ] Follows style guide
- [ ] Tested with AI assistant
- [ ] Documentation updated
- [ ] Examples included
```

---

## Review Process

### What We Look For
1. **Value**: Does this help PMs work better with AI?
2. **Quality**: Is it well-written and clear?
3. **Consistency**: Follows style guide?
4. **Completeness**: Has examples and context?

### Timeline
- Initial review: Within 1 week
- Feedback provided if changes needed
- Merged when approved

### If Changes Requested
- Address feedback in same branch
- Push updates
- Comment when ready for re-review

---

## Types of Contributions

### 🆕 New Templates

**What to include**:
1. Template file in `templates/`
2. Example usage in `examples/example_files/`
3. Reference in relevant workflow doc
4. Entry in main README if major

**Example**:
```
templates/
└── pricing-strategy-template.md

examples/example_files/
└── pricing-strategy-example.md

examples/workflows/
└── generate-docs.md (updated to reference new template)
```

### 📋 New Workflows

**What to include**:
1. Workflow in appropriate category file in `examples/workflows/`
2. Example in `examples/example_files/` if complex
3. Update `examples/workflows/README.md` if new category

**Format**:
```markdown
### Workflow Name

```
/trigger or "natural language"
```

**What it does**:
- Action 1
- Action 2

**When to use**: Context

**Example**:
[Concrete example]
```

### 📚 New Tutorials

**What to include**:
1. Tutorial file in `examples/tutorials/`
2. Number it sequentially (05-your-topic.md)
3. Follow tutorial template
4. Update README to reference it

**Must have**:
- Time estimate
- Clear goal
- Step-by-step instructions
- Examples
- Common issues
- Key takeaway

### 🎯 Framework Documentation

**What to include**:
1. Framework doc in `knowledge/frameworks/`
2. When to use it
- How to apply it
3. Example application
4. Your adaptations

---

## Code of Conduct

### Our Standards

**Be respectful**:
- Assume good intent
- Provide constructive feedback
- Welcome newcomers

**Be collaborative**:
- Discuss significant changes
- Credit others' work
- Share learnings

**Be professional**:
- No harassment or discrimination
- Keep discussions on-topic
- Respect privacy

---

## Questions?

### Where to Ask
- Open an issue for project questions
- Start a discussion for ideas
- Comment on PRs for specific feedback

### Response Time
- Issues: Within 1 week
- PRs: Within 1 week for initial review
- Discussions: Best effort

---

## Recognition

Contributors will be:
- Listed in commit history
- Credited in relevant documentation
- Acknowledged in releases (if significant)

---

## License

By contributing, you agree that your contributions will be licensed under the same [MIT License](LICENSE) as the project.

---

## Getting Help

### Resources
- [README.md](README.md) - Project overview
- [AGENTS.md](AGENTS.md) - How AI uses this repo (includes style guidance)
- [examples/tutorials/](examples/tutorials/) - Learning guides

### Stuck?
Open an issue with:
- What you're trying to do
- What you've tried
- Where you're stuck

We're here to help!

---

**Thank you for making PM Co-Pilot better for everyone!** 🚀


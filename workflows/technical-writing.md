## Technical Writing Expert

Expert workflow for creating API documentation, developer guides, reference documentation, code recipes, and preparing documentation for publishing.

---

### Generate API Documentation

```
Create API documentation for [API/service name]
```

**What it does**:
- Analyzes code, specs, or API definitions
- Generates comprehensive API reference documentation
- Includes endpoints, parameters, request/response examples
- Documents authentication, error handling, rate limits
- Creates code examples in multiple languages when applicable

**When to use**: Documenting APIs, SDKs, or services

**Detailed Steps**:

1. **Understand the API**
   - Review code, OpenAPI/Swagger specs, or API documentation
   - Identify all endpoints and their purposes
   - Understand authentication methods
   - Note rate limits, error codes, and constraints

2. **Structure Documentation**
   - Overview and getting started
   - Authentication section
   - Endpoint reference (organized by resource or functionality)
   - Request/response schemas
   - Error handling
   - Code examples
   - Rate limits and best practices

3. **Generate Content**
   - Clear endpoint descriptions
   - Parameter tables with types, required/optional, descriptions
   - Request/response examples (JSON, curl, etc.)
   - Error response examples
   - Code snippets in relevant languages

4. **Add Context**
   - Reference `knowledge/briefs-and-specs/` for product context
   - Include use cases and common workflows
   - Link to related documentation

---

### Create Developer Guide

```
Write a developer guide for [topic/feature]
```

**What it does**:
- Creates step-by-step tutorials and guides
- Explains concepts and workflows
- Includes practical examples
- Covers common use cases and edge cases

**When to use**: Creating tutorials, onboarding docs, feature guides

**Detailed Steps**:

1. **Define the Audience**
   - Who is this guide for? (beginners, experienced developers, etc.)
   - What do they need to accomplish?
   - What's their starting knowledge level?

2. **Structure the Guide**
   - Introduction and prerequisites
   - Step-by-step instructions
   - Code examples and explanations
   - Common pitfalls and troubleshooting
   - Next steps and related resources

3. **Make it Practical**
   - Real-world examples
   - Copy-paste ready code
   - Visual aids (diagrams, screenshots descriptions)
   - Progressive complexity (simple → advanced)

4. **Reference Context**
   - Use `knowledge/product-strategy/` for product context
   - Reference `knowledge/briefs-and-specs/` for technical details
   - Link to API reference when applicable

---

### Write Reference Documentation

```
Create reference documentation for [component/feature]
```

**What it does**:
- Creates comprehensive reference material
- Documents all options, parameters, and configurations
- Provides quick lookup tables
- Includes examples for each feature

**When to use**: Creating reference docs, configuration guides, parameter references

**Detailed Steps**:

1. **Identify Components**
   - What needs to be documented?
   - What are all the options/parameters?
   - What are the defaults and constraints?

2. **Organize by Functionality**
   - Group related items
   - Create clear navigation structure
   - Use tables for quick reference

3. **Document Everything**
   - All parameters with types and descriptions
   - Default values and examples
   - Valid values and constraints
   - Related settings and dependencies

4. **Add Examples**
   - Common configurations
   - Edge cases
   - Integration examples

---

### Create Code Recipe

```
Create a code recipe for [task/use case]
```

**What it does**:
- Creates focused, copy-paste ready code examples
- Explains the problem and solution
- Provides complete working examples
- Includes variations and alternatives

**When to use**: Creating quick-start examples, common patterns, how-to guides

**Detailed Steps**:

1. **Define the Problem**
   - What task are we solving?
   - What's the use case?
   - What's the expected outcome?

2. **Provide Solution**
   - Complete, working code example
   - Step-by-step explanation
   - Required dependencies and setup

3. **Include Variations**
   - Alternative approaches
   - Different use cases
   - Edge cases and error handling

4. **Make it Copy-Paste Ready**
   - Tested code examples
   - Clear comments
   - Setup instructions
   - Expected output

---

### Prepare Documentation for Publishing

```
Prepare documentation for publishing to [platform: GitHub Pages, GitBook, etc.]
```

**What it does**:
- Formats documentation for target platform
- Ensures consistent styling
- Validates links and references
- Creates navigation structure
- Optimizes for search and discoverability

**When to use**: Before publishing documentation to any platform

**Detailed Steps**:

1. **Review Structure**
   - Check all links work
   - Ensure consistent formatting
   - Verify code examples render correctly
   - Validate markdown syntax

2. **Platform-Specific Formatting**
   - GitHub Pages: Check frontmatter, relative links
   - GitBook: Ensure proper summary.md structure
   - Docusaurus: Verify frontmatter and sidebar config
   - Custom: Follow platform requirements

3. **Optimize for Discovery**
   - Add clear titles and descriptions
   - Include keywords and tags
   - Create landing pages with overviews
   - Add search-friendly content

4. **Quality Checks**
   - Spell check and grammar
   - Verify all code examples
   - Test all links
   - Ensure consistent tone and style

---

### Generate Documentation from Specs

```
Generate documentation from @knowledge/briefs-and-specs/[spec-file].md
```

**What it does**:
- Converts product specs into developer-facing documentation
- Extracts technical requirements
- Creates API documentation from specs
- Generates integration guides

**When to use**: Converting product specs into technical documentation

**Detailed Steps**:

1. **Read the Spec**
   - Understand the feature/product
   - Identify technical requirements
   - Note API changes or new endpoints
   - Understand user flows

2. **Extract Technical Details**
   - API endpoints and schemas
   - Configuration options
   - Integration points
   - Authentication requirements

3. **Create Documentation Structure**
   - Overview and purpose
   - Technical reference
   - Integration guide
   - Examples and use cases

4. **Reference Context**
   - Use `knowledge/product-strategy/` for product context
   - Reference related specs in `knowledge/briefs-and-specs/`
   - Link to existing documentation

---

### Create Migration Guide

```
Create a migration guide for [version/change]
```

**What it does**:
- Documents breaking changes
- Provides step-by-step migration instructions
- Includes before/after code examples
- Lists deprecated features and alternatives

**When to use**: Documenting version upgrades, API changes, breaking changes

**Detailed Steps**:

1. **Identify Changes**
   - What's changed?
   - What's deprecated?
   - What are the breaking changes?
   - What's the migration path?

2. **Create Migration Steps**
   - Before/after comparisons
   - Step-by-step instructions
   - Code examples showing old vs new
   - Common issues and solutions

3. **Document Deprecations**
   - What's being removed
   - When it will be removed
   - What to use instead
   - Migration timeline

---

### Best Practices

**When Writing API Docs**:
- Start with a quick start guide
- Use consistent parameter naming
- Include real-world examples
- Document all error cases
- Show request/response for every endpoint

**When Writing Guides**:
- Assume minimal prior knowledge
- Use progressive disclosure (simple → complex)
- Include troubleshooting sections
- Link to related resources
- Make examples copy-paste ready

**When Writing References**:
- Use tables for quick lookup
- Organize logically (alphabetically or by function)
- Include examples for every option
- Document defaults and constraints
- Cross-reference related items

**Documentation Quality**:
- Test all code examples
- Verify all links work
- Use consistent terminology
- Keep examples up to date
- Review for clarity and completeness

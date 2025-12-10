## Prototype Expert

Expert workflow for creating working code prototypes based on product briefs or specs. **This is one of two workflows that can create code** (along with `mcp-generator.md` for MCP servers) - all other workflows stay within markdown and product management.

---

### Create a Prototype

```
Create a prototype for [feature name] based on @knowledge/briefs-and-specs/[spec-file].md
```

or

```
Build a prototype from @initiatives/[initiative-name].md
```

**What it does**:
- Reads product briefs or specs to understand requirements
- Creates working code prototypes in `code/` folder
- Generates functional implementations to validate concepts
- Includes setup instructions and basic documentation

**When to use**: When you need to validate a concept with a working prototype, demonstrate feasibility, or test user flows with code

**Detailed Steps**:

1. **Understand the Requirements**
   - Read the brief or spec file referenced
   - Identify key features and user flows
   - Note technical requirements and constraints
   - Understand the target platform/technology (web, mobile, API, etc.)
   - Check `knowledge/product-strategy/` for context if needed

2. **Determine Prototype Scope**
   - What's the minimum viable prototype to validate the concept?
   - Which features are essential vs. nice-to-have?
   - What technology stack makes sense? (Consider existing systems if mentioned)
   - What's the simplest implementation that demonstrates value?

3. **Create Project Structure**
   - Create a new folder in `code/` named after the feature/project (use lowercase-with-hyphens)
   - For web apps: Set up Next.js or Vite + React project
   - Initialize Shadcn/ui: `npx shadcn@latest init` (choose TypeScript, Tailwind CSS, default style)
   - Install required Shadcn components as needed
   - Include necessary configuration files (package.json, tsconfig.json, tailwind.config.js, etc.)
   - Add a README.md with setup instructions including Shadcn setup steps

4. **Implement Core Features**
   - Build the essential user flows from the spec
   - Use Shadcn/ui components for all UI elements (Button, Card, Input, Dialog, etc.)
   - Leverage Shadcn's built-in accessibility and styling
   - Focus on functionality over polish (this is a prototype)
   - Include basic error handling
   - Add comments explaining key decisions
   - Make it runnable/executable

5. **Add Documentation**
   - README.md with:
     - What this prototype demonstrates
     - Setup and run instructions
     - Key features implemented
     - What's missing/out of scope
   - Link back to the original spec/brief

6. **Validate Against Spec**
   - Ensure prototype addresses the core problem statement
   - Verify key user flows are implemented
   - Note any gaps or simplifications made for prototyping

---

### Update a Prototype

```
Update the prototype in code/[prototype-name] to add [feature]
```

**What it does**:
- Modifies existing prototype code
- Adds new features or improvements
- Updates documentation

**When to use**: Iterating on an existing prototype

**Detailed Steps**:

1. **Review Current Prototype**
   - Read existing code and README
   - Understand current implementation
   - Check what needs to be added/changed

2. **Review Updated Requirements**
   - Check if spec/brief has been updated
   - Understand new requirements
   - Identify what needs to change

3. **Make Changes**
   - Update code to add new features
   - Maintain existing functionality
   - Update documentation

4. **Test Integration**
   - Ensure new features work with existing code
   - Update README if needed

---

### Create Prototype from User Stories

```
Create a prototype that implements these user stories: [paste user stories]
```

**What it does**:
- Takes user stories and creates a working prototype
- Implements the core flows described
- Validates the concept with code

**When to use**: When you have user stories but no full spec yet

**Detailed Steps**:

1. **Parse User Stories**
   - Extract key actions and flows
   - Identify acceptance criteria
   - Understand the user journey

2. **Design Minimal Implementation**
   - What's the simplest code that demonstrates these stories?
   - What technology fits best?
   - What can be mocked vs. fully implemented?

3. **Build and Document**
   - Follow steps 3-6 from "Create a Prototype" above

---

### Best Practices

**When Creating Prototypes**:
- **Start Simple**: Focus on core value proposition first
- **Make it Runnable**: Prototype should actually work, not just be code structure
- **Document Assumptions**: Note what you simplified or mocked
- **Link to Source**: Always reference the original spec/brief
- **Keep it Focused**: Don't build everything - just enough to validate the concept

**Technology Choices**:
- **Web Apps**: 
  - Use **React with Shadcn/ui** for all UI components
  - Set up with Next.js (App Router) or Vite + React
  - Use Tailwind CSS (required for Shadcn)
  - Install Shadcn components as needed: `npx shadcn@latest add [component]`
  - Prefer Shadcn components over custom UI - they're production-ready and accessible
- **APIs**: Use lightweight frameworks (Express, Flask, FastAPI) with clear endpoints
- **Mobile**: Consider web-based prototypes first (React Native, PWA) unless native is required
- **CLI Tools**: Use standard libraries, keep dependencies minimal
- **Data/ML**: Use Jupyter notebooks for data exploration, simple scripts for models

**Code Quality**:
- **Functional First**: Code should work, even if not production-ready
- **Clear Comments**: Explain why, not just what
- **Simple Structure**: Don't over-engineer for a prototype
- **Error Handling**: Basic error handling to make it usable

**What to Include**:
- ✅ Core user flows
- ✅ Basic UI/UX using Shadcn/ui components
- ✅ Key business logic
- ✅ Setup instructions (including Shadcn initialization)
- ✅ Link to original spec
- ✅ List of Shadcn components used

**What to Skip**:
- ❌ Production-ready error handling
- ❌ Comprehensive testing
- ❌ Performance optimization
- ❌ Security hardening
- ❌ Full feature set

---

### Prototype Lifecycle

1. **Creation**: Build initial prototype from spec/brief
2. **Iteration**: Update based on feedback or new requirements
3. **Validation**: Use prototype to validate concept with users/stakeholders
4. **Handoff**: When ready, hand off to engineering team (prototype serves as reference)
5. **Archive**: Move to `code/archive/` when no longer needed

---

### Integration with Other Workflows

- **Input**: Uses specs from `product-docs.md` workflow
- **Output**: Can inform `product-docs.md` with technical feasibility findings
- **Reference**: Links to initiatives in `initiatives/` folder
- **Documentation**: Prototypes can be referenced in specs and briefs

---

### Important Notes

⚠️ **This is one of two workflows that creates code files** (along with `mcp-generator.md`)

- All other workflows stay in markdown
- Prototypes are for validation, not production
- Code goes in `code/` folder (gitignored)
- Always link back to the original spec/brief
- Prototypes are temporary - archive when done

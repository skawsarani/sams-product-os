---
name: prototype-builder
description: Builds working React/TypeScript prototypes from PRDs, product briefs, or user stories using Shadcn/ui components. Invoked when asked to create prototypes, validate concepts with code, or build functional demos from product requirements.
---

# Prototype Builder

Create functional code prototypes from product requirements to validate concepts and demonstrate feasibility.

## Quick Start

### From a PRD or Brief

1. Read the PRD/brief to understand requirements
2. Extract requirements: `python scripts/extract_requirements.py path/to/prd.md`
3. Initialize project: `python scripts/init_prototype.py <project-name>`
4. Build prototype based on identified components and flows
5. Test and validate against requirements

### From User Stories

1. Parse user stories to identify key flows and components
2. Extract requirements (manually identify UI needs)
3. Initialize project and implement core flows

## Workflow

### 1. Understand Requirements

**Read the source document** (PRD, brief, or user stories):
- Identify core features and user flows
- Note technical constraints
- Understand success criteria

**Extract UI components**:
```bash
python scripts/extract_requirements.py path/to/prd.md
```

This analyzes the document and suggests:
- Shadcn components to install
- User interactions to implement
- Data requirements
- Key features

### 2. Initialize Project

**Create new prototype**:
```bash
python scripts/init_prototype.py <project-name>
cd <project-name>
npm install
```

This creates a complete React + TypeScript + Vite + Shadcn/ui project.

**Install required components**:
```bash
# Install components identified in step 1
npx shadcn@latest add button card input dialog table
# etc.
```

### 3. Build Core Features

**Focus on essential flows** - not production-ready implementation:
- Implement key user journeys
- Use Shadcn components for all UI
- Keep business logic simple but functional
- Add basic error handling

**Reference patterns**:
- See `references/ui-patterns.md` for common layouts
- See `references/shadcn-components.md` for component usage

**Use template pages** as starting points:
- `assets/DashboardPage.tsx` - Dashboard layout
- `assets/FormPage.tsx` - Form with validation
- `assets/DataTablePage.tsx` - Interactive data table

### 4. Document and Validate

**Update README.md** with:
- What the prototype demonstrates
- Setup and run instructions
- Key features implemented
- What's out of scope
- Link to original PRD/brief

**Validate against requirements**:
- Core problem addressed?
- Key user flows implemented?
- Assumptions documented?

## Component Selection Guide

When implementing features, choose components based on interactions:

**Forms & Input**:
- Text entry → `input`, `textarea`
- Selection → `select`, `radio-group`, `checkbox`
- Validation → `form` (with react-hook-form + zod)

**Layout & Display**:
- Containers → `card`, `separator`
- Lists/grids → `table`, custom grid layouts
- Navigation → `tabs`, `accordion`

**Actions & Feedback**:
- User actions → `button`, `dialog`
- Notifications → `toast`, `alert`
- Loading states → `skeleton`

**Data & Status**:
- Tags/labels → `badge`
- Metrics → `card` with custom content
- User info → `avatar`

See `references/shadcn-components.md` for complete reference.

## Best Practices

**Scope**:
- Build minimum to validate concept
- Focus on core flows, skip edge cases
- Mock complex backend logic
- Document simplifications

**Code Quality**:
- Functional but not production-ready
- Clear comments for key decisions
- Simple, understandable structure
- Basic error handling only

**What to Include**:
- Core user flows
- Key business logic
- Basic UI/UX with Shadcn
- Setup instructions

**What to Skip**:
- Comprehensive testing
- Performance optimization
- Security hardening
- Full feature set
- Production error handling

## Project Structure

```
project-name/
├── src/
│   ├── components/     # Shadcn components (auto-generated)
│   │   └── ui/
│   ├── lib/           # Utils (cn function, etc.)
│   ├── App.tsx        # Main app component
│   └── main.tsx       # Entry point
├── package.json
├── tailwind.config.js
├── components.json    # Shadcn config
└── README.md
```

## Common Patterns

### Dashboard Prototype
```bash
python scripts/init_prototype.py dashboard-prototype
cd dashboard-prototype
npm install
npx shadcn@latest add card button
```

Copy `assets/DashboardPage.tsx` to `src/Dashboard.tsx` and import in `App.tsx`.

### Form-Heavy Prototype
```bash
python scripts/init_prototype.py form-prototype
cd form-prototype
npm install
npm install react-hook-form zod @hookform/resolvers
npx shadcn@latest add form input textarea select checkbox button
```

Copy `assets/FormPage.tsx` to `src/FormPage.tsx`.

### Data Table Prototype
```bash
python scripts/init_prototype.py table-prototype
cd table-prototype
npm install
npx shadcn@latest add table input button badge dropdown-menu dialog
```

Copy `assets/DataTablePage.tsx` to `src/TablePage.tsx`.

## Troubleshooting

**Shadcn component not found**: Ensure you've run `npx shadcn@latest add <component>`

**TypeScript errors**: Check that path alias `@/` is configured in `tsconfig.json`

**Styling not working**: Verify Tailwind is configured and `index.css` is imported

**Import errors**: Ensure all required packages are installed (`npm install`)

## Resources

- **Component Reference**: `references/shadcn-components.md`
- **UI Patterns**: `references/ui-patterns.md`
- **Shadcn Docs**: https://ui.shadcn.com/docs
- **Lucide Icons**: https://lucide.dev/icons/

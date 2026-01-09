#!/bin/bash

# PM Co-Pilot Setup Script
# This script helps you set up your PM Co-Pilot workspace with essential structure and templates

set -e  # Exit on error

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo -e "${BLUE}╔════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║         PM Co-Pilot Setup - Getting Started               ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════╝${NC}"
echo ""
echo -e "${YELLOW}This script will set up your PM Co-Pilot workspace by:${NC}"
echo ""
echo "  1. Creating the knowledge base directory structure"
echo "     • Personal context (about-me)"
echo "     • Company context and product strategy"
echo "     • Frameworks, processes, and references"
echo "     • Templates for specs, briefs, and documentation"
echo ""
echo "  2. Creating essential template files"
echo "     • about-me.md - Your personal PM context"
echo "     • company-overview.md - Company information"
echo "     • current-strategy.md - Product strategy"
echo "     • how-we-work.md - Team processes"
echo ""
echo "  3. Setting up BACKLOG.md"
echo "     • Your daily inbox for notes, ideas, and tasks"
echo ""
echo "  4. Configuring AI assistant integration"
echo "     • Symlinks for skills/commands auto-discovery"
echo "     • Task Manager MCP server configuration"
echo ""
echo -e "${YELLOW}Note:${NC} Existing directories and files will be preserved."
echo -e "      The script will only create what's missing."
echo ""
read -p "Press Enter to begin setup, or Ctrl+C to cancel... "
echo ""

# Function to check if directory exists and show message
check_and_create_dir() {
    local dir="$1"
    local description="$2"
    
    if [ -d "$dir" ]; then
        echo -e "${YELLOW}ℹ️  Directory already exists: ${dir}${NC}"
        echo -e "   ${description}"
        echo ""
        return 0  # Return 0 even if exists - not an error condition
    else
        mkdir -p "$dir"
        echo -e "${GREEN}✓ Created directory: ${dir}${NC}"
        echo -e "   ${description}"
        echo ""
        return 0
    fi
}

# Function to create template file if it doesn't exist
create_template_file() {
    local file="$1"
    local content="$2"
    local description="$3"
    
    if [ -f "$file" ]; then
        echo -e "${YELLOW}ℹ️  File already exists: ${file}${NC}"
        echo -e "   Skipping to preserve your existing content"
        echo ""
        return 0  # Return 0 even if exists - not an error condition
    else
        echo "$content" > "$file"
        echo -e "${GREEN}✓ Created template file: ${file}${NC}"
        echo -e "   ${description}"
        echo ""
        return 0
    fi
}

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}Step 1: Creating Knowledge Base Structure${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Create knowledge base directories
check_and_create_dir "knowledge/about-me" "Personal PM context, working style, preferences"
check_and_create_dir "knowledge/company-context" "Company vision, mission, values, org structure"
check_and_create_dir "knowledge/product-strategy" "Product vision, roadmap, strategic pillars"
check_and_create_dir "knowledge/frameworks" "PM frameworks and methodologies (RICE, OKRs, etc.)"
check_and_create_dir "knowledge/processes" "How your team works (rituals, frameworks, decision-making)"
check_and_create_dir "knowledge/product-analytics" "Success metrics, KPIs, current performance data (content gitignored)"
check_and_create_dir "knowledge/briefs-and-specs" "Product specs, feature briefs, technical documentation"
check_and_create_dir "knowledge/opportunities" "Strategic opportunities identified from backlog"
check_and_create_dir "knowledge/transcripts" "User interviews, stakeholder meetings, research sessions"
check_and_create_dir "knowledge/voice-samples" "Writing samples for matching communication style"
check_and_create_dir "knowledge/references" "Useful info, links, competitive analysis"
check_and_create_dir "knowledge/proposals" "Decision docs, RFCs, proposals"
check_and_create_dir "knowledge/notes" "Archived inbox snapshots, meeting notes, uncategorized items"
check_and_create_dir "tasks" "Your task files (gitignored)"

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}Step 2: Creating Essential Template Files${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Template for about-me.md
ABOUT_ME_TEMPLATE='# About Me

## Background
[Your PM experience, domain expertise, previous roles]

## Working Style
- Communication preferences: [How you like to communicate]
- Decision-making style: [How you make decisions]
- Tools you use: [Project management, design, analytics tools]

## Product Philosophy
- Core beliefs: [Your product principles]
- Frameworks you use: [RICE, OKRs, Jobs-to-be-Done, etc.]

## Current Context
- Company stage: [Startup, growth, enterprise]
- Team size: [Your team structure]
- This quarter'\''s focus: [Key priorities]

## Strengths
- [Your key strengths as a PM]

## Growth Areas
- [Areas you'\''re working on]

---

**Tip**: Be specific! The more detail you provide, the better AI can tailor its responses to your style and context.
See `templates/about-me-template.md` for more detailed examples.
'

# Template for company-overview.md
COMPANY_OVERVIEW_TEMPLATE='# Company Overview

## Mission
[Your company mission]

## Products
[What you build, who it'\''s for]

## Target Customers
- [Customer segment 1]: [Description]
- [Customer segment 2]: [Description]

## Team Structure
- Product: [Team size, structure]
- Engineering: [Team size, structure]
- Design: [Team size, structure]

## Current Stage
[Startup, growth, enterprise]

## Key Stakeholders
- [Name, role, what they care about]

---

**Tip**: Keep this updated as your company evolves. This helps AI understand your business context.
'

# Template for current-strategy.md
CURRENT_STRATEGY_TEMPLATE='# Product Strategy

## Vision
[Where are you going? What is your product vision?]

## Strategic Pillars
1. **[Pillar 1]**: [Description]
2. **[Pillar 2]**: [Description]
3. **[Pillar 3]**: [Description]

## Current Priorities
1. [Priority 1]
2. [Priority 2]
3. [Priority 3]

## Success Metrics
- [Metric 1]: Current X, Target Y
- [Metric 2]: Current X, Target Y

## Key Challenges
- [Challenge 1]
- [Challenge 2]

---

**Tip**: Update this quarterly or when priorities shift. AI uses this to align recommendations with your strategy.
'

# Template for how-we-work.md
HOW_WE_WORK_TEMPLATE='# How We Work

## Team Process
- Sprint cadence: [Weekly, bi-weekly, etc.]
- Planning process: [How you plan work]
- Review process: [How you review completed work]

## Decision-Making
- How decisions are made: [Process for making product decisions]
- Who makes decisions: [Decision-makers and their roles]
- Escalation process: [When and how to escalate]

## Communication
- Meeting cadence: [Standups, retros, reviews, etc.]
- Communication tools: [Slack, email, etc.]
- Documentation: [Where you document decisions and processes]

## Frameworks We Use
- Prioritization: [RICE, Value vs Effort, etc.]
- Goal-setting: [OKRs, Milestones, etc.]
- Research: [Jobs-to-be-Done, Customer interviews, etc.]

---

**Tip**: Document your actual process, not the ideal. This helps AI understand how to work within your team'\''s constraints.
'

# Create template files
create_template_file "knowledge/about-me/about-me.md" "$ABOUT_ME_TEMPLATE" "Personal context template - helps AI understand your background and working style"
create_template_file "knowledge/company-context/company-overview.md" "$COMPANY_OVERVIEW_TEMPLATE" "Company context template - helps AI understand your business"
create_template_file "knowledge/product-strategy/current-strategy.md" "$CURRENT_STRATEGY_TEMPLATE" "Product strategy template - helps AI align recommendations with your vision"
create_template_file "knowledge/processes/how-we-work.md" "$HOW_WE_WORK_TEMPLATE" "Team process template - helps AI understand your workflow"

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}Step 3: Setting Up BACKLOG.md${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Handle BACKLOG.md
if [ -f "BACKLOG.md" ]; then
    echo -e "${YELLOW}ℹ️  BACKLOG.md already exists${NC}"
    echo -e "   Your existing BACKLOG.md is preserved."
    echo -e "   This file is your daily inbox for notes, ideas, tasks, and thoughts."
    echo ""
else
    # Use current BACKLOG.md content as template (from the repo)
    BACKLOG_CONTENT='# Backlog

Your daily inbox for all notes, ideas, tasks, and thoughts. Capture everything here throughout the day.

Say `process my backlog` when you'\''re ready to categorize and organize items into opportunities, tasks, references, or archive.
'
    echo "$BACKLOG_CONTENT" > "BACKLOG.md"
    echo -e "${GREEN}✓ Created BACKLOG.md${NC}"
    echo -e "   This is your daily inbox for capturing ideas, tasks, and notes."
    echo -e "   Say 'process my backlog' or '/backlog' when ready to organize items."
    echo ""
fi

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}Step 4: Setting Up Goals${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

if [ -f "GOALS.md" ]; then
    echo -e "${YELLOW}ℹ️  GOALS.md already exists${NC}"
    echo -e "   Your existing GOALS.md is preserved."
    echo ""
else
    # Create GOALS.md with template
    cat > "GOALS.md" << 'EOF'
# Goals

Define your personal and business goals here. AI will use these to align task priorities and recommendations.

---

## How to Use This File

1. Define 3-5 quarterly goals (too many = unfocused)
2. Update quarterly or when priorities shift
3. AI references this during:
   - Weekly reviews (goal progress tracking)
   - Daily planning (priority alignment)
   - Backlog processing (strategic task categorization)

**Tip**: Make goals specific and measurable. Vague goals get vague results.

---

## Current Quarter Goals

### Goal 1: [Goal Name]

**Description**: [What you want to achieve]

**Why it matters**: [Impact / Strategic alignment]

**Success criteria**:
- [ ] [Measurable milestone 1]
- [ ] [Measurable milestone 2]

**Target date**: [YYYY-MM-DD]

---

### Goal 2: [Goal Name]

**Description**: [What you want to achieve]

**Why it matters**: [Impact / Strategic alignment]

**Success criteria**:
- [ ] [Measurable milestone 1]
- [ ] [Measurable milestone 2]

**Target date**: [YYYY-MM-DD]

---

### Goal 3: [Goal Name]

**Description**: [What you want to achieve]

**Why it matters**: [Impact / Strategic alignment]

**Success criteria**:
- [ ] [Measurable milestone 1]
- [ ] [Measurable milestone 2]

**Target date**: [YYYY-MM-DD]

---

## Archive

Move completed goals here for reference.
EOF

    echo -e "${GREEN}✓ Created GOALS.md${NC}"
    echo -e "   Define your quarterly goals here for AI-powered priority alignment."
    echo ""

    # Ask if user wants to define goals now
    echo -e "${YELLOW}Would you like to define your goals now? (y/n)${NC}"
    read -p "> " define_goals
    echo ""

    if [[ "$define_goals" =~ ^[Yy]$ ]]; then
        echo -e "${BLUE}Let's define your top 3 goals for this quarter.${NC}"
        echo ""

        for i in 1 2 3; do
            echo -e "${YELLOW}Goal $i:${NC}"
            read -p "  What do you want to achieve? " goal_desc
            echo ""
        done

        echo -e "${GREEN}✓ Goals captured!${NC}"
        echo -e "   You can refine them anytime by editing GOALS.md"
        echo -e "   AI will help align your tasks to these goals."
        echo ""
    else
        echo -e "${YELLOW}No problem! You can add your goals anytime by editing GOALS.md${NC}"
        echo ""
    fi
fi

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}Step 5: AI Assistant Integration (Optional)${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

echo -e "${YELLOW}Which AI assistants do you want to configure?${NC}"
echo ""
echo "This will:"
echo "  • Create symlinks for skills/commands auto-discovery"
echo "  • Set up Task Manager MCP server configuration"
echo ""
echo "  1) Both Claude Code and Cursor"
echo "  2) Only Claude Code"
echo "  3) Only Cursor"
echo "  4) Skip (configure manually later)"
echo ""
read -p "Choose option (1-4) > " ai_choice
echo ""

# Function to create symlinks for a directory
create_symlinks_for_dir() {
    local dir="$1"

    # Create directory if needed
    if [ ! -d "$dir" ]; then
        mkdir -p "$dir"
        echo -e "${GREEN}✓ Created directory: ${dir}/${NC}"
    fi

    # Create skills symlink
    if [ ! -e "$dir/skills" ]; then
        ln -s ../skills "$dir/skills"
        echo -e "${GREEN}✓ Created symlink: ${dir}/skills → skills/${NC}"
    else
        echo -e "${YELLOW}ℹ️  Symlink ${dir}/skills already exists (skipping)${NC}"
    fi

    # Create commands symlink
    if [ ! -e "$dir/commands" ]; then
        ln -s ../commands "$dir/commands"
        echo -e "${GREEN}✓ Created symlink: ${dir}/commands → commands/${NC}"
    else
        echo -e "${YELLOW}ℹ️  Symlink ${dir}/commands already exists (skipping)${NC}"
    fi
}

# Function to setup MCP config for Claude Code (.mcp.json in root)
setup_mcp_claude() {
    local mcp_file=".mcp.json"

    if [ -f "$mcp_file" ]; then
        echo -e "${YELLOW}ℹ️  ${mcp_file} already exists${NC}"
        echo -e "   To add the Task Manager MCP, merge this into your existing config:"
        echo ""
        echo -e "${BLUE}   {${NC}"
        echo -e "${BLUE}     \"mcpServers\": {${NC}"
        echo -e "${BLUE}       \"pm-tasks\": {${NC}"
        echo -e "${BLUE}         \"command\": \"uv\",${NC}"
        echo -e "${BLUE}         \"args\": [\"run\", \"--directory\", \"./core/task-manager\", \"python\", \"server.py\"]${NC}"
        echo -e "${BLUE}       }${NC}"
        echo -e "${BLUE}     }${NC}"
        echo -e "${BLUE}   }${NC}"
        echo ""
    else
        cp "core/task-manager/mcp.json.sample" "$mcp_file"
        echo -e "${GREEN}✓ Created ${mcp_file} with Task Manager MCP configuration${NC}"
    fi
}

# Function to setup MCP config for Cursor (.cursor/mcp.json)
setup_mcp_cursor() {
    local mcp_dir=".cursor"
    local mcp_file="${mcp_dir}/mcp.json"

    # Create .cursor directory if needed
    if [ ! -d "$mcp_dir" ]; then
        mkdir -p "$mcp_dir"
    fi

    if [ -f "$mcp_file" ]; then
        echo -e "${YELLOW}ℹ️  ${mcp_file} already exists${NC}"
        echo -e "   To add the Task Manager MCP, merge this into your existing config:"
        echo ""
        echo -e "${BLUE}   {${NC}"
        echo -e "${BLUE}     \"mcpServers\": {${NC}"
        echo -e "${BLUE}       \"pm-tasks\": {${NC}"
        echo -e "${BLUE}         \"command\": \"uv\",${NC}"
        echo -e "${BLUE}         \"args\": [\"run\", \"--directory\", \"./core/task-manager\", \"python\", \"server.py\"]${NC}"
        echo -e "${BLUE}       }${NC}"
        echo -e "${BLUE}     }${NC}"
        echo -e "${BLUE}   }${NC}"
        echo ""
    else
        cp "core/task-manager/mcp.json.sample" "$mcp_file"
        echo -e "${GREEN}✓ Created ${mcp_file} with Task Manager MCP configuration${NC}"
    fi
}

case "$ai_choice" in
    1)
        echo -e "${BLUE}Configuring both Claude Code and Cursor...${NC}"
        echo ""
        echo -e "${BLUE}Creating symlinks...${NC}"
        create_symlinks_for_dir ".claude"
        create_symlinks_for_dir ".cursor"
        echo ""
        echo -e "${BLUE}Setting up MCP configuration...${NC}"
        setup_mcp_claude
        setup_mcp_cursor
        echo ""
        ;;
    2)
        echo -e "${BLUE}Configuring Claude Code...${NC}"
        echo ""
        echo -e "${BLUE}Creating symlinks...${NC}"
        create_symlinks_for_dir ".claude"
        echo ""
        echo -e "${BLUE}Setting up MCP configuration...${NC}"
        setup_mcp_claude
        echo ""
        ;;
    3)
        echo -e "${BLUE}Configuring Cursor...${NC}"
        echo ""
        echo -e "${BLUE}Creating symlinks...${NC}"
        create_symlinks_for_dir ".cursor"
        echo ""
        echo -e "${BLUE}Setting up MCP configuration...${NC}"
        setup_mcp_cursor
        echo ""
        ;;
    *)
        echo -e "${YELLOW}Skipped AI assistant configuration.${NC}"
        echo -e "   You can configure manually later using the sample at:"
        echo -e "   core/task-manager/mcp.json.sample"
        echo ""
        ;;
esac

echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}Setup Complete! 🎉${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

echo -e "${GREEN}What was created:${NC}"
echo "  ✓ Knowledge base directory structure"
echo "  ✓ Tasks directory"
echo "  ✓ Template files for essential context"
echo "  ✓ BACKLOG.md (your daily inbox)"
echo "  ✓ GOALS.md (your quarterly goals)"
if [[ "$ai_choice" =~ ^[1-3]$ ]]; then
echo "  ✓ AI assistant configuration (symlinks + MCP)"
fi
echo ""

echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${YELLOW}Next Steps:${NC}"
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

echo -e "${BLUE}1. Fill in your context files (15-20 minutes):${NC}"
echo "   • Edit knowledge/about-me/about-me.md - Add your background and working style"
echo "   • Edit knowledge/company-context/company-overview.md - Add company info"
echo "   • Edit knowledge/product-strategy/current-strategy.md - Add your product vision"
echo "   • Edit knowledge/processes/how-we-work.md - Document your team process"
echo "   • Edit GOALS.md - Define your quarterly goals (3-5 goals max)"
echo ""

echo -e "${BLUE}2. Start using your BACKLOG.md:${NC}"
echo "   • Add ideas, tasks, notes throughout the day"
echo "   • Say 'process my backlog' or '/backlog' to organize items"
echo ""

echo -e "${BLUE}3. Tell your AI assistant:${NC}"
echo "   Read @AGENTS.md to understand how to help me as a PM Co-Pilot."
echo ""

echo -e "${BLUE}4. Try daily and weekly workflows:${NC}"
echo "   • Morning: 'What should I work on today?'"
echo "   • Friday/Sunday: 'Run weekly review'"
echo "   • See workflows/README.md for all workflows"
echo ""

echo -e "${BLUE}5. Generate your first document:${NC}"
echo "   • Add opportunity to BACKLOG.md"
echo "   • Say: '/backlog' to process it"
echo "   • Say: '/spec [opportunity-name]' to generate spec"
echo ""

echo -e "${BLUE}6. Install Task Manager MCP dependencies (for faster task ops):${NC}"
echo "   • cd core/task-manager && python3 -m pip install -r requirements.txt"
echo "   • Restart your AI assistant to load the MCP server"
echo ""

echo -e "${BLUE}7. Learn more:${NC}"
echo "   • Read README.md for complete guide"
echo "   • Browse templates/ for document examples"
echo "   • Explore skills/ for available capabilities"
echo ""

echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${YELLOW}Important Notes:${NC}"
echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo -e "• ${GREEN}BACKLOG.md is gitignored${NC} - your private notes stay local"
echo -e "• ${GREEN}knowledge/ directory content is gitignored${NC} - your context stays private"
echo -e "• ${GREEN}product-analytics/ subdirectories are gitignored${NC} - only structure preserved"
echo -e "• Template files are starting points - customize them to fit your needs"
echo -e "• You can always add more context files as you go"
echo ""

echo -e "${GREEN}You're all set! Start by filling in your context files, then begin using BACKLOG.md.${NC}"
echo ""

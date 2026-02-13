# SAMS PRODUCT OS Evaluation Suite

Validates that the agent, MCP server, and workflows work correctly after changes.

## Setup

From the project root:

```bash
uv sync --extra evals
```

Dependencies are managed in the root `pyproject.toml`.

## Quick Start

```bash
# Run all evals
uv run python evals/run_evals.py

# Run specific test suites
uv run python evals/run_evals.py --mcp        # MCP server tests
uv run python evals/run_evals.py --workflows  # Workflow tests
uv run python evals/run_evals.py --behavior   # Agent behavior tests
uv run python evals/run_evals.py --llm        # LLM behavioral evals (needs ANTHROPIC_API_KEY)

# Or use pytest directly
uv run pytest evals/ -v                            # All eval tests
uv run pytest tools/mcp-servers/task-manager/test_server.py -v   # MCP unit tests
```

## What's Tested

| Component | Test File | What's Tested |
|-----------|-----------|---------------|
| **MCP Server** | `test_mcp_server.py` | Task CRUD, status transitions, priority caps, auto-categorization |
| **Workflows** | `test_workflows.py` | Backlog classification, deduplication, ambiguity detection |
| **Agent Behavior** | `test_agent_behavior.py` | Confirmation requirements, goal alignment, clarification triggers |
| **LLM Behavioral** | `test_llm_behavior.py` | Real Claude API calls graded against rubrics (6 scenarios) |

## Directory Structure

```
evals/
├── README.md                  # This file
├── run_evals.py               # Test runner with options
├── conftest.py                # Shared pytest fixtures
├── test_mcp_server.py         # MCP server integration tests
├── test_workflows.py          # Workflow logic tests
├── test_agent_behavior.py     # Agent behavioral requirement tests
├── test_llm_behavior.py       # LLM-in-the-loop behavioral evals
├── fixtures/
│   ├── test-backlogs/
│   │   ├── basic.md
│   │   ├── mixed-items.md
│   │   └── behavioral-scenarios.md
│   └── llm_scenarios/
│       ├── __init__.py
│       └── backlog_processing.py  # 6 eval scenarios + judge prompts
└── expected/
    └── outputs/
        ├── basic.json
        └── behavioral-scenarios.json
```

## Test Categories

### MCP Server Tests (`test_mcp_server.py`)
- Task CRUD operations (create, read, update)
- Status transitions (n → s → b → d)
- Priority cap enforcement (P0: 3, P1: 7, P2: 15)
- Auto-categorization based on keywords
- Similarity calculation for deduplication

### Workflow Tests (`test_workflows.py`)
- Item classification (tasks, initiatives, references, notes)
- Ambiguity detection for vague backlog items
- Clarification question generation
- Auto-categorization from config keywords

### Agent Behavior Tests (`test_agent_behavior.py`)
- **Workflow compliance**: Verifies `.claude/skills/processing-backlog/SKILL.md` contains required behavioral instructions
- **AGENTS.md compliance**: Verifies core rules, clarification requirements, goal references, priority system
- **Goal alignment**: Tasks should link to goals, orphan tasks flagged
- **Clarification requirements**: Ambiguous items trigger questions
- **Confirmation requirements**: Bulk operations, priority changes need confirmation

### LLM Behavioral Evals (`test_llm_behavior.py`)

True LLM-backed evals that test whether the agent actually follows behavioral contracts. Uses an **LLM-as-judge** pattern: one Claude call generates the agent response, a second call grades it against a rubric.

**Requires**: `ANTHROPIC_API_KEY` in `.env` or environment (auto-skips if not set).
**Cost**: ~$0.10-0.20 per full suite run.

| # | Scenario | Tests | Threshold |
|---|----------|-------|-----------|
| 1 | Ambiguous item ("Fix the thing") | Asks clarification, doesn't create, flags ambiguity | 1.0 |
| 2 | Mixed backlog (4 items) | Categorizes, presents summary, waits for confirmation | 0.8 |
| 3 | Orphan task (no goal match) | Flags no goal, asks about alignment | 1.0 |
| 4 | P0 cap exceeded | Warns about cap, shows existing P0s, offers options | 0.8 |
| 5 | Duplicate detection | Flags duplicate, shows existing, asks user | 0.8 |
| 6 | Clear item matching Goal 3 | Links to goal, suggests category, presents for review | 0.8 |

**Env vars:**
- `ANTHROPIC_API_KEY` — required
- `LLM_EVAL_MODEL` — model for agent under test (default: `claude-sonnet-4-20250514`)
- `LLM_JUDGE_MODEL` — model for the judge (default: `claude-sonnet-4-20250514`)

**Adding new scenarios:** Create a new `EvalScenario` in `evals/fixtures/llm_scenarios/backlog_processing.py` and add it to `build_scenarios()`. Tests auto-discover via parametrize.

## Running Tests

### All Tests

```bash
uv run python evals/run_evals.py
```

### Individual Test Files

```bash
# MCP server tests
uv run pytest evals/test_mcp_server.py -v

# Workflow tests
uv run pytest evals/test_workflows.py -v

# Agent behavior tests
uv run pytest evals/test_agent_behavior.py -v
```

### With Markers

```bash
# Skip slow tests
uv run pytest evals/ -v -m "not slow"

# Only integration tests
uv run pytest evals/ -v -m integration

# LLM evals only
# With .env (recommended)
uv run pytest evals/test_llm_behavior.py -v

# Everything except LLM evals (no API key needed)
uv run pytest evals/ -v -m "not llm"

# All evals (LLM tests auto-skip if no key)
uv run pytest evals/ -v
```

## Available Fixtures

| Fixture | Description |
|---------|-------------|
| `temp_project_dir` | Temp directory with tasks/, knowledge/, config.yaml |
| `create_task_file` | Factory to create task files in temp directory |
| `mock_project_dirs` | Patches server module to use temp directory |
| `load_fixture_file` | Load test fixtures from fixtures/ directory |
| `load_expected_output` | Load expected output JSON from expected/outputs/ |
| `sample_goals` | Sample goals for testing goal alignment |
| `anthropic_client` | Session-scoped Anthropic client (skips if no API key) |
| `llm_model` | Model for agent under test (env: `LLM_EVAL_MODEL`) |
| `judge_model` | Model for judge (env: `LLM_JUDGE_MODEL`) |
| `agents_md_content` | AGENTS.md content for LLM evals |
| `skill_md_content` | processing-backlog SKILL.md content |
| `goals_md_content` | GOALS.md content for LLM evals |

## Writing New Tests

```python
# In evals/test_*.py

def test_my_feature(mock_project_dirs, create_task_file):
    """Test description."""
    # Create test data
    task_path = create_task_file("test.md", {"title": "Test", "priority": "P1"}, "")

    # Run operation
    result = some_function()

    # Assert
    assert result == expected
```

## Maintenance

Update tests when:
- `config.yaml` keywords change → Update categorization tests and `conftest.py` test config
- Priority caps change → Update cap enforcement tests
- AGENTS.md requirements change → Update behavior tests
- `.claude/skills/processing-backlog/SKILL.md` instructions change → Update workflow compliance tests

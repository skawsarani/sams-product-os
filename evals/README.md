# PM Co-Pilot Evaluation Suite

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

## Directory Structure

```
evals/
├── README.md                  # This file
├── run_evals.py               # Test runner with options
├── conftest.py                # Shared pytest fixtures
├── test_mcp_server.py         # MCP server integration tests
├── test_workflows.py          # Workflow logic tests
├── test_agent_behavior.py     # Agent behavioral requirement tests
├── fixtures/
│   └── test-backlogs/
│       ├── basic.md
│       ├── mixed-items.md
│       └── behavioral-scenarios.md
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
- **Workflow compliance**: Verifies workflow files contain required instructions
- **Goal alignment**: Tasks should link to goals, orphan tasks flagged
- **Clarification requirements**: Ambiguous items trigger questions
- **Confirmation requirements**: Bulk operations, priority changes need confirmation

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
- `config.yaml` keywords change → Update categorization tests
- Priority caps change → Update cap enforcement tests
- AGENTS.md requirements change → Update behavior tests
- Workflow instructions change → Update compliance tests

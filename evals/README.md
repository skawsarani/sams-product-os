# SAMS PRODUCT OS Evaluation Suite

Validates that the agent, MCP server, and workflows work correctly after changes.

## Setup

```bash
uv sync --extra evals
```

## Quick Start

```bash
# Run all evals
uv run python evals/run_evals.py

# Run specific suites
uv run python evals/run_evals.py --mcp        # MCP server tests
uv run python evals/run_evals.py --workflows   # Workflow tests
uv run python evals/run_evals.py --behavior    # Agent behavior tests
uv run python evals/run_evals.py --llm         # LLM behavioral evals (needs ANTHROPIC_API_KEY)

# Or use pytest directly
uv run pytest evals/ -v
uv run pytest tools/mcp-servers/task-manager/test_server.py -v
```

## Test Suites

### MCP Server (`tools/mcp-servers/task-manager/test_server.py`)

Unit tests for the task-manager MCP server: ambiguity detection, clarification questions, task content generation, similarity calculation, auto-categorization, backlog parsing, config loading, archive/restore, status transitions, file integrity, and edge cases.

### Workflows (`evals/test_workflows.py`)

Backlog classification, deduplication, ambiguity detection, clarification question generation, auto-categorization from config keywords.

### Agent Behavior (`evals/test_agent_behavior.py`)

Behavioral contract tests: verifies `.claude/skills/process-backlog/SKILL.md` and `AGENTS.md` contain required instructions (user review, confirmation, goal linking, ambiguity resolution, priority caps). Tests goal alignment, clarification triggers, and confirmation requirements.

### LLM Behavioral (`evals/test_llm_behavior.py`)

Real Claude API calls graded by an LLM judge against rubrics. **Requires** `ANTHROPIC_API_KEY`. **Cost**: ~$0.10-0.20 per suite run.

| # | Scenario | Threshold |
|---|----------|-----------|
| 1 | Ambiguous item — asks clarification, doesn't create | 1.0 |
| 2 | Mixed backlog — categorizes, summarizes, waits for confirmation | 0.8 |
| 3 | Orphan task — flags no goal match | 1.0 |
| 4 | P0 cap exceeded — warns, shows existing, offers options | 0.8 |
| 5 | Duplicate detection — flags similar, asks user | 0.8 |
| 6 | Clear item with goal match — links goal, presents for review | 0.8 |

**Env vars:** `ANTHROPIC_API_KEY` (required), `LLM_EVAL_MODEL` (default: `claude-sonnet-4-20250514`), `LLM_JUDGE_MODEL` (default: `claude-sonnet-4-20250514`)

**Adding scenarios:** Create a new `EvalScenario` in `evals/fixtures/llm_scenarios/backlog_processing.py` and add it to `build_scenarios()`. Tests auto-discover via parametrize.

## Skill-Creator Evals

End-to-end evals in skill-creator compatible format, complementing the pytest suite above.

### `evals.json`

6 eval scenarios for `process-backlog` in the standard skill-creator schema (prompt + expected_output + expectations). Run via `/skill-creator` eval mode for grading and benchmarking.

### `trigger-eval.json`

20 trigger eval queries (10 should-trigger, 10 should-not-trigger) for optimizing the `process-backlog` description via skill-creator's description optimization flow.

### Two-Layer Strategy

| Layer | Format | Purpose | Cost |
|-------|--------|---------|------|
| **Unit/Integration** | pytest (`test_*.py`) | MCP server, workflows, behavioral contracts | Free (local) |
| **End-to-End** | skill-creator (`evals.json`) | Full skill execution with grading + benchmarking | ~$0.10-0.20/run |

## Directory Structure

```
evals/
├── README.md
├── evals.json                 # Skill-creator compatible eval definitions
├── trigger-eval.json          # Trigger eval queries for description optimization
├── run_evals.py               # Test runner with options
├── conftest.py                # Shared pytest fixtures
├── test_workflows.py          # Workflow logic tests
├── test_agent_behavior.py     # Agent behavioral requirement tests
├── test_llm_behavior.py       # LLM-in-the-loop behavioral evals
├── fixtures/
│   ├── test-backlogs/         # basic.md, mixed-items.md, behavioral-scenarios.md
│   └── llm_scenarios/
│       └── backlog_processing.py  # 6 eval scenarios + judge prompts
└── expected/
    └── outputs/               # basic.json, behavioral-scenarios.json
```

## Maintenance

Update tests when:
- `config.yaml` keywords change — update categorization tests and `conftest.py` test config
- Priority caps change — update cap enforcement tests
- `AGENTS.md` requirements change — update behavior tests
- `.claude/skills/process-backlog/SKILL.md` changes — update workflow compliance tests
- Skill description changes — rerun trigger evals via skill-creator
- New eval scenarios needed — add to both `evals.json` and `fixtures/llm_scenarios/`

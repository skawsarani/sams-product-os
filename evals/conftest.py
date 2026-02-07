"""
Shared pytest fixtures for PM Co-Pilot evaluation suite.

Provides common fixtures for:
- Temporary test directories with proper structure
- Test data loading (fixtures and expected outputs)
- Task file creation helpers
"""

import json
import sys
from pathlib import Path
from typing import Generator

import pytest
import yaml

# Add parent directory to path so we can import from tools/mcp-servers/task-manager
# tests/ -> evals/ -> project root
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "tools" / "mcp-servers" / "task-manager"))


# ============================================================================
# Path Fixtures
# ============================================================================


@pytest.fixture
def project_root() -> Path:
    """Return the project root directory."""
    return PROJECT_ROOT


@pytest.fixture
def fixtures_dir() -> Path:
    """Return the fixtures directory path."""
    return PROJECT_ROOT / "evals" / "fixtures"


@pytest.fixture
def expected_dir() -> Path:
    """Return the expected outputs directory path."""
    return PROJECT_ROOT / "evals" / "expected" / "outputs"


# ============================================================================
# Temporary Directory Fixtures
# ============================================================================


@pytest.fixture
def temp_project_dir(tmp_path: Path) -> Generator[Path, None, None]:
    """
    Create a temporary project directory with proper structure.

    Includes:
    - tasks/ directory
    - knowledge/ subdirectories
    - config.yaml with test configuration
    - Empty BACKLOG.md
    """
    # Create directory structure
    (tmp_path / "tasks").mkdir()
    (tmp_path / "knowledge" / "initiatives").mkdir(parents=True)
    (tmp_path / "knowledge" / "references").mkdir(parents=True)
    (tmp_path / "knowledge" / "notes").mkdir(parents=True)

    # Create default config.yaml
    config = {
        "categories": [
            "technical", "outreach", "research", "writing",
            "admin", "strategy", "stakeholder", "discovery"
        ],
        "priorities": ["P0", "P1", "P2", "P3"],
        "statuses": {"n": "not_started", "s": "started", "b": "blocked", "d": "done"},
        "deduplication": {
            "similarity_threshold": 0.6,
            "check_categories": True,
            "check_keywords": True,
        },
        "priority_caps": {"P0": 3, "P1": 7, "P2": 15, "P3": 999},
        "task_aging": {"prune_completed_after": 90, "flag_stale_after": 14},
        "category_keywords": {
            "technical": ["code", "api", "database", "deploy", "fix", "bug", "implement"],
            "outreach": ["email", "contact", "reach", "meeting", "call"],
            "research": ["research", "study", "learn", "investigate", "analyze"],
            "writing": ["write", "draft", "document", "blog", "article"],
            "admin": ["schedule", "organize", "expense", "invoice", "calendar"],
        },
    }

    with open(tmp_path / "config.yaml", "w") as f:
        yaml.dump(config, f)

    # Create empty BACKLOG.md
    (tmp_path / "BACKLOG.md").touch()

    yield tmp_path


@pytest.fixture
def temp_tasks_dir(temp_project_dir: Path) -> Path:
    """Return the tasks directory within the temp project."""
    return temp_project_dir / "tasks"


# ============================================================================
# Task Creation Fixtures
# ============================================================================


@pytest.fixture
def create_task_file(temp_tasks_dir: Path):
    """
    Factory fixture to create task files in the temp directory.

    Usage:
        def test_something(create_task_file):
            task_path = create_task_file("my-task.md", frontmatter, body)
    """
    def _create_task_file(
        filename: str,
        frontmatter: dict,
        body: str = ""
    ) -> Path:
        task_path = temp_tasks_dir / filename
        yaml_str = yaml.dump(frontmatter, default_flow_style=False, sort_keys=False)
        content = f"---\n{yaml_str}---\n\n{body}\n"
        task_path.write_text(content)
        return task_path

    return _create_task_file


# ============================================================================
# Test Data Loading Fixtures
# ============================================================================


@pytest.fixture
def load_fixture_file(fixtures_dir: Path):
    """
    Factory fixture to load fixture files.

    Usage:
        def test_something(load_fixture_file):
            content = load_fixture_file("test-backlogs/basic.md")
    """
    def _load_fixture(relative_path: str) -> str:
        filepath = fixtures_dir / relative_path
        if not filepath.exists():
            raise FileNotFoundError(f"Fixture file not found: {filepath}")
        return filepath.read_text()

    return _load_fixture


@pytest.fixture
def load_expected_output(expected_dir: Path):
    """
    Factory fixture to load expected output JSON files.

    Usage:
        def test_something(load_expected_output):
            expected = load_expected_output("basic.json")
    """
    def _load_expected(filename: str) -> dict:
        filepath = expected_dir / filename
        if not filepath.exists():
            raise FileNotFoundError(f"Expected output file not found: {filepath}")
        with open(filepath) as f:
            return json.load(f)

    return _load_expected


# ============================================================================
# Pytest Configuration
# ============================================================================


def pytest_configure(config):
    """Register custom markers."""
    config.addinivalue_line("markers", "slow: marks tests as slow")
    config.addinivalue_line("markers", "integration: marks integration tests")

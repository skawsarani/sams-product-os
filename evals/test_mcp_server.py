"""
MCP Server Integration Tests

Tests the task-manager MCP server tools work correctly:
- Task CRUD operations (create, read, update)
- Status transitions
- Priority cap enforcement
- Auto-categorization
- Similarity calculation
- Config loading

Run with: pytest evals/test_mcp_server.py -v
"""

import sys
from datetime import datetime
from pathlib import Path

import pytest

# Add tools/mcp-servers/task-manager to path for imports
# tests/ -> evals/ -> project root
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "tools" / "mcp-servers" / "task-manager"))

from server import (
    parse_yaml_frontmatter,
    write_task_file,
    get_all_tasks,
    get_task_by_file,
    auto_categorize,
    calculate_similarity,
    load_config,
)

import server


@pytest.fixture
def mock_project_dirs(temp_project_dir: Path, monkeypatch):
    """Mock the server module's PROJECT_ROOT and TASKS_DIR."""
    monkeypatch.setattr(server, "PROJECT_ROOT", temp_project_dir)
    monkeypatch.setattr(server, "TASKS_DIR", temp_project_dir / "tasks")
    monkeypatch.setattr(server, "CONFIG_FILE", temp_project_dir / "config.yaml")
    return temp_project_dir


class TestTaskCRUD:
    """Test basic task CRUD operations."""

    def test_create_task_file(self, mock_project_dirs: Path):
        """Create a task and verify file exists with correct content."""
        tasks_dir = mock_project_dirs / "tasks"
        task_file = tasks_dir / "test-task.md"

        frontmatter = {
            "title": "Test Task",
            "priority": "P1",
            "status": "n",
            "category": "technical",
            "keywords": ["test"],
            "created_date": datetime.now().isoformat(),
            "updated_date": datetime.now().isoformat(),
        }
        body = "## Context\nTest context."

        write_task_file(task_file, frontmatter, body)

        assert task_file.exists()
        content = task_file.read_text()
        assert "title: Test Task" in content
        assert "priority: P1" in content
        assert "## Context" in content

    def test_read_task_file(self, mock_project_dirs: Path, create_task_file):
        """Read a task file and verify data is correct."""
        frontmatter = {
            "title": "Read Test",
            "priority": "P2",
            "status": "s",
            "category": "research",
            "keywords": ["api", "research"],
        }
        create_task_file("read-test.md", frontmatter, "Body content.")

        task = get_task_by_file("read-test.md")

        assert task is not None
        assert task["title"] == "Read Test"
        assert task["priority"] == "P2"
        assert task["status"] == "s"
        assert task["category"] == "research"
        assert "api" in task["keywords"]

    def test_update_task_status(self, mock_project_dirs: Path, create_task_file):
        """Update task status and verify change."""
        frontmatter = {
            "title": "Status Update Test",
            "priority": "P1",
            "status": "n",
            "category": "technical",
        }
        task_path = create_task_file("status-test.md", frontmatter, "Body.")

        fm, body = parse_yaml_frontmatter(task_path)
        fm["status"] = "s"
        fm["updated_date"] = datetime.now().isoformat()
        write_task_file(task_path, fm, body)

        task = get_task_by_file("status-test.md")
        assert task["status"] == "s"

    def test_get_all_tasks(self, mock_project_dirs: Path, create_task_file):
        """Get all tasks and verify count."""
        create_task_file("task-1.md", {"title": "Task 1", "priority": "P1", "status": "n"}, "")
        create_task_file("task-2.md", {"title": "Task 2", "priority": "P2", "status": "s"}, "")
        create_task_file("task-3.md", {"title": "Task 3", "priority": "P0", "status": "b"}, "")

        tasks = get_all_tasks()

        assert len(tasks) == 3
        titles = [t["title"] for t in tasks]
        assert "Task 1" in titles
        assert "Task 2" in titles
        assert "Task 3" in titles

    def test_task_not_found(self, mock_project_dirs: Path):
        """Getting nonexistent task returns None."""
        task = get_task_by_file("nonexistent.md")
        assert task is None


class TestStatusTransitions:
    """Test valid status transitions."""

    @pytest.mark.parametrize("from_status,to_status", [
        ("n", "s"),  # not started -> started
        ("s", "b"),  # started -> blocked
        ("b", "s"),  # blocked -> started
        ("s", "d"),  # started -> done
        ("n", "d"),  # not started -> done (skip started)
        ("d", "n"),  # done -> not started (reopen)
    ])
    def test_status_transitions(
        self,
        mock_project_dirs: Path,
        create_task_file,
        from_status: str,
        to_status: str
    ):
        """Test all valid status transitions work."""
        frontmatter = {
            "title": f"Transition {from_status} to {to_status}",
            "priority": "P2",
            "status": from_status,
        }
        task_path = create_task_file(f"transition-{from_status}-{to_status}.md", frontmatter, "")

        fm, body = parse_yaml_frontmatter(task_path)
        fm["status"] = to_status
        write_task_file(task_path, fm, body)

        task = get_task_by_file(f"transition-{from_status}-{to_status}.md")
        assert task["status"] == to_status


class TestPriorityCaps:
    """Test priority cap enforcement."""

    def test_count_tasks_by_priority(self, mock_project_dirs: Path, create_task_file):
        """Count tasks by priority."""
        create_task_file("p0-1.md", {"title": "P0 1", "priority": "P0", "status": "n"}, "")
        create_task_file("p0-2.md", {"title": "P0 2", "priority": "P0", "status": "n"}, "")
        create_task_file("p1-1.md", {"title": "P1 1", "priority": "P1", "status": "n"}, "")
        create_task_file("p2-1.md", {"title": "P2 1", "priority": "P2", "status": "s"}, "")

        tasks = get_all_tasks()
        p0_count = len([t for t in tasks if t["priority"] == "P0"])
        p1_count = len([t for t in tasks if t["priority"] == "P1"])
        p2_count = len([t for t in tasks if t["priority"] == "P2"])

        assert p0_count == 2
        assert p1_count == 1
        assert p2_count == 1

    def test_priority_cap_check(self, mock_project_dirs: Path, create_task_file):
        """Verify we can check if cap would be exceeded."""
        config = load_config()
        caps = config["priority_caps"]

        # Create P0 tasks up to cap
        for i in range(caps["P0"]):
            create_task_file(f"p0-{i}.md", {"title": f"P0 {i}", "priority": "P0", "status": "n"}, "")

        tasks = get_all_tasks()
        p0_count = len([t for t in tasks if t["priority"] == "P0"])

        # Should be at or above cap
        assert p0_count >= caps["P0"]


class TestAutoCategorization:
    """Test auto-categorization based on keywords."""

    @pytest.fixture
    def config(self, mock_project_dirs: Path):
        """Load config for categorization tests."""
        return load_config()

    def test_technical_keywords(self, config: dict):
        """Technical keywords categorize as technical."""
        category = auto_categorize("Fix the API bug", "Database error in production", config)
        assert category == "technical"

    def test_outreach_keywords(self, config: dict):
        """Outreach keywords categorize as outreach."""
        category = auto_categorize("Email the client", "Schedule a call to discuss", config)
        assert category == "outreach"

    def test_research_keywords(self, config: dict):
        """Research keywords categorize as research."""
        category = auto_categorize("Research competitors", "Analyze market trends", config)
        assert category == "research"

    def test_writing_keywords(self, config: dict):
        """Writing keywords categorize as writing."""
        category = auto_categorize("Write blog post", "Draft the proposal document", config)
        assert category == "writing"

    def test_admin_keywords(self, config: dict):
        """Admin keywords categorize as admin."""
        category = auto_categorize("Schedule team meeting", "Organize calendar", config)
        assert category == "admin"

    def test_no_matching_keywords(self, config: dict):
        """Items without matching keywords return empty."""
        category = auto_categorize("Random unrelated task", "No keywords here", config)
        assert category == ""

    def test_case_insensitive(self, config: dict):
        """Auto-categorization is case-insensitive."""
        category = auto_categorize("FIX THE BUG", "IN THE API", config)
        assert category == "technical"


class TestSimilarityCalculation:
    """Test task similarity calculation."""

    @pytest.fixture
    def config(self, mock_project_dirs: Path):
        """Load config for similarity tests."""
        return load_config()

    def test_identical_tasks(self, config: dict):
        """Identical tasks have high similarity."""
        task1 = {"title": "Fix auth bug", "keywords": ["auth"], "category": "technical"}
        task2 = {"title": "Fix auth bug", "keywords": ["auth"], "category": "technical"}

        similarity = calculate_similarity(task1, task2, config)
        assert similarity >= 0.8

    def test_different_tasks(self, config: dict):
        """Different tasks have low similarity."""
        task1 = {"title": "Fix auth bug", "keywords": ["auth"], "category": "technical"}
        task2 = {"title": "Write blog post", "keywords": ["blog"], "category": "writing"}

        similarity = calculate_similarity(task1, task2, config)
        assert similarity < 0.3

    def test_similar_titles(self, config: dict):
        """Similar titles have medium similarity."""
        task1 = {"title": "Fix auth bug", "keywords": [], "category": "technical"}
        task2 = {"title": "Fix authentication bug", "keywords": [], "category": "technical"}

        similarity = calculate_similarity(task1, task2, config)
        assert 0.4 < similarity < 0.9

    def test_keyword_overlap_increases_similarity(self, config: dict):
        """Keyword overlap increases similarity."""
        task1 = {"title": "Task A", "keywords": ["auth", "bug"], "category": "technical"}
        task2 = {"title": "Task B", "keywords": ["auth", "security"], "category": "technical"}

        similarity_with_kw = calculate_similarity(task1, task2, config)

        task1_no_kw = {"title": "Task A", "keywords": [], "category": "technical"}
        task2_no_kw = {"title": "Task B", "keywords": [], "category": "technical"}

        similarity_without_kw = calculate_similarity(task1_no_kw, task2_no_kw, config)

        assert similarity_with_kw > similarity_without_kw


class TestConfigLoading:
    """Test configuration loading."""

    def test_config_loads(self, mock_project_dirs: Path):
        """Config loads without errors."""
        config = load_config()
        assert "priority_caps" in config

    def test_priority_caps_correct(self, mock_project_dirs: Path):
        """Priority caps have expected values."""
        config = load_config()

        assert config["priority_caps"]["P0"] == 3
        assert config["priority_caps"]["P1"] == 7
        assert config["priority_caps"]["P2"] == 15
        assert config["priority_caps"]["P3"] == 999

    def test_category_keywords_exist(self, mock_project_dirs: Path):
        """All 8 categories have keywords defined."""
        config = load_config()
        expected = ["technical", "outreach", "research", "writing", "admin"]

        for cat in expected:
            assert cat in config["category_keywords"]


class TestTaskFileIntegrity:
    """Test task file integrity after operations."""

    def test_multiple_updates_preserve_content(self, mock_project_dirs: Path, create_task_file):
        """Multiple updates preserve all content."""
        original_body = """## Context
Important context here.

## Technical Details
- Tech 1
- Tech 2

## Progress Log
- 2024-01-15: Created
"""
        frontmatter = {
            "title": "Integrity Test",
            "priority": "P1",
            "status": "n",
            "category": "technical",
            "keywords": ["test", "integrity"],
        }
        task_path = create_task_file("integrity-test.md", frontmatter, original_body)

        # Multiple status updates
        for status in ["s", "b", "s", "d"]:
            fm, body = parse_yaml_frontmatter(task_path)
            fm["status"] = status
            fm["updated_date"] = datetime.now().isoformat()
            write_task_file(task_path, fm, body)

        # Verify content preserved
        final_fm, final_body = parse_yaml_frontmatter(task_path)
        assert final_fm["title"] == "Integrity Test"
        assert final_fm["keywords"] == ["test", "integrity"]
        assert "## Context" in final_body
        assert "## Technical Details" in final_body
        assert "## Progress Log" in final_body

    def test_special_characters_preserved(self, mock_project_dirs: Path, create_task_file):
        """Special characters are preserved through updates."""
        body = """## Context
Code snippet: `const x = { key: "value" };`

URL: https://example.com/path?param=value&other=123

Quote: "It's working!"
"""
        frontmatter = {
            "title": 'Task with "quotes" and colons:',
            "priority": "P1",
            "status": "n",
        }
        task_path = create_task_file("special-chars.md", frontmatter, body)

        fm, read_body = parse_yaml_frontmatter(task_path)
        fm["status"] = "s"
        write_task_file(task_path, fm, read_body)

        final_fm, final_body = parse_yaml_frontmatter(task_path)
        assert "https://example.com" in final_body
        assert "const x = { key:" in final_body

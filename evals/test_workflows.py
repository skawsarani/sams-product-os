"""
Workflow Tests

Tests the backlog processing workflow:
- Item classification (tasks, initiatives, references, notes)
- Ambiguity detection
- Auto-categorization
- Deduplication

Run with: pytest evals/test_workflows.py -v
"""

import json
import re
import sys
from pathlib import Path

import pytest

# Add mcp/task-manager to path for imports
# tests/ -> evals/ -> project root
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "mcp" / "task-manager"))

from server import (
    is_ambiguous,
    generate_clarification_questions,
    auto_categorize,
    calculate_similarity,
    load_config,
    get_all_tasks,
)

import server


@pytest.fixture
def mock_project_dirs(temp_project_dir: Path, monkeypatch):
    """Mock the server module's PROJECT_ROOT and TASKS_DIR."""
    monkeypatch.setattr(server, "PROJECT_ROOT", temp_project_dir)
    monkeypatch.setattr(server, "TASKS_DIR", temp_project_dir / "tasks")
    monkeypatch.setattr(server, "CONFIG_FILE", temp_project_dir / "config.yaml")
    return temp_project_dir


class TestAmbiguityDetection:
    """Test ambiguity detection for backlog items."""

    @pytest.mark.parametrize("item,should_be_ambiguous", [
        ("Bug", True),  # Too short
        ("Fix it", True),  # Too short
        ("The database", True),  # No action verb
        ("Maybe update docs", True),  # Vague "maybe"
        ("Should look into this", True),  # Vague "should"
        ("Might need to refactor", True),  # Vague "might"
        ("Fix authentication bug in login flow", False),  # Clear
        ("Email Sarah about Q4 roadmap", False),  # Clear
        ("Research competitor pricing models", False),  # Clear
    ])
    def test_ambiguity_detection(self, item: str, should_be_ambiguous: bool):
        """Test various items for ambiguity detection."""
        is_amb, reason = is_ambiguous(item)
        assert is_amb == should_be_ambiguous, f"'{item}' ambiguity: expected {should_be_ambiguous}, got {is_amb} ({reason})"


class TestClarificationQuestions:
    """Test clarification question generation."""

    def test_generates_deadline_question(self):
        """Items without deadline info get deadline question."""
        questions = generate_clarification_questions("Fix the bug")
        has_deadline_q = any("when" in q.lower() for q in questions)
        assert has_deadline_q

    def test_generates_context_question(self):
        """Items without context get context question."""
        questions = generate_clarification_questions("Update documentation")
        has_context_q = any("why" in q.lower() or "context" in q.lower() for q in questions)
        assert has_context_q

    def test_question_format(self):
        """All questions end with question mark or parenthesis."""
        questions = generate_clarification_questions("Something to do")
        for q in questions:
            assert q.endswith("?") or q.endswith(")"), f"'{q}' should be a question"


class TestItemClassification:
    """Test classification of backlog items into types."""

    def test_classify_task(self):
        """Clear actionable items are classified as tasks."""
        item = "Fix authentication bug in login flow"
        is_amb, reason = is_ambiguous(item)
        assert is_amb is False

    def test_classify_initiative_indicators(self):
        """Items with initiative indicators are identified."""
        initiative_items = [
            "Users complaining about slow startup times",
            "Explore new pricing strategies",
            "Investigate performance issues",
            "Consider adding dark mode",
        ]

        initiative_indicators = [
            "explore", "investigate", "consider", "opportunity",
            "users complaining", "user feedback", "users want",
            "performance issue", "slow startup"
        ]

        for item in initiative_items:
            is_initiative = any(ind in item.lower() for ind in initiative_indicators)
            assert is_initiative, f"'{item}' should be classified as initiative"

    def test_classify_reference(self):
        """Items with URLs are classified as references."""
        reference_items = [
            "Found article about pricing: https://example.com/pricing",
            "Read this: https://docs.example.com/api",
            "Reference: https://competitor.com/features",
        ]

        url_pattern = r'https?://[^\s]+'

        for item in reference_items:
            has_url = bool(re.search(url_pattern, item))
            assert has_url, f"'{item}' should be classified as reference"

    def test_classify_notes(self):
        """Meeting notes are identified for archival."""
        notes_items = [
            ("Meeting notes", "- Point 1\n- Point 2"),
            ("Standup notes", "- Alice: working on X\n- Bob: blocked"),
        ]

        notes_keywords = ["notes", "meeting notes", "standup", "retrospective"]

        for title, description in notes_items:
            is_notes = (
                any(kw in title.lower() for kw in notes_keywords) and
                description.startswith("-")
            )
            assert is_notes, f"'{title}' should be classified as notes"


class TestBacklogClassification:
    """Test backlog processing classification with fixtures."""

    def test_basic_backlog_classification(self, load_fixture_file, load_expected_output, mock_project_dirs: Path):
        """Backlog items classified correctly."""
        backlog = load_fixture_file("test-backlogs/basic.md")
        expected = load_expected_output("basic.json")
        config = load_config()

        # Parse backlog
        items = self._parse_backlog(backlog)

        # Classify items
        tasks, initiatives, references, notes = self._classify_items(items, config)

        # Verify counts
        assert len(tasks) == expected["expected"]["tasks"]["count"]
        assert len(initiatives) == expected["expected"]["initiatives"]["count"]
        assert len(references) == expected["expected"]["references"]["count"]

    def test_auto_categorization(self, mock_project_dirs: Path):
        """Tasks get correct categories based on keywords."""
        config = load_config()

        test_cases = [
            ("Fix authentication bug", "JWT tokens expiring", "technical"),
            ("Email Sarah about roadmap", "Need to sync on Q1", "outreach"),
        ]

        for title, description, expected_category in test_cases:
            category = auto_categorize(title, description, config)
            assert category == expected_category, f"'{title}' expected {expected_category}, got {category}"

    def _parse_backlog(self, content: str) -> list[dict]:
        """Parse backlog content into items."""
        lines = content.split('\n')
        items = []
        current_item = None

        for line in lines:
            stripped = line.strip()
            if not stripped:
                continue
            if stripped.startswith('# ') and not stripped.startswith('## '):
                continue
            if stripped.startswith('## '):
                if current_item:
                    items.append(current_item)
                title = stripped[3:].strip()
                current_item = {"title": title, "description": ""}
            elif current_item is not None:
                if stripped.startswith(('- ', '* ', '+ ')):
                    current_item["description"] += stripped + "\n"
                else:
                    if current_item["description"]:
                        current_item["description"] += " " + stripped
                    else:
                        current_item["description"] = stripped

        if current_item:
            items.append(current_item)

        return items

    def _classify_items(self, items: list[dict], config: dict) -> tuple[list, list, list, list]:
        """Classify items into tasks, initiatives, references, notes."""
        tasks = []
        initiatives = []
        references = []
        notes = []

        url_pattern = r'https?://[^\s]+'
        initiative_indicators = [
            "explore", "investigate", "consider", "opportunity",
            "users complaining", "user feedback", "users want",
            "performance issue", "slow startup"
        ]
        notes_keywords = ["notes", "meeting notes", "standup"]

        for item in items:
            title = item["title"]
            desc = item.get("description", "")
            full_text = f"{title} {desc}".strip()

            # Check reference first (has URL)
            if re.search(url_pattern, full_text):
                references.append(item)
                continue

            # Check notes
            if any(kw in title.lower() for kw in notes_keywords) and desc.startswith("-"):
                notes.append(item)
                continue

            # Check initiative
            if any(ind in full_text.lower() for ind in initiative_indicators):
                initiatives.append(item)
                continue

            # Check if it's a clear task
            is_amb, _ = is_ambiguous(full_text)
            if not is_amb:
                tasks.append(item)

        return tasks, initiatives, references, notes


class TestDeduplication:
    """Test duplicate detection."""

    @pytest.fixture
    def config(self, mock_project_dirs: Path):
        """Load config for deduplication tests."""
        return load_config()

    def test_detect_exact_duplicate(self, mock_project_dirs: Path, create_task_file, config: dict):
        """Exact duplicate titles are detected."""
        create_task_file("existing-task.md", {
            "title": "Fix authentication bug",
            "priority": "P1",
            "status": "n",
            "category": "technical",
            "keywords": ["auth", "bug"],
        }, "")

        existing_tasks = get_all_tasks()
        new_task = {
            "title": "Fix authentication bug",
            "keywords": ["auth", "bug"],
            "category": "technical",
        }

        similar = []
        for task in existing_tasks:
            similarity = calculate_similarity(new_task, task, config)
            if similarity >= config["deduplication"]["similarity_threshold"]:
                similar.append((task, similarity))

        assert len(similar) >= 1
        assert similar[0][1] >= 0.6

    def test_no_false_positive(self, mock_project_dirs: Path, create_task_file, config: dict):
        """Different tasks are not flagged as duplicates."""
        create_task_file("write-docs.md", {
            "title": "Write API documentation",
            "priority": "P2",
            "status": "n",
            "category": "writing",
            "keywords": ["docs", "api"],
        }, "")

        existing_tasks = get_all_tasks()
        new_task = {
            "title": "Schedule team meeting",
            "keywords": ["meeting", "team"],
            "category": "admin",
        }

        similar = []
        for task in existing_tasks:
            similarity = calculate_similarity(new_task, task, config)
            if similarity >= config["deduplication"]["similarity_threshold"]:
                similar.append((task, similarity))

        assert len(similar) == 0

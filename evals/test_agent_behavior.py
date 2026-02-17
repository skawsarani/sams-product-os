"""
Agent Behavioral Requirement Tests

Tests that the agent follows behavioral requirements from AGENTS.md and workflows:
- Present findings for user review before creating anything
- Wait for user confirmation before creating tasks/initiatives
- Link tasks to goals from GOALS.md
- Ask for clarification on ambiguous items
- Follow interaction style guidelines

These tests validate behavioral contracts, not just function outputs.

Run with: pytest evals/test_agent_behavior.py -v
"""

import re
import sys
from pathlib import Path
from typing import Optional

import pytest

# tests/ -> evals/ -> project root
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "tools" / "mcp-servers" / "task-manager"))

from server import is_ambiguous, generate_clarification_questions


# ============================================================================
# Fixtures
# ============================================================================


@pytest.fixture
def agents_md() -> str:
    """Load AGENTS.md content."""
    agents_file = PROJECT_ROOT / "AGENTS.md"
    if not agents_file.exists():
        pytest.skip("AGENTS.md not found")
    return agents_file.read_text()


@pytest.fixture
def process_backlog_workflow() -> str:
    """Load process-backlog skill content."""
    skill_file = PROJECT_ROOT / "skills" / "process-backlog" / "SKILL.md"
    if not skill_file.exists():
        pytest.skip("process-backlog SKILL.md not found")
    return skill_file.read_text()


@pytest.fixture
def goals_md() -> str:
    """Load GOALS.md content."""
    goals_file = PROJECT_ROOT / "GOALS.md"
    if not goals_file.exists():
        pytest.skip("GOALS.md not found")
    return goals_file.read_text()


@pytest.fixture
def sample_goals() -> list[dict]:
    """Sample goals for testing goal alignment."""
    return [
        {
            "name": "Improve Developer Experience",
            "description": "Reduce friction in daily dev workflows",
            "keywords": ["developer", "dx", "tooling", "automation"],
        },
        {
            "name": "Launch Mobile App",
            "description": "Ship iOS and Android apps by Q2",
            "keywords": ["mobile", "ios", "android", "app"],
        },
        {
            "name": "Reduce Churn",
            "description": "Decrease customer churn rate by 20%",
            "keywords": ["churn", "retention", "customer", "engagement"],
        },
    ]


# ============================================================================
# Workflow Compliance Tests
# ============================================================================


class TestWorkflowCompliance:
    """Test that workflow files contain required behavioral instructions."""

    def test_process_backlog_requires_user_review(self, process_backlog_workflow: str):
        """Workflow must instruct agent to present findings before creating."""
        review_patterns = [
            r"present.*findings.*review",
            r"present.*for.*user.*review",
            r"before.*creating",
            r"never.*auto.?create",
        ]

        content_lower = process_backlog_workflow.lower()
        has_review_requirement = any(
            re.search(pattern, content_lower) for pattern in review_patterns
        )

        assert has_review_requirement, (
            "Workflow must instruct agent to present findings for user review before creating"
        )

    def test_process_backlog_requires_confirmation(self, process_backlog_workflow: str):
        """Workflow must require user confirmation before creating items."""
        confirmation_patterns = [
            r"wait.*for.*user.*response",
            r"get.*confirmation",
            r"ask.*proceed",
            r"wait.*for.*confirmation",
        ]

        content_lower = process_backlog_workflow.lower()
        has_confirmation = any(
            re.search(pattern, content_lower) for pattern in confirmation_patterns
        )

        assert has_confirmation, (
            "Workflow must require user confirmation before creating items"
        )

    def test_process_backlog_requires_goal_linking(self, process_backlog_workflow: str):
        """Workflow must instruct linking tasks to goals."""
        goal_patterns = [
            r"link.*to.*goal",
            r"goal.*from.*goals\.md",
            r"reference.*goal",
            r"relevant.*goal",
        ]

        content_lower = process_backlog_workflow.lower()
        has_goal_linking = any(
            re.search(pattern, content_lower) for pattern in goal_patterns
        )

        assert has_goal_linking, (
            "Workflow must instruct agent to link tasks to goals from GOALS.md"
        )

    def test_process_backlog_requires_ambiguity_resolution(self, process_backlog_workflow: str):
        """Workflow must instruct resolving ambiguous items."""
        ambiguity_patterns = [
            r"resolve.*ambigu",
            r"clarif",
            r"vague.*item",
            r"ask.*clarification",
        ]

        content_lower = process_backlog_workflow.lower()
        has_ambiguity_handling = any(
            re.search(pattern, content_lower) for pattern in ambiguity_patterns
        )

        assert has_ambiguity_handling, (
            "Workflow must instruct agent to resolve ambiguous items"
        )

    def test_process_backlog_enforces_priority_caps(self, process_backlog_workflow: str):
        """Workflow must mention priority cap enforcement."""
        priority_patterns = [
            r"priority.*cap",
            r"enforce.*priority",
            r"check.*cap",
            r"p0.*max",
        ]

        content_lower = process_backlog_workflow.lower()
        has_priority_enforcement = any(
            re.search(pattern, content_lower) for pattern in priority_patterns
        )

        assert has_priority_enforcement, (
            "Workflow must instruct agent to enforce priority caps"
        )


class TestAgentsMdCompliance:
    """Test that AGENTS.md contains required behavioral guidelines."""

    def test_agents_md_has_core_rules(self, agents_md: str):
        """AGENTS.md must define core behavioral rules."""
        assert "core rules" in agents_md.lower(), (
            "AGENTS.md must have Core Rules section"
        )

    def test_agents_md_requires_clarification(self, agents_md: str):
        """AGENTS.md must instruct asking for clarification."""
        clarification_patterns = [
            r"ask.*clarification",
            r"stop.*and.*ask",
            r"lacks.*context.*ask",
        ]

        content_lower = agents_md.lower()
        has_clarification = any(
            re.search(pattern, content_lower) for pattern in clarification_patterns
        )

        assert has_clarification, (
            "AGENTS.md must instruct agent to ask for clarification when needed"
        )

    def test_agents_md_references_goals(self, agents_md: str):
        """AGENTS.md must reference GOALS.md for alignment."""
        assert "goals.md" in agents_md.lower(), (
            "AGENTS.md must reference GOALS.md for task alignment"
        )

    def test_agents_md_defines_priority_system(self, agents_md: str):
        """AGENTS.md must define the priority system."""
        priority_patterns = [
            r"p0.*p1.*p2.*p3",
            r"priorities.*p0",
            r"p0.*max.*3",
        ]

        content_lower = agents_md.lower()
        has_priority_system = any(
            re.search(pattern, content_lower) for pattern in priority_patterns
        )

        assert has_priority_system, (
            "AGENTS.md must define the priority system (P0-P3)"
        )


# ============================================================================
# Goal Alignment Tests
# ============================================================================


class TestGoalAlignment:
    """Test goal alignment requirements for tasks."""

    def test_task_should_reference_goal(self, sample_goals: list[dict]):
        """Tasks should be linkable to at least one goal."""
        # Tasks that clearly align with goals (using explicit keywords)
        aligned_tasks = [
            ("Fix developer tooling automation", "Improve Developer Experience"),
            ("Fix iOS mobile app crash on login", "Launch Mobile App"),
            ("Add customer retention churn dashboard", "Reduce Churn"),
        ]

        for task_title, expected_goal in aligned_tasks:
            matching_goal = find_matching_goal(task_title, sample_goals)
            assert matching_goal is not None, (
                f"Task '{task_title}' should match goal '{expected_goal}'"
            )

    def test_orphan_task_detection(self, sample_goals: list[dict]):
        """Tasks that don't align with any goal should be flagged."""
        orphan_tasks = [
            "Reorganize office supplies",
            "Update personal LinkedIn",
            "Random cleanup task",
        ]

        for task_title in orphan_tasks:
            matching_goal = find_matching_goal(task_title, sample_goals)
            # These should NOT match any goal - agent should ask about alignment
            assert matching_goal is None, (
                f"Orphan task '{task_title}' should not match any goal"
            )

    def test_goal_keywords_extraction(self):
        """Goal keywords should be extractable for matching."""
        goal = {
            "name": "Improve Developer Experience",
            "description": "Reduce friction in daily dev workflows by improving tooling",
            "keywords": ["developer", "dx", "tooling"],
        }

        # Extract keywords from goal
        all_keywords = set(goal.get("keywords", []))
        all_keywords.update(goal["name"].lower().split())
        all_keywords.update(goal["description"].lower().split())

        assert "developer" in all_keywords
        assert "tooling" in all_keywords
        assert "friction" in all_keywords


# ============================================================================
# Clarification Requirement Tests
# ============================================================================


class TestClarificationRequirements:
    """Test when agent should ask for clarification."""

    @pytest.mark.parametrize("item,should_clarify,reason", [
        # Should clarify - too short (< 10 chars)
        ("Fix it", True, "Too short"),
        ("Bug", True, "Too short"),

        # Should clarify - vague language detected
        ("Do something about performance", True, "Contains 'something'"),
        ("Maybe refactor the code", True, "Contains 'maybe'"),
        ("Should look into this issue", True, "Contains 'should'"),

        # Should NOT clarify - clear enough
        ("Fix authentication bug in login API", False, "Clear action and target"),
        ("Email Sarah about Q4 roadmap by Friday", False, "Clear action, target, deadline"),
        ("Research competitor pricing models", False, "Clear research task"),
        ("Deploy v2.1 to staging environment", False, "Clear deployment action"),
    ])
    def test_clarification_needed(self, item: str, should_clarify: bool, reason: str):
        """Test items that should/shouldn't require clarification."""
        is_amb, _ = is_ambiguous(item)

        assert is_amb == should_clarify, (
            f"'{item}' clarification={is_amb}, expected={should_clarify}. Reason: {reason}"
        )

    @pytest.mark.parametrize("item,reason", [
        ("Update the thing", "Unclear what 'thing' refers to"),
        ("Fix the issue", "No specific issue identified"),
        ("Handle that problem", "Vague reference"),
    ])
    def test_vague_targets_need_clarification(self, item: str, reason: str):
        """Items with vague targets should require clarification."""
        is_amb, _ = is_ambiguous(item)
        assert is_amb, f"'{item}' should be flagged as ambiguous: {reason}"

    def test_clarification_questions_are_actionable(self):
        """Clarification questions should be specific and actionable."""
        vague_items = [
            "Fix the bug",
            "Update documentation",
            "Something about users",
        ]

        for item in vague_items:
            questions = generate_clarification_questions(item)

            assert len(questions) > 0, f"Should generate questions for '{item}'"

            # Questions should be actual questions
            for q in questions:
                assert q.endswith("?") or q.endswith(")"), (
                    f"'{q}' should be a question"
                )

            # Should ask about at least one of: what, when, why
            question_text = " ".join(questions).lower()
            has_useful_question = any(
                word in question_text
                for word in ["what", "when", "why", "which", "how", "who"]
            )
            assert has_useful_question, (
                f"Questions for '{item}' should include what/when/why/which/how"
            )

    def test_missing_deadline_triggers_question(self):
        """Items without deadline should get deadline question."""
        items_without_deadline = [
            "Write the report",
            "Review the PR",
            "Send the email",
        ]

        for item in items_without_deadline:
            questions = generate_clarification_questions(item)
            has_deadline_q = any("when" in q.lower() for q in questions)
            assert has_deadline_q, f"'{item}' should trigger deadline question"

    def test_missing_context_triggers_question(self):
        """Items without context should get context question."""
        items_without_context = [
            "Fix the bug",
            "Update the config",
        ]

        for item in items_without_context:
            questions = generate_clarification_questions(item)
            has_context_q = any(
                "why" in q.lower() or "context" in q.lower() or "goal" in q.lower()
                for q in questions
            )
            assert has_context_q, f"'{item}' should trigger context question"


# ============================================================================
# Confirmation Before Action Tests
# ============================================================================


class TestConfirmationBeforeAction:
    """Test scenarios where confirmation is required before action."""

    def test_bulk_creation_requires_confirmation(self):
        """Creating multiple items at once should require confirmation."""
        backlog_items = [
            {"title": "Task 1", "type": "task"},
            {"title": "Task 2", "type": "task"},
            {"title": "Initiative 1", "type": "initiative"},
        ]

        # More than 1 item = requires confirmation
        requires_confirmation = len(backlog_items) > 1
        assert requires_confirmation, "Creating multiple items should require confirmation"

    def test_priority_change_requires_confirmation(self):
        """Changing task priority should be confirmed."""
        scenarios = [
            {"from": "P3", "to": "P0", "requires_confirmation": True},
            {"from": "P2", "to": "P1", "requires_confirmation": True},
            {"from": "P1", "to": "P2", "requires_confirmation": False},  # Downgrade ok
        ]

        for scenario in scenarios:
            # Upgrading priority (lower number = higher priority) needs confirmation
            from_num = int(scenario["from"][1])
            to_num = int(scenario["to"][1])
            is_upgrade = to_num < from_num

            assert is_upgrade == scenario["requires_confirmation"], (
                f"Priority change {scenario['from']} -> {scenario['to']} "
                f"confirmation expected: {scenario['requires_confirmation']}"
            )

    def test_near_cap_requires_warning(self):
        """Creating task when near priority cap should warn user."""
        caps = {"P0": 3, "P1": 7, "P2": 15, "P3": 999}

        scenarios = [
            {"priority": "P0", "current_count": 2, "should_warn": True},
            {"priority": "P0", "current_count": 3, "should_warn": True},  # At cap
            {"priority": "P1", "current_count": 5, "should_warn": False},
            {"priority": "P1", "current_count": 6, "should_warn": True},
        ]

        for scenario in scenarios:
            priority = scenario["priority"]
            count = scenario["current_count"]
            cap = caps[priority]

            # Warn if within 1 of cap or at/over cap
            should_warn = count >= cap - 1

            assert should_warn == scenario["should_warn"], (
                f"Priority {priority} with {count}/{cap} tasks: "
                f"warn expected={scenario['should_warn']}, got={should_warn}"
            )


# ============================================================================
# Behavioral Scenario Tests
# ============================================================================


class TestBehavioralScenarios:
    """Test complete behavioral scenarios."""

    def test_ambiguous_item_flow(self):
        """
        Scenario: User adds ambiguous item to backlog
        Expected: Agent should ask for clarification, NOT create task
        """
        # Use an item that current server detects as ambiguous (vague language)
        item = "Maybe fix something"

        # Step 1: Detect ambiguity
        is_amb, reason = is_ambiguous(item)
        assert is_amb, f"Item should be detected as ambiguous. Got: {reason}"

        # Step 2: Generate clarification questions
        questions = generate_clarification_questions(item)
        assert len(questions) > 0, "Should generate clarification questions"

        # Step 3: Agent should NOT proceed to create task
        # (This is a behavioral contract - agent must ask first)
        should_create = not is_amb
        assert not should_create, "Agent should NOT create task for ambiguous item"

    def test_clear_item_with_goal_flow(self, sample_goals: list[dict]):
        """
        Scenario: User adds clear item that aligns with a goal
        Expected: Agent should present with goal reference, ask confirmation
        """
        # Use explicit keywords that match goal keywords
        item = "Fix developer tooling for better automation"

        # Step 1: Item should not be ambiguous
        is_amb, _ = is_ambiguous(item)
        assert not is_amb, "Clear item should not be ambiguous"

        # Step 2: Should match a goal
        matching_goal = find_matching_goal(item, sample_goals)
        assert matching_goal is not None, "Should find matching goal"
        assert matching_goal["name"] == "Improve Developer Experience"

        # Step 3: Agent should present findings WITH goal reference
        # (Behavioral contract: include goal in presentation)

    def test_orphan_task_flow(self, sample_goals: list[dict]):
        """
        Scenario: User adds task that doesn't align with any goal
        Expected: Agent should flag this and ask about goal alignment
        """
        item = "Reorganize the file cabinet"

        # Step 1: No matching goal
        matching_goal = find_matching_goal(item, sample_goals)
        assert matching_goal is None, "Should not match any goal"

        # Step 2: Agent should ask about goal alignment
        # (Behavioral contract: ask when task doesn't support goals)
        should_ask_about_goals = matching_goal is None
        assert should_ask_about_goals, "Agent should ask about goal alignment"


# ============================================================================
# Helper Functions
# ============================================================================


def find_matching_goal(task_title: str, goals: list[dict]) -> Optional[dict]:
    """
    Find a goal that matches the given task title.
    Returns the matching goal or None.
    """
    task_words = set(task_title.lower().split())

    best_match = None
    best_score = 0

    for goal in goals:
        # Get all keywords for this goal
        goal_keywords = set(k.lower() for k in goal.get("keywords", []))
        goal_keywords.update(goal["name"].lower().split())
        goal_keywords.update(goal.get("description", "").lower().split())

        # Remove common words
        stop_words = {"the", "a", "an", "to", "for", "by", "in", "on", "and", "or"}
        goal_keywords -= stop_words
        task_words_clean = task_words - stop_words

        # Calculate overlap
        overlap = len(goal_keywords & task_words_clean)

        if overlap > best_score:
            best_score = overlap
            best_match = goal

    # Require at least 2 matching keywords
    if best_score >= 2:
        return best_match

    return None


def requires_confirmation(action: str, context: dict) -> bool:
    """
    Determine if an action requires user confirmation.

    Args:
        action: The action being taken (create, update, delete, etc.)
        context: Context about the action (count, priority, etc.)

    Returns:
        True if confirmation is required
    """
    # Always confirm destructive actions
    if action in ["delete", "archive", "clear"]:
        return True

    # Confirm bulk operations
    if context.get("count", 1) > 1:
        return True

    # Confirm priority upgrades
    if action == "update_priority":
        from_num = int(context.get("from_priority", "P3")[1])
        to_num = int(context.get("to_priority", "P3")[1])
        if to_num < from_num:  # Upgrading (P2 -> P1)
            return True

    # Confirm when near priority cap
    if action == "create":
        priority = context.get("priority", "P3")
        current_count = context.get("current_count", 0)
        caps = {"P0": 3, "P1": 7, "P2": 15, "P3": 999}
        cap = caps.get(priority, 999)
        if current_count >= cap - 1:
            return True

    return False

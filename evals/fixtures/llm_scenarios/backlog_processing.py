"""
LLM eval scenarios for backlog processing behavior.

Each scenario tests a behavioral contract from SKILL.md by giving Claude
a realistic prompt and grading the response against a rubric.
"""

from dataclasses import dataclass, field


@dataclass
class GradingCriterion:
    """A single criterion for grading an agent response."""
    name: str
    description: str
    weight: float = 1.0


@dataclass
class EvalScenario:
    """A complete eval scenario with prompt, criteria, and thresholds."""
    id: str
    name: str
    description: str
    system_prompt: str  # Assembled at runtime from AGENTS.md + SKILL.md
    user_message: str
    criteria: list[GradingCriterion] = field(default_factory=list)
    fail_if_present: list[str] = field(default_factory=list)
    pass_threshold: float = 0.8


# ============================================================================
# Judge Prompt
# ============================================================================

JUDGE_SYSTEM_PROMPT = """\
You are an eval judge. You grade an AI agent's response against a rubric.

For each criterion, score 1 (met) or 0 (not met). Be strict — partial credit is not allowed.
If a fail_if_present phrase appears in the response, that criterion automatically scores 0.

Respond with ONLY valid JSON in this exact format:
{
  "criteria_scores": {
    "<criterion_name>": {"score": 0 or 1, "reason": "brief explanation"}
  },
  "overall_notes": "one sentence summary"
}
"""

JUDGE_USER_TEMPLATE = """\
## Agent Response to Grade

{agent_response}

## Grading Rubric

{rubric}

## Fail-if-present phrases
{fail_phrases}

Grade the response. Return ONLY JSON.
"""


# ============================================================================
# Scenario Definitions
# ============================================================================

def build_scenarios() -> list[EvalScenario]:
    """Return all eval scenarios. system_prompt is filled at test time."""

    return [
        # ------------------------------------------------------------------
        # 1. Ambiguous item — agent must ask, not create
        # ------------------------------------------------------------------
        EvalScenario(
            id="ambiguous_item",
            name="Ambiguous backlog item",
            description="Agent receives a vague item and should ask for clarification instead of creating a task.",
            system_prompt="",  # filled at runtime
            user_message=(
                "I just added this to my backlog:\n\n"
                "```\n- Fix the thing\n```\n\n"
                "Can you process this?"
            ),
            criteria=[
                GradingCriterion(
                    "asks_clarification",
                    "Agent asks the user for clarification about what 'the thing' refers to",
                ),
                GradingCriterion(
                    "does_not_create_task",
                    "Agent does NOT create a task or say it will create one",
                ),
                GradingCriterion(
                    "identifies_ambiguity",
                    "Agent explicitly flags the item as vague or ambiguous",
                ),
            ],
            fail_if_present=["task created", "I've created", "I created"],
            pass_threshold=1.0,
        ),

        # ------------------------------------------------------------------
        # 2. Mixed backlog — categorize, summarize, wait for confirmation
        # ------------------------------------------------------------------
        EvalScenario(
            id="mixed_backlog",
            name="Mixed backlog items",
            description="Agent processes a backlog with task, initiative, reference, and ambiguous items.",
            system_prompt="",
            user_message=(
                "Here's my backlog to process:\n\n"
                "```\n"
                "- Email Sarah about Q4 roadmap review by Friday\n"
                "- Enterprise SSO — we should think about this strategically\n"
                "- https://stripe.com/docs/api — good API doc reference\n"
                "- Fix the thing\n"
                "```\n\n"
                "Process these please."
            ),
            criteria=[
                GradingCriterion(
                    "categorizes_items",
                    "Agent categorizes items into tasks, initiatives, references, and ambiguous",
                ),
                GradingCriterion(
                    "presents_summary",
                    "Agent presents a structured summary or table before taking action",
                ),
                GradingCriterion(
                    "waits_for_confirmation",
                    "Agent asks the user how to proceed or waits for confirmation",
                ),
                GradingCriterion(
                    "does_not_create",
                    "Agent does NOT create any tasks or files without user approval",
                ),
            ],
            fail_if_present=["task created", "I've created", "file created"],
            pass_threshold=0.8,
        ),

        # ------------------------------------------------------------------
        # 3. Orphan task — no goal match, should flag
        # ------------------------------------------------------------------
        EvalScenario(
            id="orphan_task",
            name="Orphan task with no goal alignment",
            description="Agent receives a task that doesn't align with any goal in GOALS.md.",
            system_prompt="",
            user_message=(
                "Process this backlog item:\n\n"
                "```\n- Reorganize office supplies and restock printer paper\n```"
            ),
            criteria=[
                GradingCriterion(
                    "flags_no_goal",
                    "Agent flags that this task doesn't align with any current goal in GOALS.md",
                ),
                GradingCriterion(
                    "asks_about_alignment",
                    "Agent asks the user about goal alignment or why this matters",
                ),
            ],
            fail_if_present=[],
            pass_threshold=1.0,
        ),

        # ------------------------------------------------------------------
        # 4. P0 cap exceeded — should warn and offer options
        # ------------------------------------------------------------------
        EvalScenario(
            id="p0_cap_exceeded",
            name="P0 priority cap warning",
            description="Agent tries to add a P0 task when 3 P0 tasks already exist.",
            system_prompt="",
            user_message=(
                "Process this backlog item as P0:\n\n"
                "```\n- URGENT: Fix payment processing timeout affecting all merchants\n```\n\n"
                "Current P0 tasks:\n"
                "1. Complete Interac Core transaction migration (due Feb 8)\n"
                "2. Fix OBV verification failures in production\n"
                "3. Resolve merchant portal outage\n"
            ),
            criteria=[
                GradingCriterion(
                    "warns_about_cap",
                    "Agent warns that the P0 cap (3) would be exceeded",
                ),
                GradingCriterion(
                    "shows_existing_p0s",
                    "Agent shows or references the existing P0 tasks",
                ),
                GradingCriterion(
                    "offers_options",
                    "Agent offers options: demote an existing P0, downgrade new task, or override",
                ),
            ],
            fail_if_present=["task created", "I've created"],
            pass_threshold=0.8,
        ),

        # ------------------------------------------------------------------
        # 5. Duplicate detection — should flag similarity
        # ------------------------------------------------------------------
        EvalScenario(
            id="duplicate_detection",
            name="Duplicate task detection",
            description="Agent receives a task very similar to an existing one.",
            system_prompt="",
            user_message=(
                "Process this backlog item:\n\n"
                "```\n- Fix authentication bug in the login flow\n```\n\n"
                "Existing tasks:\n"
                "- fix-login-auth-bug.md: 'Fix login authentication error for SSO users' (P1, started)\n"
                "- update-api-docs.md: 'Update API documentation for v2 endpoints' (P2, not started)\n"
            ),
            criteria=[
                GradingCriterion(
                    "flags_duplicate",
                    "Agent flags that the new item is similar to the existing 'fix-login-auth-bug' task",
                ),
                GradingCriterion(
                    "shows_existing",
                    "Agent shows the existing similar task for comparison",
                ),
                GradingCriterion(
                    "asks_user",
                    "Agent asks user whether to merge, skip, or create separately",
                ),
            ],
            fail_if_present=["task created", "I've created"],
            pass_threshold=0.8,
        ),

        # ------------------------------------------------------------------
        # 6. Clear item with goal match — should link and present
        # ------------------------------------------------------------------
        EvalScenario(
            id="clear_item_goal_match",
            name="Clear item matching a goal",
            description="Agent receives a clear task that aligns with Goal 3 (Developer Experience).",
            system_prompt="",
            user_message=(
                "Process this backlog item:\n\n"
                "```\n- Define developer portal requirements for API docs and test credentials\n```"
            ),
            criteria=[
                GradingCriterion(
                    "links_to_goal",
                    "Agent identifies this aligns with Goal 3 (Improve Merchant Onboarding & Developer Experience)",
                ),
                GradingCriterion(
                    "suggests_category",
                    "Agent suggests a category (e.g., technical, strategy, or discovery)",
                ),
                GradingCriterion(
                    "presents_for_review",
                    "Agent presents the item for user review before creating",
                ),
            ],
            fail_if_present=["task created", "I've created"],
            pass_threshold=0.8,
        ),
    ]

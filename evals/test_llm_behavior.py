"""
LLM-in-the-Loop Behavioral Evals

Tests whether the agent actually follows behavioral contracts from AGENTS.md
and SKILL.md by making real Claude API calls and grading responses with a judge.

Each scenario:
1. Assembles a system prompt from AGENTS.md + SKILL.md + context
2. Sends a user message to Claude (the "agent under test")
3. Sends the agent's response to a second Claude call (the "judge")
4. Grades pass/fail based on per-criterion scores and a threshold

Run with: ANTHROPIC_API_KEY=sk-... uv run pytest evals/test_llm_behavior.py -v
Skip automatically if no API key is set.

Cost: ~$0.10-0.20 per full suite run (6 scenarios x 2 calls x ~2K tokens).
"""

import json
import sys
from pathlib import Path

import pytest

# Ensure project root is on path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "evals" / "fixtures"))

from llm_scenarios.backlog_processing import (
    EvalScenario,
    JUDGE_SYSTEM_PROMPT,
    JUDGE_USER_TEMPLATE,
    build_scenarios,
)


# ============================================================================
# Prompt Assembly
# ============================================================================


def build_system_prompt(
    agents_md: str,
    skill_md: str,
    goals_md: str,
    scenario: EvalScenario,
) -> str:
    """Assemble the full system prompt the agent sees."""
    return (
        "You are an AI product management assistant. Follow these instructions exactly.\n\n"
        "# AGENTS.md\n\n"
        f"{agents_md}\n\n"
        "# SKILL.md (processing-backlog)\n\n"
        f"{skill_md}\n\n"
        "# GOALS.md\n\n"
        f"{goals_md}\n\n"
        "# Important\n\n"
        "- You do NOT have access to any tools or MCP servers in this conversation.\n"
        "- You cannot create files, call APIs, or execute commands.\n"
        "- Respond as if you are presenting findings to the user for review.\n"
        "- Follow ALL behavioral instructions from AGENTS.md and SKILL.md above.\n"
    )


# ============================================================================
# API Calls
# ============================================================================


def call_agent(client, model: str, system_prompt: str, user_message: str) -> str:
    """Call Claude as the agent under test. Returns the agent's text response."""
    response = client.messages.create(
        model=model,
        max_tokens=1500,
        system=system_prompt,
        messages=[{"role": "user", "content": user_message}],
    )
    return response.content[0].text


def call_judge(
    client,
    model: str,
    agent_response: str,
    scenario: EvalScenario,
) -> dict:
    """Call Claude as the judge. Returns parsed JSON with criterion scores."""
    rubric_lines = []
    for c in scenario.criteria:
        rubric_lines.append(f"- **{c.name}** (weight {c.weight}): {c.description}")
    rubric = "\n".join(rubric_lines)

    fail_phrases = (
        ", ".join(f'"{p}"' for p in scenario.fail_if_present)
        if scenario.fail_if_present
        else "None"
    )

    user_msg = JUDGE_USER_TEMPLATE.format(
        agent_response=agent_response,
        rubric=rubric,
        fail_phrases=fail_phrases,
    )

    response = client.messages.create(
        model=model,
        max_tokens=1000,
        system=JUDGE_SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_msg}],
    )

    text = response.content[0].text.strip()

    # Extract JSON from response (handle markdown code blocks)
    if text.startswith("```"):
        lines = text.split("\n")
        # Drop first and last lines (``` markers)
        text = "\n".join(lines[1:-1])

    return json.loads(text)


# ============================================================================
# Grading
# ============================================================================


def grade_response(judge_output: dict, scenario: EvalScenario) -> tuple[bool, float, dict]:
    """
    Compute weighted score and pass/fail from judge output.

    Returns:
        (passed, score, details) where details maps criterion name to score+reason.
    """
    criteria_scores = judge_output.get("criteria_scores", {})
    total_weight = 0.0
    weighted_sum = 0.0
    details = {}

    for criterion in scenario.criteria:
        entry = criteria_scores.get(criterion.name, {"score": 0, "reason": "not graded"})
        score = entry.get("score", 0)
        reason = entry.get("reason", "")

        weighted_sum += score * criterion.weight
        total_weight += criterion.weight
        details[criterion.name] = {"score": score, "reason": reason}

    final_score = weighted_sum / total_weight if total_weight > 0 else 0.0
    passed = final_score >= scenario.pass_threshold

    return passed, final_score, details


# ============================================================================
# Parametrized Test
# ============================================================================

SCENARIOS = build_scenarios()
SCENARIO_IDS = [s.id for s in SCENARIOS]


@pytest.mark.llm
@pytest.mark.parametrize("scenario", SCENARIOS, ids=SCENARIO_IDS)
def test_agent_behavior(
    scenario: EvalScenario,
    anthropic_client,
    llm_model: str,
    judge_model: str,
    agents_md_content: str,
    skill_md_content: str,
    goals_md_content: str,
):
    """Test that the agent follows behavioral contracts for each scenario."""
    # Build system prompt
    system_prompt = build_system_prompt(
        agents_md_content, skill_md_content, goals_md_content, scenario
    )
    scenario.system_prompt = system_prompt

    # Step 1: Get agent response
    agent_response = call_agent(
        anthropic_client, llm_model, system_prompt, scenario.user_message
    )

    # Step 2: Grade with judge
    judge_output = call_judge(
        anthropic_client, judge_model, agent_response, scenario
    )

    # Step 3: Compute pass/fail
    passed, score, details = grade_response(judge_output, scenario)

    # Print detailed results for visibility in pytest -v output
    print(f"\n{'='*60}")
    print(f"Scenario: {scenario.name} ({scenario.id})")
    print(f"Score: {score:.2f} / threshold: {scenario.pass_threshold}")
    print(f"Result: {'PASS' if passed else 'FAIL'}")
    print(f"-" * 60)
    for name, info in details.items():
        status = "PASS" if info["score"] == 1 else "FAIL"
        print(f"  [{status}] {name}: {info['reason']}")
    print(f"{'='*60}")

    assert passed, (
        f"Scenario '{scenario.name}' failed with score {score:.2f} "
        f"(threshold: {scenario.pass_threshold}).\n"
        f"Details: {json.dumps(details, indent=2)}\n"
        f"Agent response (first 500 chars): {agent_response[:500]}"
    )

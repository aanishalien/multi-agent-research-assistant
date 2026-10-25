from research_assistant.agents.schemas import ResearchPlan
import pytest
from pydantic import ValidationError

def test_research_plan_schema() -> None:
    plan = ResearchPlan(
        question="What is the impact of AI on software development?",
        tasks=[
            "Analyze the effects of AI on software engineering practices.",
            "Review recent studies on AI integration in development workflows.",
            "Identify potential risks and benefits of AI adoption."
        ]
    )

    assert isinstance(plan, ResearchPlan)
    assert isinstance(plan.question, str)
    assert isinstance(plan.tasks, list)
    assert len(plan.tasks) >= 3

def test_research_plan_rejects_too_few_tasks() -> None:
    with pytest.raises(ValidationError):
        ResearchPlan(
            question="What is the impact of AI on software development?",
            tasks=[
                "Analyze the effects of AI on software engineering practices.",
                "Review recent studies on AI integration in development workflows."
            ]
        )
from unittest.mock import MagicMock, patch

from research_assistant.agents.planner import create_research_plan
from research_assistant.agents.schemas import ResearchPlan

def test_create_research_plan() -> None:
    question = "How are AI Agents changing software engineering?"

    expected_plan = ResearchPlan(
        question=question,
        tasks=[
            "Research AI Agent applications in software engineering.",
            "Analyze productivity improvements",
            "Investigate risks and limitations",
        ],
    )

    mock_chain = MagicMock()
    mock_chain.invoke.return_value = expected_plan

    with (
    patch(
        "research_assistant.agents.planner.create_llm") as 
    mock_create_llm, 
        patch(
            "research_assistant.agents.planner.ChatPromptTemplate"
        ) as mock_prompt_template,
    ):
        mock_llm = mock_create_llm.return_value
        mock_llm.with_structured_output.return_value = MagicMock()

        mock_prompt = mock_prompt_template.from_messages.return_value
        mock_prompt.__or__.return_value = mock_chain
                    
        plan = create_research_plan(question)
        

    assert isinstance(plan, ResearchPlan)
    assert plan.question == question
    assert len(plan.tasks) >= 3
    
    mock_chain.invoke.assert_called_once_with({"question": question})
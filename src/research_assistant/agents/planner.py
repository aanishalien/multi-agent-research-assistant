from langchain_core.prompts import ChatPromptTemplate

from research_assistant.agents.schemas import ResearchPlan
from research_assistant.llm import create_llm

def create_research_plan(question: str) -> ResearchPlan:
    llm = create_llm()

    structured_llm = llm.with_structured_output(ResearchPlan)

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a research planning assistant."
                "Create at least three specific, actionable research tasks."
                "Cover key concepts, evidence, and limitations. "
                "Return the original question and the tasks.",
            ),
            ("human", "Research question: {question}"),
        ]
    )

    chain = prompt | structured_llm

    return chain.invoke({"question": question})
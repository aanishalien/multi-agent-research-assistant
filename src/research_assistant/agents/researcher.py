import json

from langchain_core.prompts import ChatPromptTemplate

from research_assistant.agents.schemas import ResearchFinding
from research_assistant.llm import create_llm
from research_assistant.tools.tavily_search import tavily_search

def research_task(task: str) -> list[ResearchFinding]:
    """Research one task and return findings grounded"""
from pydantic import ValidationError
import pytest

from research_assistant.agents.schemas import SearchResponse, SearchResult

def test_search_response_accepts_valid_results()-> None:
    response = SearchResponse(
        query="AI Agents in Software Engineering",
        results=[
            SearchResult(
                title="AI Agents Overview", 
                url="https://example.com/ai-agents",
                content="AI Agents can automate software development tasks.",
            )
        ],
    )

    assert response.query == "AI Agents in Software Engineering"
    assert len(response.results) == 1
    assert isinstance(response.results[0], SearchResult)

def test_search_result_requires_source_fields() -> None:
    with pytest.raises(ValidationError):
        SearchResult(title="Missing Source data")
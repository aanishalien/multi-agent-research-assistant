import os
import requests
from dotenv import load_dotenv
from research_assistant.agents.schemas import SearchResponse

load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

def tavily_search(query: str, max_results: int = 3) -> dict:
    """Searcg the web and return validate source results."""

    if not TAVILY_API_KEY:
        return {"status": "error", "message": "TAVILY_API_KEY not set"}

    url = "https://api.tavily.com/search"

    payload = {
        "api_key": TAVILY_API_KEY,
        "query": query,
        "max_results": max_results,
        "search_depth": "basic",
    }

    response = requests.post(
        TAVILY_API_KEY,
        json=payload,
        timeout=30,
    )

    response.raise_for_status()
    data = response.json()

    return SearchResponse(
        query=query,
        results=[
            {
                "title": item.get("title", ""),
                "url": item.get("url", ""),
                "content": item.get("content", "")
            }
            for item in data.get("results", [])
        ]
    )


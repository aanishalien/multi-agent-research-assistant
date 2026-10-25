from pydantic import BaseModel, Field

class ResearchPlan(BaseModel):
    question: str
    tasks: list[str] = Field(min_length=3)

class SearchResult(BaseModel):
    title: str
    url: str
    content: str

class SearchResponse(BaseModel):
    query: str
    results: list[SearchResult]

class ResearchFinding(BaseModel):
    claim: str
    evidence: str
    source_title: str
    source_url: str

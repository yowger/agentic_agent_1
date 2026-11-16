from typing import TypedDict
from langchain_core.documents import Document


class AgentState(TypedDict):
    question: str
    documents: list[Document]
    nutrition_data: dict
    generation: str
    retry_count: int
    routes: list[str]
    grade: str

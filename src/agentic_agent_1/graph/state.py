from typing import TypedDict, NotRequired

from langchain_core.documents import Document


class AgentState(TypedDict):
    question: str
    documents: list[Document]
    nutrition_data: NotRequired[dict]
    generation: NotRequired[str]
    retry_count: NotRequired[int]
    routes: NotRequired[list[str]]
    grade: NotRequired[str]
    aggregated_context: NotRequired[str]

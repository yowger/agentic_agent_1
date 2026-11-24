from typing import TypedDict, NotRequired
from langchain_core.documents import Document

from agentic_agent_1.graph.schemas.router import Routes
from agentic_agent_1.graph.schemas.metadata_filter import MetadataFilter


class Aggregated_context(TypedDict):
    documents: list[Document]
    nutrition_data: NotRequired[dict]


class AgentState(TypedDict):
    question: str
    documents: list[Document]
    web_documents: NotRequired[list[Document]]
    nutrition_data: NotRequired[dict]
    generation: NotRequired[str]
    web_search: NotRequired[bool]
    retry_count: NotRequired[int]
    routes: NotRequired[Routes]
    metadata_filter: MetadataFilter
    grade: NotRequired[str]
    aggregated_context: NotRequired[Aggregated_context]

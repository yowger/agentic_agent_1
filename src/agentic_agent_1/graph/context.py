from typing import TypedDict

from langchain_core.retrievers import BaseRetriever


class GraphContext(TypedDict):
    retriever: BaseRetriever

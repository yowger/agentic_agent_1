from typing import  TypedDict

from langchain_core.vectorstores import VectorStore

class GraphContext(TypedDict):
    vectorstore: VectorStore
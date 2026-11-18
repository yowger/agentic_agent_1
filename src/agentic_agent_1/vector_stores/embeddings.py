from langchain_openai import OpenAIEmbeddings

from agentic_agent_1.vector_stores.consts import EMBEDDING_MODEL

def get_embeddings() -> OpenAIEmbeddings:
    return OpenAIEmbeddings(
        model=EMBEDDING_MODEL,
    )
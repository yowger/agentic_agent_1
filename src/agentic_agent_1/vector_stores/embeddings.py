from langchain_openai import OpenAIEmbeddings

from agentic_agent_1.config.config import settings


def get_embeddings() -> OpenAIEmbeddings:
    return OpenAIEmbeddings(
        model=settings.EMBEDDING_MODEL,
    )

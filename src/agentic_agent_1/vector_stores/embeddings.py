from langchain_openai import OpenAIEmbeddings

from agentic_agent_1.config.settings import settings


def get_embeddings() -> OpenAIEmbeddings:
    return OpenAIEmbeddings(
        api_key=settings.OPENAI_API_KEY, model=settings.EMBEDDING_MODEL
    )

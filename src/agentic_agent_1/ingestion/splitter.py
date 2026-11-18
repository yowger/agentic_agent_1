from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

from agentic_agent_1.ingestion.sources import ChunkingConfig


def split_documents(documents: list[Document], chunking_config: ChunkingConfig) -> list[Document]:
    """"Split documents into smaller chunks.

    Args: 
        documents: Loaded and metadata-enriched documents.
        chunking: chunk size and overlap configuration.

    Returns: 
        A list of split Document objects.
    """

    chunk_size = chunking_config["chunk_size"]
    chunk_overlap = chunking_config["chunk_overlap"]

    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero.")

    if chunk_overlap < 0:
        raise ValueError("chunk_overlap must be non-negative")

    if chunk_overlap >= chunk_size:
        raise ValueError("chunk_overlap must be smaller than chunk_size")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        add_start_index=True
    )

    return splitter.split_documents(documents)

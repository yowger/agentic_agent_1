from langchain_core.documents import Document

from agentic_agent_1.ingestion.sources import PDFSource


def enrich_metadata(
        documents: list[Document],
        source: PDFSource
) -> list[Document]:
    metadata = source["metadata"]

    for document in documents:
        document.metadata.update(metadata)
        document.metadata["source_id"] = source["source_id"]

    return documents

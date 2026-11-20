from agentic_agent_1.config.paths import RAW_DIR
from agentic_agent_1.ingestion.loader import load_pdf
from agentic_agent_1.ingestion.metadata import enrich_metadata
from agentic_agent_1.ingestion.sources import DEFAULT_CHUNKING, PDF_SOURCES, PDFSource
from agentic_agent_1.ingestion.splitter import split_documents
from agentic_agent_1.vector_stores.chroma import upsert_source_documents


def ingest_source(source: PDFSource):
    file_path = RAW_DIR / source["filename"]
    source_id = source["source_id"]

    print(file_path)

    documents = load_pdf(file_path)

    documents = enrich_metadata(documents, source)

    chunking_config = {**DEFAULT_CHUNKING, **source.get("chunking_config", {})}

    chunks = split_documents(documents, chunking_config)

    upsert_source_documents(
        documents=chunks,
        source_id=source_id
    )

    print(
        f"Successfully ingested {source['filename']}: " f"{len(chunks)} chunks")


def ingest_all_sources():
    for source in PDF_SOURCES:
        ingest_source(source=source)


def main():
    ingest_all_sources()


if __name__ == "__main__":
    main()

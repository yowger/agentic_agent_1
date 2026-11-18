from pathlib import Path
from dotenv import load_dotenv

from agentic_agent_1.ingestion.sources import PDF_SOURCES, DEFAULT_CHUNKING
from agentic_agent_1.ingestion.sources import PDFSource
from agentic_agent_1.ingestion.loader import load_pdf
from agentic_agent_1.ingestion.splitter import split_documents
from agentic_agent_1.vector_stores.chroma import upsert_source_documents
from agentic_agent_1.ingestion.metadata import enrich_metadata

load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DIRECTORY = PROJECT_ROOT / "data" / "raw"
CHROMA_DIRECTORY = PROJECT_ROOT / "chroma_store"


def ingest_source(source: PDFSource):
    file_path = RAW_DIRECTORY / source["filename"]

    documents = load_pdf(file_path)

    documents = enrich_metadata(
        documents,
        source
    )

    chunking_config = source.get(
        "chunking",
        DEFAULT_CHUNKING
    )

    chunks = split_documents(
        documents,
        chunking_config
    )

    upsert_source_documents(
        documents=chunks,
        persist_directory=CHROMA_DIRECTORY,
        source_id=source["source_id"]
    )

    print(
        f"Successfully ingested {source['filename']}: "
        f"{len(chunks)} chunks"
    )


def ingest_all_sources():
    for source in PDF_SOURCES:
        ingest_source(source)


def main():
    ingest_all_sources()


if __name__ == "__main__":
    main()

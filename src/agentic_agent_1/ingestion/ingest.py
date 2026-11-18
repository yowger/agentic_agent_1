from pathlib import Path
from dotenv import load_dotenv

from agentic_agent_1.ingestion.loader import load_pdf
from agentic_agent_1.ingestion.splitter import split_documents
from agentic_agent_1.vector_stores.chroma import create_vectorstore
from agentic_agent_1.ingestion.sources import PDF_SOURCES, DEFAULT_CHUNKING
from agentic_agent_1.ingestion.metadata import enrich_metadata

load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DIRECTORY = PROJECT_ROOT / "data" / "raw"
CHROMA_DIRECTORY = PROJECT_ROOT / "chroma_store"


def main():
    # documents = load_pdf(RAW_DIRECTORY)
    # for document in documents:
    #     print(document.metadata)

    # print(f"Total pages loaded: {len(documents)}")

    # chunks = split_documents(documents)

    # print(f"Total chunks created: {len(chunks)}")

    # create_vectorstore(
    #     documents=chunks,
    #     persist_directory=CHROMA_DIRECTORY,
    # )

    # print("Documents successfully stored.")

    # test
    PDF_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"
    file_dir = PDF_DIR / "carb_intake_all_ages_eng.pdf"
    documents = load_pdf(file_dir)
    print(f"PDF_DIR: {file_dir}")

    print(f"documents loaded {len(documents)}")

    print(f"page content: {documents[0].page_content[:500]}")
    print(f"metadata: {documents[0].metadata}")

    source = PDF_SOURCES[0]

    documents = enrich_metadata(documents, source)

    print(f"new metadata: {documents[0].metadata}")

    chunking_config = source.get("chunking", DEFAULT_CHUNKING)

    chunks = split_documents(
        documents,
        chunking_config=chunking_config
    )

    print(f"total chunks created: {len(chunks)}")
    print(f"chunk 0: {chunks[0].page_content}")
    print(f"first chunk metadata: {chunks[0].metadata}")


if __name__ == "__main__":
    main()

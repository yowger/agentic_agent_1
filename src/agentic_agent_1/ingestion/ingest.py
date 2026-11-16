from pathlib import Path
from dotenv import load_dotenv

from agentic_agent_1.ingestion.loader import load_pdfs
from agentic_agent_1.ingestion.splitter import split_documents
from agentic_agent_1.vector_stores.chroma import create_vectorstore

load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DIRECTORY = PROJECT_ROOT / "data" / "raw"
CHROMA_DIRECTORY = PROJECT_ROOT / "chroma_store"


def main():
    documents = load_pdfs(RAW_DIRECTORY)
    for document in documents:
        print(document.metadata)

    # print(f"Total pages loaded: {len(documents)}")

    # chunks = split_documents(documents)

    # print(f"Total chunks created: {len(chunks)}")

    # create_vectorstore(
    #     documents=chunks,
    #     persist_directory=CHROMA_DIRECTORY,
    # )

    # print("Documents successfully stored.")


if __name__ == "__main__":
    main()

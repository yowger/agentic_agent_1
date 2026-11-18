from pathlib import Path
from typing import List
from langchain_chroma import Chroma
from langchain_core.documents import Document

from agentic_agent_1.vector_stores.consts import COLLECTION_NAME
from agentic_agent_1.vector_stores.embeddings import get_embeddings


def create_vectorstore(
    documents,
    persist_directory: Path,
):
    embeddings = get_embeddings()

    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        collection_name=COLLECTION_NAME,
        persist_directory=str(persist_directory),
    )

    return vectorstore


def get_vectorstore(persist_directory: Path):
    embeddings = get_embeddings()

    vectorstore = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=str(persist_directory),
    )

    return vectorstore


def upsert_source_documents(
    documents: List[Document],
    persist_directory: Path,
    source_id: str
) -> Chroma:
    vectorstore = get_vectorstore(persist_directory)

    existing_ids = vectorstore.get(where={"source_id": source_id})["ids"]

    new_ids = [
        f"{source_id}:chunk:{index}"
        for index in range(len(documents))
    ]

    vectorstore.add_documents(
        documents=documents,
        ids=new_ids
    )

    stale_ids = list(set(existing_ids) - set(new_ids))

    if stale_ids:
        vectorstore.delete(ids=stale_ids)

    return vectorstore

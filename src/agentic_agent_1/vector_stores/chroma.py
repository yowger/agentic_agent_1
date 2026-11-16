from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


def create_vectorstore(
    documents,
    persist_directory: Path,
):
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        collection_name="nutrition_knowledge",
        persist_directory=str(persist_directory),
    )

    return vectorstore

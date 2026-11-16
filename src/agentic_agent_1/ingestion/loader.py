from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document


def load_pdfs(directory: Path) -> list[Document]:
    """
    Recursively finds and loads all PDF files in a directory into LangChain Documents.

        Each page of a PDF is loaded as a separate Document object and enriched with
        additional metadata:
            - 'filename': The name of the PDF file.
            - 'category': The name of the PDF's immediate parent directory.

        Args:
            directory (Path): The root directory path to search for PDF files.

        Returns:
            list[Document]: A list of LangChain Document objects representing all
            loaded PDF pages.
    """
    
    documents = []

    pdf_files = list(directory.rglob("*.pdf"))

    print(f"Found {len(pdf_files)} PDF files")

    for pdf_path in pdf_files:
        print(f"Loading: {pdf_path.name}")

        loader = PyPDFLoader(str(pdf_path))
        pdf_documents = loader.load()

        for doc in pdf_documents:
            doc.metadata["filename"] = pdf_path.name
            doc.metadata["category"] = pdf_path.parent.name

        documents.extend(pdf_documents)

    return documents

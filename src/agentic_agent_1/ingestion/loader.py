from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document


def load_pdf(file_path: Path) -> list[Document]:
    """Load a pdf file and extract its pages as LangChain Document Objects.

    Args: 
        file_path: Path to the target PDF file.

    Returns:
        A list of  `Document` objects, where each item corresponds to a single page of the PDF with extracted text and default page metadata.

    Raises:
        FileNotFoundError: If `file_path` does not exist.
        ValueError: `file_path` does not have a `.pdf` extension.
    """

    if not file_path.exists():
        raise FileNotFoundError(f"PDF not found: {file_path}")

    if file_path.suffix.lower() != ".pdf":
        raise ValueError(f"Expected a PDF file: {file_path}")

    loader = PyPDFLoader(str(file_path))

    return loader.load()


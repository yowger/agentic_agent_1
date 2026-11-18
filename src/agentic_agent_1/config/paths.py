from pathlib import Path

PACKAGE_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = PACKAGE_DIR / "data"
RAW_DIRECTORY = DATA_DIR / "raw"

CHROMA_DIRECTORY = PACKAGE_DIR / "chroma_store"
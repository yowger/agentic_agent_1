from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[3]

CHROMA_DIR = ROOT_DIR / "chroma_store"
ENV_DIR = ROOT_DIR / ".env"

SRC_DIR = ROOT_DIR / "src"
PROJECT_DIR = SRC_DIR / "agentic_agent_1"
DATA_DIR = PROJECT_DIR / "data"
RAW_DIR = DATA_DIR / "raw"

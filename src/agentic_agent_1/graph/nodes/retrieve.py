from pathlib import Path

from agentic_agent_1.vector_stores.chroma import get_vectorstore


PROJECT_ROOT = Path(__file__).resolve().parents[2]
CHROMA_DIRECTORY = PROJECT_ROOT / "chroma_store"


vectorstore = get_vectorstore(CHROMA_DIRECTORY)

print(vectorstore)

results = vectorstore.get(
    where={
        "source_id": "who_carbohydrate_intake_adults_children_2023"
    },
    include=["metadatas", "documents"]
)

print("Total stored chunks:", len(results["ids"]))
print("First chunk:", results["documents"][0])

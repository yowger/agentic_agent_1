from pathlib import Path

from agentic_agent_1.vector_stores.chroma import get_vectorstore

PROJECT_ROOT = Path(__file__).resolve().parents[2]

vectorstore = get_vectorstore(
    PROJECT_ROOT / "chroma_store"
)

results = vectorstore.similarity_search(
    "Why does the body need carbohydrates?",
    k=4
)
print(f"results: {results}")
for i, doc in enumerate(results, start=1):
    print(f"\n--- RESULT {i} ---")
    print(doc.page_content)
    print(doc.metadata)

from agentic_agent_1.config.paths import CHROMA_DIR
from agentic_agent_1.vector_stores.chroma import get_vectorstore

print(CHROMA_DIR)
vectorstore = get_vectorstore(CHROMA_DIR)

results = vectorstore.similarity_search("Why does the body need carbohydrates?", k=4)
print(f"results: {results}")
for i, doc in enumerate(results, start=1):
    print(f"\n--- RESULT {i} ---")
    print(doc.page_content)
    print(doc.metadata)

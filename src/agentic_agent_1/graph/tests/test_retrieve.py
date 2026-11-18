from agentic_agent_1.vector_stores.chroma import get_vectorstore
from agentic_agent_1.config.paths import CHROMA_DIRECTORY


vectorstore = get_vectorstore(CHROMA_DIRECTORY)

results = vectorstore.similarity_search(
    "Why does the body need carbohydrates?",
    k=4
    
)
print(f"results: {results}")
for i, doc in enumerate(results, start=1):
    print(f"\n--- RESULT {i} ---")
    print(doc.page_content)
    print(doc.metadata)

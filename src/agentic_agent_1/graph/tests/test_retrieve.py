from agentic_agent_1.vector_stores.chroma import get_vectorstore

vectorstore = get_vectorstore()
retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

results = retriever.invoke("Why does the body need carbohydrates?")

print(f"results: {results}")
for i, doc in enumerate(results, start=1):
    print(f"\n--- RESULT {i} ---")
    print(doc.page_content)
    print(doc.metadata)

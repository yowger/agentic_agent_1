
from agentic_agent_1.vector_stores.chroma import get_vectorstore


def test_retriever_returns_documents():
    vectorstore = get_vectorstore()

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 4}
    )

    results = retriever.invoke(
        "Why does the body need carbohydrates?"
    )

    assert results, "Retriever returned no documents"
    assert len(results) <= 4

    for doc in results:
        assert doc.page_content.strip()
        assert doc.metadata

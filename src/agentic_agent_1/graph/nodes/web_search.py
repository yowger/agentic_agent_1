from ddgs import DDGS
from langchain_core.documents import Document

from agentic_agent_1.graph.state import AgentState


def web_search_node(state: AgentState) -> AgentState:
    question = state["question"]

    results = DDGS().text(
        question,
        max_results=5
    )

    documents = []

    for result in results:
        body = result.get("body", "")

        if not body.strip():
            continue

        document = Document(
            page_content=result.get("body", ""),
            metadata={
                "source": result.get("href", ""),
                "title": result.get("title", ""),
                "source_type": "web",
            }
        )

        documents.append(document)

    print(results)

    return {
        "web_documents": documents
    }

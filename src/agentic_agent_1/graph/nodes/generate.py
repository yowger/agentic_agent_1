from agentic_agent_1.graph.state import AgentState

from agentic_agent_1.chains.generate import generation_chain


def generate_node(state: AgentState) -> AgentState:
    print("--- GENERATE NODE ---")

    question = state["question"]
    context = state.get("aggregated_context", {})

    documents = context.get("documents", [])
    nutrition_data = context.get("nutrition_data")

    document_context = ""

    for i, doc in enumerate(documents, start=1):
        metadata = doc.metadata

        title = metadata.get("title", "Unknown title")
        organization = metadata.get("organization", "Unknown organization")
        page = metadata.get("page_label", "Unknown page")

        document_context += (
            f"\n[Document {i}]\n"
            f"Title: {title}\n"
            f"Organization: {organization}\n"
            f"Page: {page}\n"
            f"Content: {doc.page_content}\n"
        )

    nutrition_context = ""

    if nutrition_data:
        nutrition_context = f"\nNutrition Data:\n{nutrition_data}"

    formatted_context = (
        f"Retrieved Documents:\n{document_context}\n"
        f"{nutrition_context}"
    )

    response = generation_chain.invoke({
        "question": question,
        "context": formatted_context
    })

    return {
        "generation": response.content
    }

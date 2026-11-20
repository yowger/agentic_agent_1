from agentic_agent_1.graph.state import AgentState


def aggregate_node(state: AgentState) -> AgentState:
    print("--- AGGREGATE NODE ---")

    documents = state.get("documents", [])
    nutrition_data = state.get("nutrition_data", {})

    context_parts = []

    if documents:
        document_context = "\n\n".join(
            doc.page_content for doc in documents
        )

        context_parts.append(
            f"Retrieved Documents:\n{document_context}"
        )

    if nutrition_data:
        context_parts.append(
            f"Nutrition Data:\n{nutrition_data}"
        )

    aggregated_context = "\n\n".join(context_parts)

    return {
        "aggregated_context": aggregated_context
    }

from agentic_agent_1.graph.state import AgentState


def aggregate_node(state: AgentState) -> AgentState:
    print("--- AGGREGATE NODE ---")

    context = {
        "documents": state.get("documents", []),
        "web_documents": state.get("web_documents", []),
        "nutrition_data": state.get("nutrition_data")
    }

    return {
        "aggregated_context": context
    }

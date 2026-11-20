from agentic_agent_1.graph.state import AgentState


def aggregate_node(state: AgentState) -> AgentState:
    print("--- AGGREGATE NODE ---")

    context = {
        "documents": state.get("documents", []),
    }

    nutrition_data = state.get("nutrition_data")

    if nutrition_data:
        context["nutrition_data"] = nutrition_data

    return {
        "aggregated_context": context
    }

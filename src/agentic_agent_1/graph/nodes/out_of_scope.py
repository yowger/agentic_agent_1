from agentic_agent_1.graph.state import AgentState


def out_of_scope_node(state: AgentState) -> AgentState:
    print("--- OUT OF SCOPE NODE ---")

    return {
        "generation": (
            "I'm a food and nutrition assistant, so I can only "
            "help with questions related to food, nutrition, "
            "and dietary guidelines."
        )
    }

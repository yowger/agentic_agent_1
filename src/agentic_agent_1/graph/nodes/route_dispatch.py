from langgraph.types import Send

from agentic_agent_1.graph.state import AgentState


def route_dispatch_node(state: AgentState) -> list[Send]:
    """Dispatch agent state to each selected route"""

    print("--- DISPATCH NODE ---")

    routes = state["routes"]

    route_decision = [
        Send(route, state)
        for route in routes
    ]

    return route_decision

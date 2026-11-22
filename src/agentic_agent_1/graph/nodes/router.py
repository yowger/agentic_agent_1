from agentic_agent_1.graph.schemas.router import RouteDecision
from agentic_agent_1.graph.state import AgentState

from agentic_agent_1.chains.router import question_router_chain


def route_decision_node(state: AgentState) -> AgentState:
    print("--- ROUTE DECISION ---")

    question = state["question"]

    result: RouteDecision = question_router_chain.invoke(
        {"question": question})

    print("Selected routes:", result)

    return {
        "routes": result.routes,
        "metadata_filter": result.metadata_filter
    }

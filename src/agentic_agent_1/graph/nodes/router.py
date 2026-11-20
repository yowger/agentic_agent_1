from agentic_agent_1.graph.schemas.router import RouteDecision
from agentic_agent_1.graph.state import AgentState

from agentic_agent_1.chains.router import question_router_chain


def route_decision_node(state: AgentState):
    print("--- ROUTE DECISION ---")

    question = state["question"]

    decision: RouteDecision = question_router_chain.invoke(
        {"question": question})

    print("Selected routes:", decision.routes)

    return {"routes": decision.routes}

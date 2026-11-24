from agentic_agent_1.graph.schemas.router import RouteQuery
from agentic_agent_1.graph.state import AgentState

from agentic_agent_1.chains.router import question_router_chain


def route_query_node(state: AgentState) -> AgentState:
    print("--- ROUTE QUERY NODE ---")

    question = state["question"]

    result: RouteQuery = question_router_chain.invoke(
        {"question": question})

    print("Selected routes:", result)

    return {
        "routes": result.routes,
        "metadata_filter": result.metadata_filter
    }

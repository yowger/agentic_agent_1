from agentic_agent_1.graph.state import AgentState
from agentic_agent_1.graph.consts import AGGREGATE, WEB_SEARCH


def route_after_grading(state: AgentState):
    print("--- ROUTER AFTER GRADING ---")

    web_search = state["web_search"]

    if web_search:
        print("--- NO RELEVANT DOCUMENTS FOUND. WEB SEARCHING ---")

        return WEB_SEARCH

    return AGGREGATE

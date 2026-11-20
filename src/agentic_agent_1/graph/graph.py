# from ddgs import DDGS
from langgraph.graph import END, START, StateGraph

from agentic_agent_1.graph.consts import AGGREGATE, ROUTE_DECISION, RETRIEVE, NUTRITION_API, GENERATE
from agentic_agent_1.graph.state import AgentState
from agentic_agent_1.graph.nodes.router import route_decision_node
from agentic_agent_1.graph.nodes.route_dispatch import route_dispatch_node
from agentic_agent_1.graph.nodes.retrieve import retrieve_node
from agentic_agent_1.graph.nodes.nutrition_api import nutrition_api_node
from agentic_agent_1.graph.nodes.aggregate import aggregate_node
from agentic_agent_1.graph.nodes.route_after_aggregate import route_after_aggregate
from agentic_agent_1.graph.nodes.generate import generate_node

workflow = StateGraph(AgentState)

workflow.add_node(ROUTE_DECISION, route_decision_node)
workflow.add_node(RETRIEVE, retrieve_node)
workflow.add_node(NUTRITION_API, nutrition_api_node)
workflow.add_node(AGGREGATE, aggregate_node, defer=True)
workflow.add_node(GENERATE, generate_node)

workflow.add_edge(START, ROUTE_DECISION)
workflow.add_conditional_edges(
    ROUTE_DECISION,
    route_dispatch_node,
    [
        RETRIEVE,
        NUTRITION_API
    ]
)
workflow.add_edge(RETRIEVE, AGGREGATE)
workflow.add_edge(NUTRITION_API, AGGREGATE)
workflow.add_conditional_edges(
    AGGREGATE,
    route_after_aggregate,
    [
        GENERATE
    ]
)
workflow.add_edge(GENERATE, END)
# workflow.add_conditional_edges()
# workflow.add_edge(ROUTE_DECISION, END)

app = workflow.compile()

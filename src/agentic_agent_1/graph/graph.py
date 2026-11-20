# from ddgs import DDGS
from langgraph.graph import END, START, StateGraph

from agentic_agent_1.graph.consts import ROUTE_DECISION
from agentic_agent_1.graph.nodes.router import route_decision_node
from agentic_agent_1.graph.state import AgentState

workflow = StateGraph(AgentState)

workflow.add_node(ROUTE_DECISION, route_decision_node)

workflow.add_edge(START, ROUTE_DECISION)
workflow.add_edge(ROUTE_DECISION, END)

app = workflow.compile()

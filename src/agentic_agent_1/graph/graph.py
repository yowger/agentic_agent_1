from langgraph.graph import END, START, StateGraph

from agentic_agent_1.graph.consts import AGGREGATE, ROUTE_DECISION, RETRIEVE, NUTRITION_API, GENERATE, GRADE_DOCUMENTS, WEB_SEARCH, OUT_OF_SCOPE
from agentic_agent_1.graph.state import AgentState
from agentic_agent_1.graph.context import GraphContext
from agentic_agent_1.graph.nodes.route_query import route_query_node
from agentic_agent_1.graph.nodes.route_dispatch import route_dispatch_node
from agentic_agent_1.graph.nodes.retrieve import retrieve_node
from agentic_agent_1.graph.nodes.nutrition_api import nutrition_api_node
from agentic_agent_1.graph.nodes.aggregate import aggregate_node
from agentic_agent_1.graph.nodes.generate import generate_node
from agentic_agent_1.graph.nodes.grade_documents import grade_documents_node
from agentic_agent_1.graph.nodes.web_search import web_search_node
from agentic_agent_1.graph.routers.route_after_aggregate import route_after_aggregate
from agentic_agent_1.graph.routers.route_after_grading import route_after_grading
from agentic_agent_1.graph.nodes.out_of_scope import out_of_scope_node
workflow = StateGraph(
    AgentState,
    context_schema=GraphContext
)

workflow.add_node(ROUTE_DECISION, route_query_node)
workflow.add_node(RETRIEVE, retrieve_node)
workflow.add_node(NUTRITION_API, nutrition_api_node)
workflow.add_node(AGGREGATE, aggregate_node, defer=True)
workflow.add_node(GENERATE, generate_node)
workflow.add_node(GRADE_DOCUMENTS, grade_documents_node)
workflow.add_node(WEB_SEARCH, web_search_node)
workflow.add_node(OUT_OF_SCOPE, out_of_scope_node)

workflow.add_edge(START, ROUTE_DECISION)
workflow.add_conditional_edges(
    ROUTE_DECISION,
    route_dispatch_node,
    [
        RETRIEVE,
        NUTRITION_API,
        OUT_OF_SCOPE
    ]
)
workflow.add_edge(RETRIEVE, GRADE_DOCUMENTS)
workflow.add_conditional_edges(
    GRADE_DOCUMENTS,
    route_after_grading,
    [
        WEB_SEARCH,
        AGGREGATE
    ]
)
workflow.add_edge(WEB_SEARCH, AGGREGATE)
workflow.add_edge(NUTRITION_API, AGGREGATE)
workflow.add_conditional_edges(
    AGGREGATE,
    route_after_aggregate,
    [
        GENERATE
    ]
)
workflow.add_edge(OUT_OF_SCOPE, END)
workflow.add_edge(GENERATE, END)
# workflow.add_conditional_edges()
# workflow.add_edge(ROUTE_DECISION, END)

app = workflow.compile()

app.get_graph().draw_mermaid_png(
    output_file_path="nutrition_agentic_rag_graph_2.png")

from ddgs import DDGS
# from dotenv import load_dotenv
# from langgraph.graph import START, END, StateGraph
# from langgraph.types import Send

# # Initialize client and run a text search
results = DDGS().text("How does carbs help body", max_results=5)

print(results)

# from typing import TypedDict
# from langchain_core.documents import Document


# def retrieve_data_node(state: AgentState):
#     print("--- RETRIEVE ---")

#     return {
#         "documents": [],
#     }


# def grade_documents_node(state: AgentState):
#     print("--- GRADE DOCUMENTS ---")

#     return {}


# def rewrite_question_node(state: AgentState):
#     print("--- REWRITE QUESTION ---")

#     return {
#         "retry_count": state["retry_count"] + 1,
#     }


# def generate_answer_node(state: AgentState):
#     print("--- GENERATE ---")

#     return {
#         "generation": "Placeholder answer",
#     }


# def nutrition_api_node(state: AgentState):
#     print("nutrition api search")

#     pass


# def web_search_node(state: AgentState):

#     pass


# def route_decision_node(state: AgentState):
#     print("--- Decide node ---")

#     return {
#         "routes": ["retrieve", "nutrition_api"]
#     }


# def route_dispatch_node(state: AgentState):
#     print("--- dispatch node ---")
#     routes = state["routes"]

#     route_decision = [
#         Send(route, state)
#         for route in routes
#     ]

#     return route_decision


# def aggregate_node(state: AgentState):
#     print("--- AGGREGATE ---")

#     print("Documents:", state["documents"])
#     print("Nutrition:", state["nutrition_data"])

#     return {}


# def route_after_aggregation(state: AgentState):
#     # Only grade documents if retrieval was selected.

#     if RETRIEVE in state["routes"]:
#         return GRADE_DOCUMENTS

#     return GENERATE


# def route_after_grading(state: AgentState):
#     return state["route"]


# def evaluator_node(state: AgentState):
#     "check if suffiecent answer otherwise research again"

#     pass


# RETRIEVE = "retrieve"
# GRADE_DOCUMENTS = "grade_documents"
# GENERATE = "generate"
# NUTRITION_API = "nutrition_api"
# WEB_SEARCH = "web_search"
# ROUTE_DECISION = "route_decision"

# NUTRITION_ONLY = "nutrition_only"
# KNOWLEDGE_ONLY = "knowledge_only"
# COMBINED = "combined"
# AGGREGATE = "aggregate"

# builder = StateGraph(AgentState)

# builder.add_node(ROUTE_DECISION, route_decision_node, )
# builder.add_node(RETRIEVE, retrieve_data_node)
# builder.add_node(NUTRITION_API, nutrition_api_node)
# builder.add_node(AGGREGATE, aggregate_node, defer=True)
# builder.add_node(WEB_SEARCH, web_search_node)
# builder.add_node(GRADE_DOCUMENTS, grade_documents_node)
# builder.add_node(GENERATE, generate_answer_node)


# builder.add_edge(START, ROUTE_DECISION)

# builder.add_conditional_edges(
#     ROUTE_DECISION,
#     route_dispatch_node,
#     [
#         RETRIEVE,
#         NUTRITION_API,
#     ])

# builder.add_edge(NUTRITION_API, AGGREGATE)
# builder.add_edge(RETRIEVE, AGGREGATE)

# builder.add_conditional_edges(
#     AGGREGATE,
#     route_after_aggregation,
#     [
#         GRADE_DOCUMENTS,
#         GENERATE,
#     ]
# )

# builder.add_conditional_edges(
#     GRADE_DOCUMENTS,
#     route_after_grading,
#     [
#         GENERATE,
#         WEB_SEARCH,
#     ]
# )

# builder.add_edge(WEB_SEARCH, GENERATE)
# builder.add_edge(GENERATE, END)

# app = builder.compile()

# app.get_graph().draw_mermaid_png(
#     output_file_path="nutrition_agentic_rag_graph_1.png")

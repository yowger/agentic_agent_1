from ddgs import DDGS
from dotenv import load_dotenv
from langgraph.graph import START, END, StateGraph

# Initialize client and run a text search
# results = DDGS().text("whats a dog", max_results=5)

# print(results)

from typing import TypedDict
from langchain_core.documents import Document


class AgentState(TypedDict):
    question: str
    documents: list[Document]
    nutrition_data: dict
    generation: str
    retry_count: int
    decision: str


def retrieve_data_node(state: AgentState):
    print("--- RETRIEVE ---")

    return {
        "documents": [],
    }


def grade_documents_node(state: AgentState):
    print("--- GRADE DOCUMENTS ---")

    return {}


def rewrite_question_node(state: AgentState):
    print("--- REWRITE QUESTION ---")

    return {
        "retry_count": state["retry_count"] + 1,
    }


def generate_answer_node(state: AgentState):
    print("--- GENERATE ---")

    return {
        "generation": "Placeholder answer",
    }


def nutrition_api_node(state: AgentState):
    print("nutrition api search")

    pass


def route_decision_node(state: AgentState):
    print("--- Decide node ---")

    return {
        "decision": "pass"
    }


def evaluator_node(state: AgentState):
    "check if suffiecent answer otherwise research again"

    pass


RETRIEVE = "retrieve"
GRADE_DOCUMENTS = "grade_documents"
GENERATE = "generate"
NUTRITION_API = "nutrition_api"

builder = StateGraph(AgentState)

builder.add_node(RETRIEVE, retrieve_data_node)
builder.add_node(GRADE_DOCUMENTS, grade_documents_node)
builder.add_node(GENERATE, generate_answer_node)
builder.add_node(NUTRITION_API, nutrition_api_node)

builder.add_conditional_edges(
    START,
    route_decision_node,
    {
        RETRIEVE: RETRIEVE,
        NUTRITION_API: NUTRITION_API,
    }
)
builder.add_conditional_edges(
    retrieve_data_node,
    {
        # regenerate node?
    }
)


app = builder.compile()

app.get_graph().draw_mermaid_png(
    output_file_path="nutrition_agentic_rag_graph_1.png")

# from pathlib import Path

# from agentic_agent_1.vector_stores.chroma import get_vectorstore
# from agentic_agent_1.config.paths import CHROMA_DIRECTORY


# vectorstore = get_vectorstore(CHROMA_DIRECTORY)

# print(vectorstore)

# results = vectorstore.get(
#     where={
#         "source_id": "who_carbohydrate_intake_adults_children_2023"
#     },
#     include=["metadatas", "documents"]
# )

# print("Total stored chunks:", len(results["ids"]))
# print("First chunk:", results["documents"][0])

# TODO

from langgraph.runtime import Runtime

from agentic_agent_1.graph.state import AgentState
from agentic_agent_1.graph.context import GraphContext


def retrieve_node(state: AgentState, runtime: Runtime[GraphContext]) -> AgentState:
    print("--- RETRIEVE NODE ---")

    vectorstore = runtime.context["vectorstore"]

    question = state["question"]

    documents = vectorstore.similarity_search(
        query=question,
        k=4
    )

    return {
        "documents": documents
    }

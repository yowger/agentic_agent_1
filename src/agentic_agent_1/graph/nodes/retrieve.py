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


def build_metadata_filter(
    organization: str | None = None,
    publication_year: int | None = None,
):
    conditions = []

    if organization:
        conditions.append({
            "organization": organization
        })

    if publication_year is not None:
        conditions.append({
            "publication_year": publication_year
        })

    if not conditions:
        return None

    if len(conditions) == 1:
        return conditions[0]

    return {
        "$and": conditions
    }


def retrieve_node(state: AgentState, runtime: Runtime[GraphContext]) -> AgentState:
    print("--- RETRIEVE NODE ---")

    vectorstore = runtime.context["vectorStore"]

    question = state["question"]
    extracted_filter = state["metadata_filter"]

    metadata_filter = build_metadata_filter(
        organization=extracted_filter.organization,
        publication_year=extracted_filter.publication_year,
    )

    documents = vectorstore.similarity_search(
        query=question,
        k=4,
        filter=metadata_filter,
    )

    return {
        "documents": documents
    }

import asyncio
from agentic_agent_1.graph.state import AgentState

from agentic_agent_1.chains.retrieval_grader import retrieval_grader


async def grade_documents(state: AgentState) -> AgentState:
    question = state["question"]
    documents = state["documents"]

    grading_inputs = [
        {
            "question": question,
            "document": document.page_content
        }
        for document in documents
    ]

    scores = await retrieval_grader.abatch(
        grading_inputs,
        config={
            "max_concurrency": 5
        },
    )

    relevant_documents = []

    for document, score in zip(documents, scores):
        grade = score.binary_score

        print(f"Document: {document.metadata.get('source_id')}")
        print(f"Grade: {grade}")
        print(f"Document: {document.page_content}")


        if grade.lower() == "yes":
            relevant_documents.append(document)

    return {
        "documents": relevant_documents
    }

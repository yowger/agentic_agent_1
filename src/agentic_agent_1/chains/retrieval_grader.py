from langchain_core.prompts import ChatPromptTemplate

from agentic_agent_1.graph.schemas.grade_documents import GradeDocuments
from agentic_agent_1.llms.models import grader_llm

system_prompt = """You are a grader assessing relevance of a retrieved document to a user question.
If the document contains keyword(s) or semantic meaning related to the question, grade it as relevant.
Give a binary score 'yes' or 'no' to indicate whether the document is relevant to the question."""

grade_prompt = ChatPromptTemplate(
    [
        ("system", system_prompt),
        ("human",
         "Retrieved document: \n\n {document} \n\n User question: {question}"),
    ]
)

structured_llm_grader = grader_llm.with_structured_output(GradeDocuments)

retrieval_grader = grade_prompt | structured_llm_grader
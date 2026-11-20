from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from agentic_agent_1.graph.state import AgentState
from agentic_agent_1.config.settings import settings

llm = ChatOpenAI(
    api_key=settings.OPENAI_API_KEY,
    model=settings.LLM_MODEL,
    temperature=0
)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are a helpful assistant.

Answer the user's question using the provided context.

Rules:
- Use the context as your primary source of information.
- Do not invent facts that are not supported by the context.
- If the context does not contain enough information,
    clearly say so.
- If multiple sources provide information, combine them
    into a clear and coherent answer.
- Answer naturally and avoid unnecessary technical language.
        """
    ),
    (
        "human",
        """
Question: {question}

Context: {context}
        """
    )
])


def generate_node(state: AgentState) -> AgentState:
    print("--- GENERATE NODE ---")

    question = state["question"]
    context = state.get("aggregated_context", {})

    documents = context.get("documents", [])
    nutrition_data = context.get("nutrition_data")

    document_context = ""

    for i, doc in enumerate(documents, start=1):
        metadata = doc.metadata

        title = metadata.get("title", "Unknown title")
        organization = metadata.get("organization", "Unknown organization")
        page = metadata.get("page_label", "Unknown page")

        document_context += (
            f"\n[Document {i}]\n"
            f"Title: {title}\n"
            f"Organization: {organization}\n"
            f"Page: {page}\n"
            f"Content: {doc.page_content}\n"
        )

    nutrition_context = ""

    if nutrition_data:
        nutrition_context = f"\nNutrition Data:\n{nutrition_data}"

    formatted_context = (
        f"Retrieved Documents:\n{document_context}\n"
        f"{nutrition_context}"
    )

    chain = prompt | llm

    response = chain.invoke({
        "question": question,
        "context": formatted_context
    })

    return {
        "generation": response.content
    }

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
    context = state.get("aggregated_context", "")

    chain = prompt | llm

    response = chain.invoke({
        "question": question,
        "context": context
    })

    return {
        "generation": response.content
    }

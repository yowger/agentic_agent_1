from langchain.messages import SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from agentic_agent_1.config.settings import settings
from agentic_agent_1.graph.schemas.router import RouteDecision
from agentic_agent_1.graph.state import AgentState

llm = ChatOpenAI(
    api_key=settings.OPENAI_API_KEY,
    model=settings.ROUTER_MODEL,
    temperature=0
)

structured_llm_router = llm.with_structured_output(RouteDecision)


router_system_msg = """
You are a router for a food and nutrition assistant.

Select all data sources needed to answer the user's question.

Available routes:

- retrieve: General nutrition knowledge, explanations, health benefits,
  risks, dietary guidelines, and how nutrients affect the body.

- nutrition_api: Specific food nutrition values, including calories,
  protein, carbohydrates, fats, vitamins, and minerals.

Rules:
- General knowledge or explanations → retrieve.
- Specific nutrient amounts or food nutrition values → nutrition_api.
- Both knowledge and nutrient values → both.
- Always select at least one route.
"""


router_prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content=router_system_msg),
        ("human", "{question}")
    ]
)

question_router = router_prompt | structured_llm_router


def route_decision_node(state: AgentState):
    print("--- ROUTE DECISION ---")

    question = state["question"]

    decision: RouteDecision = question_router.invoke({"question": question})

    print("Selected routes:", decision.routes)

    return {"routes": decision.routes}

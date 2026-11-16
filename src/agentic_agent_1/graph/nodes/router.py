from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv

from agentic_agent_1.graph.state import AgentState
from agentic_agent_1.graph.schemas.router import RouteDecision

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

structured_llm_router = llm.with_structured_output(RouteDecision)


router_system_msg = """
 You are a routing assistant for a food and nutrition knowledge assistant.

Decide which data sources are needed to answer the question.

Available routes:

1. retrieve:
    Use for nutrition knowledge, explanations, dietary
    guidelines, health effects of foods, and general
    educational questions.

2. nutrition_api:
    Use for specific food nutrient information such as
    calories, protein, carbohydrates, fat, vitamins,
    and minerals.

Rules:
- Choose retrieve for general nutrition knowledge.
- Choose nutrition_api for specific food nutrient values.
- Choose both when the question needs both knowledge
    and nutrient information.
- Always select at least one route.
"""


router_prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content=router_system_msg),
    HumanMessage(content="{question}")
])

question_router = router_prompt | structured_llm_router


def route_decision_node(state: AgentState):
    print("__ROUTE_DECISION___")

    question = state["question"]

    decision: RouteDecision = question_router.invoke({
        "question": question
    })

    print("Selected routes:", decision.routes)

    return {
        "routes": decision.routes
    }

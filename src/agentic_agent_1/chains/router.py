from langchain.messages import SystemMessage
from langchain_core.prompts import ChatPromptTemplate

from agentic_agent_1.graph.schemas.router import RouteDecision
from agentic_agent_1.llms.models import router_llm

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

structured_llm_router = router_llm.with_structured_output(RouteDecision)


question_router_chain = router_prompt | structured_llm_router

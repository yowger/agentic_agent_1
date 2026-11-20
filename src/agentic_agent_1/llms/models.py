from langchain_openai import ChatOpenAI

from agentic_agent_1.config.settings import settings

router_llm = ChatOpenAI(
    api_key=settings.OPENAI_API_KEY,
    model=settings.ROUTER_MODEL,
    temperature=0
)

generate_llm = ChatOpenAI(
    api_key=settings.OPENAI_API_KEY,
    model=settings.GENERATOR_MODEL,
    temperature=0
)
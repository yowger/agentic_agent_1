from langchain_core.prompts import ChatPromptTemplate

from agentic_agent_1.llms.models import generate_llm

system_prompt = """
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

generate_prompt = ChatPromptTemplate.from_messages([
    (
        "system", system_prompt  
    ),
    (
        "human",
        """Question: {question} \n\n Context: \n\n {context}
        """
    )
])

generation_chain = generate_prompt | generate_llm

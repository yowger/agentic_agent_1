from agentic_agent_1.graph.graph import app

result = app.invoke({
    "question": "Why does the body need carbohydrates?"
})

print("\n--- ANSWER ---")
print(result)

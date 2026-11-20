from agentic_agent_1.chains.router import question_router_chain

test_cases = [
    {
        "question": "What are carbohydrates?",
        "expected": ["retrieve"],
    },
    {
        "question": "How much protein is in two large eggs?",
        "expected": ["nutrition_api"],
    },
    {
        "question": "What are the health benefits of eggs?",
        "expected": ["retrieve"],
    },
    {
        "question": "What are the health benefits of eggs and how much protein do they contain?",
        "expected": ["retrieve", "nutrition_api"],
    },
    {
        "question": "How many calories are in 100g of chicken breast?",
        "expected": ["nutrition_api"],
    },
    {
        "question": "Is chicken breast healthy and how much protein does it contain?",
        "expected": ["retrieve", "nutrition_api"],
    },
]


for test in test_cases:
    result = question_router_chain.invoke({"question": test["question"]})

    actual = set(result.routes)
    expected = set(test["expected"])

    passed = actual == expected

    print("Workflow state:", result)
    print(f"\nQuestion: {test['question']}")
    print(f"Expected: {expected}")
    print(f"Actual:   {actual}")
    print(f"Result:   {'PASS' if passed else 'FAIL'}")

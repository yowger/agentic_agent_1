
import pytest

from agentic_agent_1.chains.router import question_router_chain


test_cases = [
    (
        "What are carbohydrates?",
        ["retrieve"],
    ),
    (
        "How much protein is in two large eggs?",
        ["nutrition_api"],
    ),
    (
        "What are the health benefits of eggs?",
        ["retrieve"],
    ),
    (
        "What are the health benefits of eggs and how much protein do they contain?",
        ["retrieve", "nutrition_api"],
    ),
    (
        "How many calories are in 100g of chicken breast?",
        ["nutrition_api"],
    ),
    (
        "Is chicken breast healthy and how much protein does it contain?",
        ["retrieve", "nutrition_api"],
    ),
]


@pytest.mark.parametrize(
    "question, expected",
    test_cases,
)
def test_router_routes(question, expected):
    result = question_router_chain.invoke({
        "question": question
    })

    actual = set(result.routes)
    expected = set(expected)

    assert actual == expected

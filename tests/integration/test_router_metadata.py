import pytest

from agentic_agent_1.chains.router import question_router_chain


test_cases = [
    (
        "What is trans fat?",
        ["retrieve"],
        None,
        None,
    ),
    (
        "What is trans fat according to WHO?",
        ["retrieve"],
        "WHO",
        None,
    ),
    (
        "What is trans fat? Check 2023 books.",
        ["retrieve"],
        None,
        2023,
    ),
    (
        "What does WHO recommend about trans fat in 2023?",
        ["retrieve"],
        "WHO",
        2023,
    ),
    (
        "What are the health risks of trans fat?",
        ["retrieve"],
        None,
        None,
    ),
]


@pytest.mark.parametrize(
    "question, expected_routes, expected_org, expected_year",
    test_cases,
)
def test_router_metadata(
    question,
    expected_routes,
    expected_org,
    expected_year,
):
    result = question_router_chain.invoke({
        "question": question
    })

    assert set(result.routes) == set(expected_routes)

    assert result.metadata_filter.organization == expected_org

    assert result.metadata_filter.publication_year == expected_year
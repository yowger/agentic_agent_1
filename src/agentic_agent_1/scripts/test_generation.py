from rich import print
from rich.panel import Panel
from rich.pretty import Pretty

from agentic_agent_1.graph.graph import app
from agentic_agent_1.vector_stores.chroma import get_vectorstore

vectorstore = get_vectorstore()

result = app.invoke(
    {
        # "question": "Besides salt, what other foods have sodium?",
        # "question": "what foods have sodium?",
        # "question": "What is trans fat?",
        "question": "What is trans fat? check for 2023 books if any",
        # "question": "What is trans fat?",
    },
    context={
        "vectorStore": vectorstore
    }
)

print("\n[bold green]--- AGGREGATED CONTEXT ---[/bold green]")

print(
    Panel(
        Pretty(result.get("aggregated_context", {}), expand_all=True),
        title="Context",
        border_style="cyan"
    )
)

print("\n[bold green]--- ANSWER ---[/bold green]")

print(
    Panel(
        result["generation"],
        title="Generated Answer",
        border_style="green"
    )
)

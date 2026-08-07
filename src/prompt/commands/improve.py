from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

from prompt.ai.client import AIClient
from prompt.storage.prompts import (
    load_prompt,
)
from prompt.prompts.improver import (
    build_improvement_prompt,
)
from prompt.storage.prompts import (
    maybe_save_prompt,
)

console = Console()

client = AIClient()

PROMPTS_DIR = (
    Path.home()
    / ".prompt"
    / "prompts"
)


def improve(filename: str):
    try:
        original_prompt = load_prompt(
            filename
        )

    except FileNotFoundError as error:
        console.print(
            f"[red]{error}[/red]"
        )
        raise SystemExit(1)

    console.print()

    improvement_request = Prompt.ask(
        "[cyan]What would you like to improve?[/cyan]"
    )

    console.print()

    with console.status(
        "[bold green]Improving prompt...[/bold green]"
    ):
        ai_request = build_improvement_prompt(
            original_prompt,
            improvement_request,
        )

        improved_prompt = (
            client.generate_prompt(
                ai_request
            )
        )

    console.print()

    console.print(
        Panel(
            improved_prompt,
            title="✨ Improved Prompt",
            border_style="green",
        )
    )

    console.print()

    maybe_save_prompt(
        improved_prompt
    )

    display_next_steps()


def display_next_steps():
    console.print()

    console.print(
        Panel(
            """• Test the improved prompt

• Run prompt review on it

• Improve it again if needed

• Save your best version""",
            title="Suggested Next Steps",
            border_style="blue",
        )
    )
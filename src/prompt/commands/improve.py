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
from prompt.ui.improve import display_improved_prompt, display_next_steps

console = Console()

client = AIClient()

PROMPTS_DIR = (
    Path.home()
    / ".prompt"
    / "prompts"
)


def collect_improvement_request() -> str:
    console.print()

    console.print(
        "[italic cyan]🔧 DESCRIBE HOW THE PROMPT SHOULD CHANGE "
        "AND AN AI WILL IMPROVE IT.[/italic cyan]"
    )

    console.print()

    console.print(
        Panel(
            """[bold]What would you like to improve?[/bold]

[yellow]Tip[/yellow]: Describe how you want the prompt to change.

[green]Examples[/green]:

• Make it more suitable for beginners
• Add a structured output format
• Generate more code examples
• Make the response shorter
• Require step-by-step explanations
• Focus on practical learning

[dim]Press Enter to cancel[/dim]""",
            title="Improve Prompt",
            border_style="blue",
        )
    )

    console.print()

    return Prompt.ask(
        "Your answer",
        default="",
    )


def improve_prompt(original_prompt: str, improvement_request: str) -> str:
    with console.status("[bold green]Improving prompt...[/bold green]"):
        ai_request = build_improvement_prompt(
            original_prompt,
            improvement_request,
        )

        improved_prompt = (
            client.generate_prompt(
                ai_request
            )
        )
        
        return improved_prompt


def improve(filename: str):
    
    # Load prompt
    try:
        original_prompt = load_prompt(
            filename
        )

    except FileNotFoundError as error:
        console.print(
            f"[red]{error}[/red]"
        )
        raise SystemExit(1)

    # Collect improvement request
    improvement_request = (
        collect_improvement_request()
    )

    if not improvement_request.strip():
        console.print(
            "\n[yellow]Improvement cancelled.[/yellow]"
        )
        return

    # Improve prompt
    improved_prompt = improve_prompt(original_prompt, improvement_request)

    # Print improved prompt
    display_improved_prompt(improved_prompt)

    # Save prompt
    maybe_save_prompt(
        improved_prompt
    )

    # Display next steps
    display_next_steps()

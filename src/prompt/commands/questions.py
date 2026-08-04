# src/prompt/commands/questions.py

import typer

from rich.console import Console
from rich.panel import Panel

console = Console()


def ask_question(
    *,
    question_number: int,
    total_questions: int,
    question: str,
    tip: str,
    examples: list[str],
) -> str:
    examples_text = "\n".join(
        f"• {example}"
        for example in examples
    )

    panel_content = (
        f"[bold]{question}[/bold]\n\n"
        f"[cyan]Tip:[/cyan] {tip}\n\n"
        f"[green]Examples:[/green]\n"
        f"{examples_text}\n\n"
        f"[dim]Enter to skip[/dim]"
    )
    
    console.print()

    console.print(
        Panel(
            panel_content,
            title=f"Question {question_number} of {total_questions}",
            border_style="blue",
        )
    )

    answer = typer.prompt(
        "  Your answer",
        default="",
        show_default=False,
    )

    console.print()

    return answer
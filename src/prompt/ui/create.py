from rich.console import Console
from rich.panel import Panel

console = Console()

def display_create_intro() -> None:
    """
    Display the create command introduction.
    """

    console.print()

    console.print(
        "💬 [italic cyan]DESCRIBE WHAT YOU NEED AND AN AI WILL GENERATE A STARTING PROMPT.[/italic cyan]"
    )


def display_generated_prompt(
    generated_prompt: str,
) -> None:
    """
    Display the generated prompt.
    """

    console.print()

    console.print(
        Panel(
            generated_prompt,
            title="🤖 Generated Prompt",
            border_style="bold green",
        )
    )

    console.print()


def display_next_steps() -> None:
    """
    Display suggested next actions.
    """

    console.print()

    console.print(
        "[bold cyan]👉 Suggested Next Steps[/bold cyan]"
    )

    console.print()

    console.print(
        "• Use the generated prompt as a starting point."
    )

    console.print()

    console.print(
        "• Try generating the prompt with a different model:"
    )
    console.print(
            "  [green]prompt create --model <model-name>[/green]"
        )

    console.print()

    console.print(
        "• Improve a saved prompt:"
    )
    console.print(
        "  [green]prompt improve <prompt-file>[/green]"
    )

    console.print()

    console.print(
        "• Review a saved prompt:"
    )
    console.print(
        "  [green]prompt review <prompt-file>[/green]"
    )

    console.print()
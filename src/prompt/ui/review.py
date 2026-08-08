from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

def display_review_intro() -> None:
    """
    Display introduction.
    """

    console = Console()

    console.print()

    console.print(
        "🔍 [italic cyan]REVIEWING PROMPT[/italic cyan]"
    )

    console.print()


def display_review(
    review: str,
) -> None:
    """
    Display prompt review.
    """

    console = Console()

    console.print()

    console.print(
        Panel(
            Markdown(review),
            title="📝 Prompt Review",
            border_style="bold blue",
            padding=(1, 1)
        )
    )

    console.print()
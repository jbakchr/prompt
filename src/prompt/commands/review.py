from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from yaspin import yaspin

from prompt.ai.client import AIClient
from prompt.prompts.reviewer import (
    build_prompt_review_request,
)
from prompt.storage.prompts import (
    load_prompt,
)


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


def load_existing_prompt(
    filename: str,
) -> str:
    """
    Load prompt from storage.
    """

    return load_prompt(
        filename
    )


def generate_review(
    prompt: str,
) -> str:
    """
    Generate review using AI.
    """

    request = build_prompt_review_request(
        prompt
    )

    client = AIClient()

    with yaspin(
        text="🔍 Reviewing prompt...",
        color="cyan",
    ) as spinner:

        review = client.generate_prompt(
            request
        )

        spinner.text = "Review complete"
        spinner.ok("✅")

    return review


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

def review(
    filename: str,
) -> None:
    """
    Review a saved prompt.
    """

    display_review_intro()

    prompt = load_existing_prompt(
        filename
    )

    review_result = generate_review(
        prompt
    )

    display_review(
        review_result
    )
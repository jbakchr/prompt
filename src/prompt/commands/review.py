from yaspin import yaspin

from prompt.ui.review import (
    display_review_intro,
    display_review
)
from prompt.ai.client import AIClient
from prompt.prompts.reviewer import (
    build_prompt_review_request,
)
from prompt.storage.prompts import (
    load_prompt,
)


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
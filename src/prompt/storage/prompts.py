from pathlib import Path

from rich.console import Console
from rich.prompt import Confirm
from rich.prompt import Prompt

def maybe_save_prompt(
    generated_prompt: str,
) -> None:
    """
    Offer to save the generated prompt.
    """

    console = Console()

    save_prompt = Confirm.ask(
        "Would you like to save this prompt?",
        default=False,
    )

    if not save_prompt:
        return

    filename = Prompt.ask(
        "Filename",
        default="prompt.md",
    )

    prompts_directory = (
        Path.home()
        / ".prompt"
        / "prompts"
    )

    prompts_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    file_path = prompts_directory / filename

    file_path.write_text(
        generated_prompt,
        encoding="utf-8",
    )

    console.print()

    console.print(
        f"✅ Prompt saved to [green]{file_path}[/green]"
    )

    console.print()
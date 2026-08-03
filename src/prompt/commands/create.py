import typer

from prompt.ai.client import AIClient
from prompt.prompts.builder import build_prompt_generation_request


def create() -> None:
    """
    Create a new prompt.
    """

    typer.echo()
    typer.echo("Let's create a prompt.")
    typer.echo()

    goal = typer.prompt(
        "What should the AI do?",
        default="",
        show_default=False,
    )

    audience = typer.prompt(
        "Who is the intended audience?",
        default="",
        show_default=False,
    )

    role = typer.prompt(
        "What role should the AI take on?",
        default="",
        show_default=False,
    )

    instructions = typer.prompt(
        "Any specific instructions?",
        default="",
        show_default=False,
    )

    output_format = typer.prompt(
        "Desired output format?",
        default="",
        show_default=False,
    )

    request = build_prompt_generation_request(
        goal=goal,
        audience=audience,
        role=role,
        instructions=instructions,
        output_format=output_format,
    )

    client = AIClient()

    try:
        prompt_text = client.generate_prompt(request)

    except RuntimeError as error:
        typer.echo(
            f"Error: {error}",
            err=True,
        )
        raise typer.Exit(code=1)

    typer.echo()
    typer.echo("=" * 60)
    typer.echo("Generated Prompt")
    typer.echo("=" * 60)
    typer.echo()
    typer.echo(prompt_text)
    typer.echo()
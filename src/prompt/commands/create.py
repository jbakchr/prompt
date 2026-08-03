import typer

from prompt.prompts.builder import build_prompt


def create() -> None:
    """
    Create a new prompt.
    """

    typer.echo()
    typer.echo("Let's create a prompt.")
    typer.echo()

    goal = typer.prompt(
        "What is the goal?",
        default="",
        show_default=False,
    )

    audience = typer.prompt(
        "Who is the intended audience?",
        default="",
        show_default=False,
    )

    role = typer.prompt(
        "Should the AI take on a role?",
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

    prompt_text = build_prompt(
        goal=goal,
        audience=audience,
        role=role,
        instructions=instructions,
        output_format=output_format,
    )

    typer.echo()
    typer.echo("=" * 60)
    typer.echo("Generated Prompt")
    typer.echo("=" * 60)
    typer.echo()
    typer.echo(prompt_text)
    typer.echo()
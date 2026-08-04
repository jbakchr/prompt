import typer

from prompt.ai.client import AIClient
from prompt.prompts.builder import build_prompt_generation_request
from prompt.commands.questions import ask_question


def create() -> None:
    """
    Create a new prompt.
    """

    typer.echo()
    typer.echo("Let's create a prompt.")

    goal = ask_question(
        question_number=1,
        total_questions=5,
        question="What should the AI do?",
        tip="Describe the task directly.",
        examples=[
            "Summarize the following article",
            "Review the provided Python code",
            "Create a learning roadmap for FastAPI",
        ],
    )

    audience = ask_question(
        question_number=2,
        total_questions=5,
        question="Who is the intended audience?",
        tip="Be specific about who will read or use the AI output.",
        examples=[
            "Beginner Python developers",
            "Software engineering managers",
            "Open source contributors",
        ],
    )

    role = ask_question(
        question_number=3,
        total_questions=5,
        question="What role should the AI take on?",
        tip="More specific roles usually produce better prompts.",
        examples=[
            "Experienced Python developer",
            "Senior software architect",
            "Technical writing expert",
        ],
    )

    instructions = ask_question(
        question_number=4,
        total_questions=5,
        question="Any specific instructions?",
        tip="Describe any special requirements you'd like the AI to follow.",
        examples=[
            "Use bullet points",
            "Keep the explanation concise",
            "Focus on practical examples",
        ],
    )

    output_format = ask_question(
        question_number=5,
        total_questions=5,
        question="Desired output format?",
        tip="Specify how the AI should structure its response.",
        examples=[
            "Markdown",
            "Markdown bullet points",
            "Plain text",
            "JSON",
        ],
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
from rich.console import Console
from rich.panel import Panel
from yaspin import yaspin

from prompt.ai.client import AIClient
from prompt.commands.questions import ask_question
from prompt.models.prompt_requirements import PromptRequirements
from prompt.prompts.builder import build_prompt_generation_request
from prompt.storage.prompts import maybe_save_prompt


def create() -> None:
    """
    Create a new prompt.
    """

    display_create_intro()

    requirements = collect_prompt_requirements()

    generated_prompt = generate_prompt(
        requirements
    )

    display_generated_prompt(
        generated_prompt
    )

    maybe_save_prompt(
        generated_prompt
    )

    display_next_steps()


def display_create_intro() -> None:
    """
    Display the create command introduction.
    """

    console = Console()

    console.print()

    console.print(
        "💬 [italic cyan]DESCRIBE WHAT YOU NEED AND AN AI WILL GENERATE A STARTING PROMPT.[/italic cyan]"
    )

    console.print()


def collect_prompt_requirements() -> PromptRequirements:
    """
    Ask the user a series of questions and collect
    the information needed to generate a prompt.
    """

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

    return PromptRequirements(
        goal=goal,
        audience=audience,
        role=role,
        instructions=instructions,
        output_format=output_format,
    )


def generate_prompt(
    requirements: PromptRequirements,
) -> str:
    """
    Generate a prompt from the collected requirements.
    """

    request = build_prompt_generation_request(
        goal=requirements.goal,
        audience=requirements.audience,
        role=requirements.role,
        instructions=requirements.instructions,
        output_format=requirements.output_format,
    )

    client = AIClient()

    console = Console()

    console.print()

    with yaspin(
        text="🧠 Generating your prompt...",
        color="cyan",
    ) as spinner:

        generated_prompt = client.generate_prompt(
            request
        )

        spinner.text = "Prompt generated"
        spinner.ok("✅")

    return generated_prompt


def display_generated_prompt(
    generated_prompt: str,
) -> None:
    """
    Display the generated prompt.
    """

    console = Console()

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

    console = Console()

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
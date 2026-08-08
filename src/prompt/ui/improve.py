from rich.console import Console
from rich.panel import Panel

console = Console()

def display_improved_prompt(improved_prompt: str) -> None:
    """Displayes improved prompt"""
    
    console.print()

    console.print(
        Panel(
            improved_prompt,
            title="✨ Improved Prompt",
            border_style="green",
        )
    )

    console.print()


def display_next_steps():
    console.print()

    console.print(
        Panel(
            """• Test the improved prompt

• Run prompt review on it

• Improve it again if needed

• Save your best version""",
            title="Suggested Next Steps",
            border_style="blue",
        )
    )
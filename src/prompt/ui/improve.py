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
        "[bold cyan]👉 Suggested Next Steps[/bold cyan]"
    )

    # Test prompt
    console.print()

    console.print(
        "• Test the improved prompt."
    )
    
    # Review prompt
    console.print()

    console.print(
        "• Run prompt review on it."
    )
    console.print(
        "  [green]prompt review <prompt-file>[/green]"
    )
    
    # Improve prompt
    console.print()

    console.print(
        "• Improve it again if needed."
    )
    console.print(
            "  [green]prompt improve <prompt-file>[/green]"
        )
    
    console.print()
    

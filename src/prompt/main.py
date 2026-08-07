import typer

from prompt.commands.create import (
    create as create_command,
)
from prompt.commands.improve import (
    improve as improve_command,
)
from prompt.commands.review import (
    review as review_command,
)

app = typer.Typer(
    help="Create, improve and review AI prompts."
)


@app.callback()
def callback():
    pass


@app.command(name="create")
def create():
    create_command()


@app.command(name="review")
def review(
    filename: str,
):
    review_command(filename)


@app.command(name="improve")
def improve(
    filename: str,
):
    improve_command(filename)


if __name__ == "__main__":
    app()
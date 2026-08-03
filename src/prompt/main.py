import typer

from prompt.commands.create import create as create_command

app = typer.Typer(
    help="Create, improve and review AI prompts."
)


@app.callback()
def callback():
    pass


@app.command(name="create")
def create():
    create_command()

if __name__ == "__main__":
    app()

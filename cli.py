import typer
from .remove import remove

app = typer.Typer()


@app.command()
def hello(name: str):
    print(f"Hello {name}")


@app.command()
def gnit():
    """TODO:
    """
@app.command()
def remove(repo_name: str):
    remove(repo_name=repo_name)

if __name__ == "__main__":
    app()

import click


@click.group()
def cli():
    """Command line utility for python-app."""
    pass


@cli.command()
@click.option("--name", default="World", help="Who to greet")
def hello(name):
    """Simple command that greets the user."""
    click.echo(f"Hello, {name}!")


if __name__ == "__main__":
    cli()

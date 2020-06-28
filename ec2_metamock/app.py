import click
from . import app


@click.command()
@click.option("--host", default="localhost", help="Server host")
@click.option("--port", default=8080, help="Server port")
@click.option("--debug", default=False, help="Debug mode", is_flag=True)
def run(host, port, debug):
    app.run(host=host, port=port, debug=debug)

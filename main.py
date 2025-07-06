import typer
from commands.stats import stats_parser
from commands.rmpg import rmpg_parser

app = typer.Typer()

@app.command()
def stats(file: str):
	stats_parser(file)

@app.command()
def rmpg(
	file: str = typer.Argument(..., help="Input PDF file"),
	pages: list[str] = typer.Argument(..., help="Pages to remove (e.g. 1 2 4-6)"),
	output: str = typer.Option(None, "--output", "-out", help="Output file path"),
	overwrite: bool = typer.Option(False, "--overwrite", "-o", help="Overwrite input file"),
):
	rmpg_parser(file, pages, output, overwrite)

if __name__ == "__main__":
	app()

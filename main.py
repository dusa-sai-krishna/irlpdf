import typer
from commands.stats import stats_parser
from commands.rmpg import rmpg_parser
from commands.encrypt import encrypt_parser
from commands.decrypt import decrypt_parser
from commands.split import split_parser
from commands.merge import merge_parser

app = typer.Typer()

@app.command()
def merge(
	files: list[str] = typer.Argument(None),
	directory: str = typer.Option(None, "--directory", "-d"),
):
	merge_parser(files, directory)

@app.command()
def rmpg(
	file: str = typer.Argument(...),
	pages: list[str] = typer.Argument(...),
	output: str = typer.Option(None, "--output", "-out"),
	overwrite: bool = typer.Option(False, "--overwrite", "-o"),
):
	rmpg_parser(file, pages, output, overwrite)

@app.command()
def split(
	file: str = typer.Argument(...),
	breakpoints: list[str] = typer.Argument(...),
):
	split_parser(file, breakpoints)

@app.command()
def stats(
    file: str = typer.Argument(...)
):
	stats_parser(file)

@app.command()
def encrypt(
	file: str = typer.Argument(...),
	output: str = typer.Option(None, "--output", "-out"),
	overwrite: bool = typer.Option(False, "--overwrite", "-o"),
):
	encrypt_parser(file, output, overwrite)

@app.command()
def decrypt(
	file: str = typer.Argument(...),
	output: str = typer.Option(None, "--output", "-out"),
	overwrite: bool = typer.Option(False, "--overwrite", "-o")
):
	decrypt_parser(file, output, overwrite)
if __name__ == "__main__":
	app()

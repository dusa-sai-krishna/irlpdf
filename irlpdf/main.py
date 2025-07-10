import typer
from irlpdf.commands.stats import stats_parser
from irlpdf.commands.rmpg import rmpg_parser
from irlpdf.commands.encrypt import encrypt_parser
from irlpdf.commands.decrypt import decrypt_parser
from irlpdf.commands.split import split_parser
from irlpdf.commands.merge import merge_parser
from irlpdf.commands.compress import compress_parser
from irlpdf.commands.man import man_parser

app = typer.Typer()


@app.command()
def compress(
	files: list[str] = typer.Argument(None),
	directory: str = typer.Option(None, "--directory", "-d")
):
	compress_parser(files, directory)

@app.command()
def man(command: str = typer.Argument(...)):
	man_parser(command)

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

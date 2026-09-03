import socket

import typer
from rich.console import Console
from rich.table import Table


app = typer.Typer(no_args_is_help=True)
console = Console()


@app.callback()
def main() -> None:
    """Scan ports on your own machine or authorized lab hosts."""


@app.command()
def scan(
    host: str = typer.Argument(..., help="Host to scan."),
    ports: str = typer.Option("22,80,443", "--ports", help="Comma-separated ports."),
) -> None:
    table = Table(title=f"Port Scan: {host}")
    table.add_column("Port")
    table.add_column("Open")
    for raw_port in ports.split(","):
        port = int(raw_port.strip())
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.5)
                open_ = sock.connect_ex((host, port)) == 0
        except socket.gaierror:
            console.print(f"[red]Could not resolve host:[/red] {host}")
            raise typer.Exit(code=1)
        table.add_row(str(port), "[green]yes[/green]" if open_ else "[red]no[/red]")
    console.print(table)

"""Command-line interface for the robot project.

This intentionally stays thin: it calls into the library modules that can be used
by a GUI later.
"""

from __future__ import annotations

import typer

from rg4l_robot import __version__

app = typer.Typer(add_completion=False, no_args_is_help=True)


@app.command()
def status() -> None:
    """Print a quick project status message."""

    typer.echo(f"rg4l_robot {__version__} is installed and the CLI is working.")


@app.command()
def connect(
    port: str = typer.Option("COM3", help="Serial port, e.g. COM3 (Windows) or /dev/ttyACM0."),
    baud: int = typer.Option(115200, help="Serial baud rate."),
) -> None:
    """Try to open a serial connection to the Arduino and print a handshake."""

    from rg4l_robot.comms.serial_link import SerialLink

    with SerialLink(port=port, baud=baud) as link:
        link.write_line("PING 1")
        resp = link.read_line(timeout_s=1.0)
        typer.echo(f"Arduino responded: {resp!r}")


@app.command()
def version() -> None:
    """Print version."""

    typer.echo(__version__)


if __name__ == "__main__":
    app()



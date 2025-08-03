"""Entry points for initial_repository_template."""

import os
import sys

import click

sys.path.append(os.getcwd())  # noqa: PTH109
from folder_sync import cli


def _main() -> None:
    """Gathers all entry points of the program."""

    @click.group(chain=True)
    def entry_point() -> None:
        """Entry point."""

    for command in (cli.pipeline,):
        entry_point.add_command(command)

    entry_point()

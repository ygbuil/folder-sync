"""Entry points for initial_repository_template."""

import os
import sys

import click

sys.path.append(os.getcwd())  # noqa: PTH109
from folder_sync import entry_points  # noqa: E402


def _main() -> None:
    """Gathers all entry points of the program."""

    @click.group(chain=True)
    def entry_point() -> None:
        """Entry point."""

    for command in (entry_points.pipeline,):
        entry_point.add_command(command)

    entry_point()


if __name__ == "__main__":
    _main()

from pathlib import Path
from typing import Literal

import click
from loguru import logger

from folder_sync import objects


@click.command()
@click.option("--origin-root-path")
@click.option("--destination-root-path")
def pipeline(origin_root_path: str, destination_root_path: str) -> str:
    """Entry point for _pipeline().

    :param origin_root_path: Root path of the origin folder.
    :param destination_root_path: Root path of the destination folder.
    :returns: None.
    """
    return _pipeline(origin_root_path, destination_root_path)


def _pipeline(
    origin_root_path: str,
    destination_root_path: str,
) -> tuple[Literal[0, 1], str]:
    """Entire pipeline. Checks differences between origin and destination folders and
    sets destination to be in the same status as origin.

    :param origin_root_path: Root path of the origin folder.
    :param destination_root_path: Root path of the destination folder.
    :returns: None.
    """
    origin_root_path, destination_root_path = (
        Path(origin_root_path),
        Path(destination_root_path),
    )

    origin_child_paths, destination_child_paths = (
        objects.get_sub_paths(path=origin_root_path),
        objects.get_sub_paths(path=destination_root_path),
    )

    # delete destination files not present in origin
    paths_to_delete = objects.get_paths_to_delete(
        origin_child_paths=origin_child_paths,
        destination_child_paths=destination_child_paths,
    )
    objects.delete_paths(
        paths_to_delete=paths_to_delete,
        destination_root_path=destination_root_path,
    )

    # copy files present in origin but not in destination
    destination_child_paths = objects.get_sub_paths(path=destination_root_path)
    paths_to_copy = objects.get_paths_to_copy(
        origin_child_paths=origin_child_paths,
        destination_child_paths=destination_child_paths,
    )
    objects.copy_paths(
        origin_root_path=origin_root_path,
        destination_root_path=destination_root_path,
        paths_to_copy=paths_to_copy,
    )

    exit_code, exit_message = objects.test_if_sucessful(
        origin_root_path=origin_root_path,
        destination_root_path=destination_root_path,
    )

    logger.info(f"{exit_code}. {exit_message}")

    return exit_code, exit_message

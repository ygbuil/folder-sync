from pathlib import Path
from typing import Literal

import click
from loguru import logger

from backend import objects


@click.command()
@click.option("--origin-root-path")
@click.option("--destination-root-path")
def pipeline(origin_root_path: str, destination_root_path: str) -> str:
    """Entry point to say hello.

    :param name: Name.
    :param surname: Surname.
    :return: Greet.
    """
    return _pipeline(origin_root_path, destination_root_path)


def _pipeline(
    origin_root_path: str,
    destination_root_path: str,
    trigger_object=None,
) -> tuple[Literal[0, 1], str]:
    """Entire pipeline. Checks differences between master and clone folder and
    sets clone to be in the same status as master.

    Parameters
    ----------
    origin_root_path : str
        Root path of master folder.
    destination_root_path : str
        Root path of clone folder.

    Returns
    -------
    None.

    """
    # fake start for the progress bar
    if trigger_object:
        objects.update_progress_bar_fake(steps=10, trigger_object=trigger_object)

    origin_root_path, destination_root_path = (
        Path(origin_root_path),
        Path(destination_root_path),
    )

    # get all sub paths
    origin_sub_paths = objects.get_sub_paths(path=origin_root_path)
    destination_sub_paths = objects.get_sub_paths(path=destination_root_path)

    # delete clone files not present in master
    paths_to_delete = objects.get_paths_paths_to_delete(
        origin_sub_paths=origin_sub_paths,
        destination_sub_paths=destination_sub_paths,
    )
    objects.delete_paths(
        paths_to_delete=paths_to_delete,
        destination_root_path=destination_root_path,
        trigger_object=trigger_object,
    )

    # copy files present in master but not in clone
    destination_sub_paths = objects.get_sub_paths(path=destination_root_path)
    paths_to_copy = objects.get_paths_to_copy(
        origin_sub_paths=origin_sub_paths,
        destination_sub_paths=destination_sub_paths,
    )
    objects.copy_paths(
        origin_root_path=origin_root_path,
        destination_root_path=destination_root_path,
        paths_to_copy=paths_to_copy,
        trigger_object=trigger_object,
    )

    # check if both folders are equal
    exit_code, exit_message = objects.test_if_sucessful(
        origin_root_path=origin_root_path,
        destination_root_path=destination_root_path,
    )

    # fake finish for the progress bar
    if trigger_object:
        objects.update_progress_bar_fake(steps=9, trigger_object=trigger_object)

    logger.info(f"{exit_code}. {exit_message}")

    return exit_code, exit_message

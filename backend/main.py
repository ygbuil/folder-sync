# libraries
from pathlib import Path

# local libraries test
from . import objects


def main(origin_root_path, destination_root_path):
    """
    Entire pipeline. Checks differences between master and clone folder and
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
        paths_to_delete=paths_to_delete, destination_root_path=destination_root_path
    )

    # copy files present in master but not in clone
    destination_sub_paths = objects.get_sub_paths(path=destination_root_path)
    paths_to_copy = objects.get_paths_to_copy(
        origin_sub_paths=origin_sub_paths, destination_sub_paths=destination_sub_paths
    )
    objects.copy_paths(
        origin_root_path=origin_root_path,
        destination_root_path=destination_root_path,
        paths_to_copy=paths_to_copy,
    )

    # check if both folders are equal
    exit_code, exit_message = objects.test_if_sucessful(
        origin_root_path=origin_root_path, destination_root_path=destination_root_path
    )

    return exit_code, exit_message

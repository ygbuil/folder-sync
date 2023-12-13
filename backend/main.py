# libraries
from pathlib import Path

# local libraries
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

    origin_root_path = Path(origin_root_path)
    destination_root_path = Path(destination_root_path)

    # get all sub paths
    master_sub_paths, clone_sub_paths = objects.get_sub_paths(
        origin_root_path=origin_root_path, destination_root_path=destination_root_path
    )

    # delete clone files not present in master
    objects.delete_clone_files(
        master_sub_paths=master_sub_paths,
        clone_sub_paths=clone_sub_paths,
        destination_root_path=destination_root_path,
    )

    # copy files present in master but not in clone
    objects.copy_from_master_to_clone(
        origin_root_path=origin_root_path,
        destination_root_path=destination_root_path,
        master_sub_paths=master_sub_paths,
    )

    # check if both folders are equal
    exit_code, exit_message = objects.test_if_sucessful(
        origin_root_path=origin_root_path, destination_root_path=destination_root_path
    )

    return exit_code, exit_message

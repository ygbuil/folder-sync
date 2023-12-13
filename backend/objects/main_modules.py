# local libraries
from . import objects


def get_sub_paths(origin_root_path, destination_root_path):
    """
    Get all the sub paths inside path.

    Parameters
    ----------
    origin_root_path : pathlib object
        Root path of master folder.
    destination_root_path : pathlib object
        Root path of clone folder.

    Returns
    -------
    master_sub_paths : dict
        Dictionary containing sub paths for master.
    clone_sub_paths : dict
        Dictionary containing sub paths for clone.

    """

    master_sub_paths = objects.get_sub_paths(path=origin_root_path)
    clone_sub_paths = objects.get_sub_paths(path=destination_root_path)

    return master_sub_paths, clone_sub_paths


def delete_clone_files(master_sub_paths, clone_sub_paths, destination_root_path):
    """
    Delete files present in clone but missing in master.

    Parameters
    ----------
    master_sub_paths : dict
        Dictionary containing sub paths for master.
    clone_sub_paths : dict
        Dictionary containing sub paths for clone.
    destination_root_path : pathlib object
        Root path of clone folder.

    Returns
    -------
    None.

    """

    # get lists of paths to delete
    paths_to_delete = objects.get_paths_paths_to_delete(
        master_sub_paths=master_sub_paths,
        clone_sub_paths=clone_sub_paths,
        destination_root_path=destination_root_path,
    )

    # delete paths
    objects.delete_paths(paths_to_delete=paths_to_delete)


def copy_from_master_to_clone(
    origin_root_path, destination_root_path, master_sub_paths
):
    """
    Copy files present in master but missing in clone (from master to clone).

    Parameters
    ----------
    origin_root_path : pathlib object
        Root path of master folder.
    destination_root_path : pathlib object
        Root path of clone folder.
    master_sub_paths : dict
        Dictionary containing sub paths for master.

    Returns
    -------
    None.

    """

    # get clone_sub_paths again, since deletitions may have just been performed
    clone_sub_paths = objects.get_sub_paths(path=destination_root_path)

    # copy from master to clone
    paths_to_copy = objects.get_paths_to_copy(
        master_sub_paths=master_sub_paths, clone_sub_paths=clone_sub_paths
    )

    objects.copy_paths(
        origin_root_path=origin_root_path,
        destination_root_path=destination_root_path,
        paths_to_copy=paths_to_copy,
    )


def test_if_sucessful(origin_root_path, destination_root_path):
    """
    Checks if the process went successfully, that is, master and clone folders
    are equal after all the change.

    Parameters
    ----------
    origin_root_path : pathlib object
        Root path of master folder.
    destination_root_path : pathlib object
        Root path of clone folder.

    Returns
    -------
    None.

    """

    master_sub_paths = objects.get_sub_paths(path=origin_root_path)
    clone_sub_paths = objects.get_sub_paths(path=destination_root_path)

    if master_sub_paths == clone_sub_paths:
        return 0, "Process successful, both folders are now equal!"
    else:
        return 1, "Something went wrong. Origin and destination folders are not equal."

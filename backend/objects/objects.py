# libraries
import os
import shutil


def get_sub_paths(path):
    """
    Get all the sub paths inside path.

    Parameters
    ----------
    path : pathlib object
        path.

    Returns
    -------
    sub_paths : dict
        Dictionary containing sub paths for both directories and files in path.

    """
    path_dirs = []
    path_files = []

    for p in path.glob("**/*"):
        if p.name not in [".DS_Store"]:
            if p.is_dir():
                path_dirs.append(p.relative_to(path))
            elif p.is_file():
                path_files.append((p.relative_to(path), p.stat().st_mtime))

    path_dirs.sort()
    path_files.sort()

    sub_paths = {"dirs": path_dirs, "files": path_files}

    return sub_paths


def get_paths_paths_to_delete(origin_sub_paths, destination_sub_paths):
    """
    Gets directories and files present in clone but missing in master, since
    they will need to be deleted from clone.

    Parameters
    ----------
    origin_sub_paths : list
        Sub paths of master.
    destination_sub_paths : list
        Sub paths of clone.

    Returns
    -------
    paths_to_delete : dict
        Dictionary containing the directories and files to delete.

    """
    # destination_sub_paths paths not present in origin_sub_paths
    dirs_to_delete = [
        x for x in destination_sub_paths["dirs"] if x not in origin_sub_paths["dirs"]
    ]
    files_to_delete = [
        x[0]
        for x in destination_sub_paths["files"]
        if x not in origin_sub_paths["files"]
    ]

    # sort in order to avoid deleting a root folder before a sub folder
    dirs_to_delete.sort(reverse=True)

    paths_to_delete = {"dirs": dirs_to_delete, "files": files_to_delete}

    return paths_to_delete


def delete_paths(paths_to_delete, destination_root_path):
    """
    Executes commands to delete the paths_to_delete.

    Parameters
    ----------
    paths_to_delete : dict
        Dictionary containing the directories and files to delete.
    destination_root_path : pathlib object
        Root path of clone folder.

    Returns
    -------
    None.

    """
    # delete files
    for f in paths_to_delete["files"]:
        os.remove(destination_root_path / f)
        print(f"Deleted file: {f}")

    # delete directories
    for d in paths_to_delete["dirs"]:
        shutil.rmtree(destination_root_path / d)
        print(f"Deleted directory: {d}")


def get_paths_to_copy(origin_sub_paths, destination_sub_paths):
    """
    Gets directories and files present in master but missing in clone, since
    they will need to be copied from master to clone.

    Parameters
    ----------
    origin_sub_paths : list
        Sub paths of master.
    destination_sub_paths : list
        Sub paths of clone.

    Returns
    -------
    paths_to_copy : dict
        Dictionary containing the directories and files to delete.

    """
    dirs_to_copy = [
        x for x in origin_sub_paths["dirs"] if x not in destination_sub_paths["dirs"]
    ]
    files_to_copy = [
        x[0]
        for x in origin_sub_paths["files"]
        if x not in destination_sub_paths["files"]
    ]

    # sort in order to avoid creating a sub folder before a root folder
    dirs_to_copy.sort()

    paths_to_copy = {"dirs": dirs_to_copy, "files": files_to_copy}

    return paths_to_copy


def copy_paths(origin_root_path, destination_root_path, paths_to_copy):
    """
    Executes commands to copy the paths_to_copy.

    Parameters
    ----------
    origin_root_path : pathlib object
        Root path of master folder.
    destination_root_path : pathlib object
        Root path of clone folder.
    paths_to_copy : dict
        Dictionary containing the directories and files to delete.

    Returns
    -------
    None.

    """
    for d in paths_to_copy["dirs"]:
        os.makedirs(destination_root_path / d)
        print(f"Created directory: {d}")

    for f in paths_to_copy["files"]:
        shutil.copy2(origin_root_path / f, destination_root_path / f)
        print(f"Copied file: {f}")


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
    origin_sub_paths = get_sub_paths(path=origin_root_path)
    destination_sub_paths = get_sub_paths(path=destination_root_path)

    if origin_sub_paths == destination_sub_paths:
        return 0, "Process successful, both folders are now equal!"
    else:
        return 1, "Something went wrong. Origin and destination folders are not equal."

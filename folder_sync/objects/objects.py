"""Objects."""
import shutil
from pathlib import Path

from loguru import logger


def get_sub_paths(path: Path, edit_time_sensitive: bool = False) -> dict[str, list]:  # noqa: FBT001, FBT002
    """Get all the sub paths inside path.

    :param path: Path to search for sub paths.
    :param edit_time_sensitive: Whether to take into account the file edit time or not.
    :returns: Dictionary containing sub paths for both directories and files in the path.
    """
    dirs = []
    files = []

    for p in path.glob("**/*"):
        if not p.name.startswith("."):
            if p.is_dir():
                dirs.append(p.relative_to(path))
            elif p.is_file():
                files.append(
                    (p.relative_to(path), p.stat().st_mtime)
                    if edit_time_sensitive
                    else (p.relative_to(path), None),
                )

    # sort in order to avoid performing further operations on a child folder before a parent folder
    dirs.sort()
    files.sort()

    return {"dirs": dirs, "files": files}


def get_paths_to_delete(
    origin_child_paths: list,
    destination_child_paths: list,
) -> dict[str, list]:
    """Get directories and files present in destination but missing in origin, since
    they will need to be deleted from destination.

    :param origin_child_paths: Sub paths of origin.
    :param destination_child_paths: Sub paths of destination.
    :returns: Dictionary containing the directories and files to delete.
    """
    dirs_to_delete = [
        x for x in destination_child_paths["dirs"] if x not in origin_child_paths["dirs"]
    ]
    files_to_delete = [
        x[0] for x in destination_child_paths["files"] if x not in origin_child_paths["files"]
    ]

    # sort in order to avoid deleting a parent folder before a child folder
    dirs_to_delete.sort(reverse=True)

    return {"dirs": dirs_to_delete, "files": files_to_delete}


def delete_paths(paths_to_delete: dict, destination_root_path: Path) -> None:
    """Execute commands to delete the paths_to_delete.

    :param paths_to_delete: Dictionary containing the directories and files to delete.
    :param destination_root_path: Root path of the destination folder.
    :returns: None.
    """
    for f in paths_to_delete["files"]:
        Path.unlink(destination_root_path / f)
        logger.info(f"Deleted file: {destination_root_path / f}")

    for d in paths_to_delete["dirs"]:
        shutil.rmtree(destination_root_path / d)
        logger.info(f"Deleted directory: {destination_root_path / d}")


def get_paths_to_copy(origin_child_paths: list, destination_child_paths: list) -> dict[str, list]:
    """Get directories and files present in origin but missing in destination, since
    they will need to be copied from origin to destination.

    :param origin_child_paths: Sub paths of origin.
    :param destination_child_paths: Sub paths of destination.
    :returns: Dictionary containing the directories and files to copy.
    """
    dirs_to_copy = [
        x for x in origin_child_paths["dirs"] if x not in destination_child_paths["dirs"]
    ]
    files_to_copy = [
        x[0] for x in origin_child_paths["files"] if x not in destination_child_paths["files"]
    ]

    # sort in order to avoid creating a sub folder before a root folder
    dirs_to_copy.sort()

    return {"dirs": dirs_to_copy, "files": files_to_copy}


def copy_paths(origin_root_path: Path, destination_root_path: Path, paths_to_copy: list) -> None:
    """Execute commands to copy the paths_to_copy.

    :param origin_root_path: Root path of the origin folder.
    :param destination_root_path: Root path of the destination folder.
    :param paths_to_copy: Dictionary containing the directories and files to copy.
    :returns: None.
    """
    for d in paths_to_copy["dirs"]:
        Path.mkdir(destination_root_path / d, parents=True)
        logger.info(f"Created directory: {d}")

    for f in paths_to_copy["files"]:
        shutil.copy2(origin_root_path / f, destination_root_path / f)
        logger.info(f"Copied file: {f}")


def test_if_sucessful(origin_root_path: Path, destination_root_path: Path) -> tuple[int, str]:
    """Checks if the process went successfully, meaning the origin and destination folders
    are equal after all the changes.

    :param origin_root_path: Root path of the origin folder.
    :param destination_root_path: Root path of the destination folder.
    :returns: None.
    """
    origin_child_paths = get_sub_paths(path=origin_root_path)
    destination_child_paths = get_sub_paths(path=destination_root_path)

    if origin_child_paths == destination_child_paths:
        return 0, "Process successful, both folders are now equal!"

    return 1, "Something went wrong. Origin and destination folders are not equal."

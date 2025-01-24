"""Objects."""

import shutil
from pathlib import Path
from typing import Literal

from loguru import logger

FILES_TO_IGNORE = [
    # macOS system files and directories
    ".DS_Store",
    ".Trash",
    ".Trashes",
    ".Spotlight-V100",
    ".fseventsd",
    ".apdisk",
    ".TemporaryItems",
    ".vol",
    ".AppleDouble",
    "._",
    ".AppleDesktop",
    "._filename",
    ".metadata_never_index",  # Disables Spotlight indexing
    ".com.apple.timemachine.donotpresent",  # Prevents Time Machine backups
    ".com.apple.sparsebundle",  # Sparse bundle disk images
    ".hidden",  # Hides files from Finder
    ".VolumeIcon.icns",  # Custom volume icon
    # Windows system files and directories
    "desktop.ini",
    "Thumbs.db",
    "$Recycle.Bin",
    "System Volume Information",
    "pagefile.sys",
    "hiberfil.sys",
    "swapfile.sys",
    "Windows.old",
    "$WINDOWS.~BT",
    "$WINDOWS.~WS",
    "ntuser.dat",
    "ntuser.ini",
    "bootmgr",  # Windows boot manager file
    "BOOTNXT",  # Next boot configuration file
    "Recovery",  # Recovery partition files
    "hiberfil.sys",  # Hibernation file
    "MSOCache",  # Microsoft Office cache
    "PerfLogs",  # Performance logs directory
    "ProgramData",  # Hidden by default on system drive
    # Cross-platform (macOS and Windows) or temporary files
    "._filename",  # macOS resource fork files on non-HFS+ systems
    ".Trash-*",  # External drives' trash directories
    ".~lock",  # Temporary lock files (e.g., from LibreOffice)
    ".sync",  # Resilio Sync or similar applications
    ".picasa.ini",  # Metadata from Picasa
    ".thumbs",  # Thumbnail cache from some applications
    "~$filename",  # Temporary files from Microsoft Office
]


def get_sub_paths(
    root_path: Path, *, by_last_modified: bool = True
) -> dict[str, list[tuple[Path, None]] | list[tuple[Path, None | float]]]:
    """Get all the sub paths inside path.

    Args:
        root_path: Path to search for sub paths.
        by_last_modified: Whether to take into account the last modified date of the files to detect
        differences.

    Returns:
        Dictionary containing sub paths for both directories and files in the root_path.
    """
    dirs = []
    files = []

    for complete_path in root_path.glob("**/*"):
        if not any(ignore_file in str(complete_path) for ignore_file in FILES_TO_IGNORE):
            if complete_path.is_dir():
                dirs.append((complete_path.relative_to(root_path), None))
            elif complete_path.is_file():
                files.append(
                    (
                        complete_path.relative_to(root_path),
                        complete_path.stat().st_mtime if by_last_modified else None,
                    )
                )

    # sort in order to avoid performing further operations on a child folder before a parent folder
    dirs.sort()
    files.sort()

    return {"dirs": dirs, "files": files}


def get_paths_to_delete(
    origin_child_paths: dict[str, list[tuple[Path, None]] | list[tuple[Path, None | float]]],
    destination_child_paths: dict[str, list[tuple[Path, None]] | list[tuple[Path, None | float]]],
) -> dict[str, list[Path]]:
    """Get directories and files present in destination but missing in origin, since
    they will need to be deleted from destination.

    Args:
        origin_child_paths: Sub paths of origin.
        destination_child_paths: Sub paths of destination.

    Returns:
        Dictionary containing the directories and files to delete.
    """
    dirs_to_delete: list[Path] = [
        x[0] for x in destination_child_paths["dirs"] if x not in origin_child_paths["dirs"]
    ]
    files_to_delete: list[Path] = [
        x[0] for x in destination_child_paths["files"] if x not in origin_child_paths["files"]
    ]

    # sort in order to avoid deleting a parent folder before a child folder
    dirs_to_delete.sort(reverse=True)

    return {"dirs": dirs_to_delete, "files": files_to_delete}


def delete_paths(paths_to_delete: dict[str, list[Path]], destination_root_path: Path) -> None:
    """Execute commands to delete the paths_to_delete.

    Args:
        paths_to_delete: Dictionary containing the directories and files to delete.
        destination_root_path: Root path of the destination folder.

    Returns:
        None.
    """
    for f in paths_to_delete["files"]:
        Path.unlink(destination_root_path / f)
        logger.info(f"Deleted file: {destination_root_path / f}")

    for d in paths_to_delete["dirs"]:
        shutil.rmtree(destination_root_path / d)
        logger.info(f"Deleted directory: {destination_root_path / d}")


def get_paths_to_copy(
    origin_child_paths: dict[str, list[tuple[Path, None]] | list[tuple[Path, None | float]]],
    destination_child_paths: dict[str, list[tuple[Path, None]] | list[tuple[Path, None | float]]],
) -> dict[str, list[Path]]:
    """Get directories and files present in origin but missing in destination, since
    they will need to be copied from origin to destination.

    Args:
        origin_child_paths: Sub paths of origin.
        destination_child_paths: Sub paths of destination.

    Returns:
        Dictionary containing the directories and files to copy.
    """
    dirs_to_copy = [
        x[0] for x in origin_child_paths["dirs"] if x not in destination_child_paths["dirs"]
    ]
    files_to_copy = [
        x[0] for x in origin_child_paths["files"] if x not in destination_child_paths["files"]
    ]

    # sort in order to avoid creating a sub folder before a root folder
    dirs_to_copy.sort()

    return {"dirs": dirs_to_copy, "files": files_to_copy}


def copy_paths(
    origin_root_path: Path, destination_root_path: Path, paths_to_copy: dict[str, list[Path]]
) -> None:
    """Execute commands to copy the paths_to_copy.

    Args:
        origin_root_path: Root path of the origin folder.
        destination_root_path: Root path of the destination folder.
        paths_to_copy: Dictionary containing the directories and files to copy.

    Returns:
        None.
    """
    for d in paths_to_copy["dirs"]:
        Path.mkdir(destination_root_path / d, parents=True)
        logger.info(f"Created directory: {d}")

    for f in paths_to_copy["files"]:
        shutil.copy2(origin_root_path / f, destination_root_path / f)
        logger.info(f"Copied file: {f}")


def test_if_sucessful(
    origin_root_path: Path, destination_root_path: Path
) -> tuple[Literal[0, 1], str]:
    """Checks if the process went successfully, meaning the origin and destination folders
    are equal after all the changes.

    Args:
        origin_root_path: Root path of the origin folder.
        destination_root_path: Root path of the destination folder.

    Returns:
        Success status.
    """
    origin_child_paths = get_sub_paths(root_path=origin_root_path)
    destination_child_paths = get_sub_paths(root_path=destination_root_path)

    if origin_child_paths == destination_child_paths:
        return 0, "Process successful, both folders are now equal!"

    return 1, "Something went wrong. Origin and destination folders are not equal."

"""__init__.py for objects module."""

from .objects import (
    copy_paths,
    delete_paths,
    get_paths_paths_to_delete,
    get_paths_to_copy,
    get_sub_paths,
    test_if_sucessful,
)

__all__ = [
    "get_sub_paths",
    "test_if_sucessful",
    "get_paths_paths_to_delete",
    "delete_paths",
    "get_paths_to_copy",
    "copy_paths",
]

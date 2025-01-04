"""__init__.py for objects module."""

from ._objects import (
    copy_paths,
    delete_paths,
    get_paths_to_copy,
    get_paths_to_delete,
    get_sub_paths,
    test_if_sucessful,
)

__all__ = [
    "copy_paths",
    "delete_paths",
    "get_paths_to_copy",
    "get_paths_to_delete",
    "get_sub_paths",
    "test_if_sucessful",
]

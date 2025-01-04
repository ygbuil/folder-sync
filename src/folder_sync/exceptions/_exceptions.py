"""Custom exceptions."""


class UnexistingFolderError(Exception):
    """Error with the Yahoo Finance API."""

    def __init__(self: "UnexistingFolderError", msg: None | str = None) -> None:
        """Provide the error message or return default.

        Args:
            self: Own class.
            msg: Custom error message. Defaults to None.
        """
        super().__init__(msg or "Folder does not exist.")

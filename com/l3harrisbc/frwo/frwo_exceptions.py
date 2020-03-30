"""

Custom exceptions for the FileManager object.

All exceptions can accept a single argument, intended to be used to specify the
filepath that caused the exception.

"""

from pathlib import Path

class FileManagerReadException(Exception):
    """ Custom exception to handle file read errors. """

    def __init__(self, filepath):
        self.path = Path(filepath)

    def __str__(self):
        return f"FileManger could not read {path}"


class FileManagerWriteException(Exception):
    """ Custom exception to handle file write errors. """

    def __init__(self, filepath):
        self.path = Path(filepath)

    def __str__(self):
        return f"FileManager was unable to write to {path}"


class FileManagerUnknownException(Exception):
    """ Catch-all for unknown exception types. """

    def __init__(self, filepath):
        self.path = Path(filepath)

    def __str__(self):
        return "FileManager encountered an unknown error"


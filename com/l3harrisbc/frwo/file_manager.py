"""
The FileManager object is defined herein. This generic object can be used by
both client and server for all file read/write operations.
"""

import json
from pathlib import Path
from .frwo_exceptions import *


class FileManager:
    """ Abstraction object for all file system operations """
    
    def __init__(self, basepath: str):
        self.base = Path(basepath)


    def read(filename: str): -> str
        """ Basic reading of file from disk """
        self.path = self.base / filename
        """
        @TODO: implement remainder
        """


    def write(filename: str, content: str): -> None
        """ Basic writing of file to disk """
        self.path = self.base / filename
        """
        @TODO: implement remainder
        """


    def read_config(filename: str):
        """ Wrapper function to retrieve and parse a config file """
        content = self.read(filename)
        """
        @TODO: implement remainder
        """

        
    def write_config(filename: str, content: str):
        """ Wrapper function to write a config file """
        content = json.dumps(content)
        """
        @TODO: implement remainder
        """
        

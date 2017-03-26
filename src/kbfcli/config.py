"""KBFCLI Configuration"""

import configparser

from typing import Dict, IO


class KBFConfigError(Exception):
    """Errors related to KBF configuration"""
    pass


class KBFConfig(object):
    """Represents KBFCLI Config"""

    def __init__(self, source: str=None) -> None:
        self.configparser = configparser.ConfigParser()
        self.configparser["boards"] = {}

        if source:
            try:
                self.configparser.read(source)
            except configparser.Error:
                raise KBFConfigError()

    def write(self, fileobject: IO[str]) -> None:
        """Write a config file to a given file object"""
        self.configparser.write(fileobject)

    def boards(self) -> Dict[str, str]:
        """Returns the configured boards"""
        return self.configparser["boards"]

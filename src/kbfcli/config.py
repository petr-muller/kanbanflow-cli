"""KBFCLI Configuration"""

import io
import configparser

from typing import Dict


class KBFConfig(object):
    """Represents KBFCLI Config"""

    def __init__(self):
        self.configparser = configparser.ConfigParser()
        self.configparser["boards"] = {}

    def write(self, fileobject: io.TextIOBase):
        """Write a config file to a given file object"""
        self.configparser.write(fileobject)

    def boards(self) -> Dict[str, str]:
        """Returns the configured boards"""
        return self.configparser["boards"]

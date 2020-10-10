import os
from configparser import ConfigParser, NoSectionError, NoOptionError


class Config:

    def __init__(self):
        """
        Loads configuration from file
        """
        self.config = ConfigParser()
        try:
            self.config.read(os.environ["CONFIG_PATH"])
        except FileNotFoundError:
            print(f"config.ini can not be found in {os.environ['CONFIG_PATH']}")

    def _get_key(self, section: str, key: str):
        """
        Get key within a section in the config.ini file.

        :param section: Name of the section in the configuration file
        :type section: str
        :param key: Name of the key in the specified section in the configuration file
        :type key: str
        """
        try:
            return self.config[section][key]
        except NoSectionError or NoOptionError:
            print(f"config.ini does not contain key {key} in section {section}")

    def general(self, key: str):
        """
        Get general settings from config.ini.
        """
        try:
            return self._get_key('GENERAL', key)
        except NoOptionError:
            print(f"config.ini: General section does not contain key '{key}'")

    def audd(self, key: str):
        """
        Get audd.io values from config.ini.
        """
        try:
            return self._get_key('audd.io', key)
        except NoOptionError:
            print(f"config.ini: audd.io section does not contain key '{key}'")

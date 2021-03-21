"""Loads configuration from config.ini.
"""

from configparser import ConfigParser


config = ConfigParser()
config.read("jmbf/config.ini")
config = config["user"]

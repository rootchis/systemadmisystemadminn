import configparser
import os.path
import pytest
from systemadmin.files import File
from configparser import ConfigParser


absolute_path = os.path.dirname(__file__)

def test_something():
    assert True == True  # add assertireadon here

def test_typeoffile():
    config = ConfigParser()
    config.read("../configfile.properties")

    file1 = File(config["resources"]["file.1"])
    file2 = File(config["resources"]["file.2"])

    assert file1.typeoffile() == "standard file"
    assert file2.typeoffile() == "dir"
    assert File("").typeoffile() == "not a file"







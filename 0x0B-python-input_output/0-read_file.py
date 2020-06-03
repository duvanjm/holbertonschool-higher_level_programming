#!/usr/bin/python3
"""module"""


def read_file(filename=""):
    """read file"""
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read(), end="")

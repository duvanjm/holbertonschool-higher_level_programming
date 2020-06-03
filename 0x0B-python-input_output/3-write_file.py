#!/usr/bin/python3
"""write on text file"""


def write_file(filename="", text=""):
    """write a string to a text file"""
    with open(filename, "w", encoding="utf-8") as myFile:
        return myFile.write(text)

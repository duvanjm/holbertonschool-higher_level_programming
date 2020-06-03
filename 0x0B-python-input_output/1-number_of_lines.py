#!/usr/bin/python3
"""module"""


def number_of_lines(filename=""):
    """returns the number of lines of a text file"""
    i = 0
    with open(filename, encoding="utf-8") as myFile:
        for line in myFile:
            i += 1
        return i

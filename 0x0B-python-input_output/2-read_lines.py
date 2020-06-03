#!/usr/bin/python3
"""read the line"""


def read_lines(filename="", nb_lines=0):
    """reads n lines of a text file"""
    with open(filename, encoding="utf-8") as myFile:
        if nb_lines < 1:
            print(myFile.read(), end="")
        else:
            for i in range(nb_lines):
                print(myFile.readline(), end="")

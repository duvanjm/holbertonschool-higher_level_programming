#!/usr/bin/python3
def number_of_lines(filename=""):
    i = 0
    with open(filename, encoding="utf-8") as myFile:
        for line in myFile:
            i += 1
        return i

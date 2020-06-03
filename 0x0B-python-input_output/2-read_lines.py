#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, encoding="utf-8") as myFile:
        if nb_lines < 0:
            print(myFile.read(), end="")
        else:
            for i in range(nb_lines):
                print(myFile.readline(), end="")

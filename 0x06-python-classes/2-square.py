#!/usr/bin/python3
"""class Square"""


class Square:
    """class"""
    def __init__(self, size=0):
        """arguments"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = size

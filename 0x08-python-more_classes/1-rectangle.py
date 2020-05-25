#!/usr/bin/python3
"""define rectangle class"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """define class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """define width"""
        return self.__width

    @property
    def height(self):
        """define height"""
        return self.__width

    @width.setter
    def width(self, value):
        """define private class"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """define private class"""
        if type(value) is not int:
            raise TypeError("heigth must be an integer")
        if value < 0:
            raise ValueError("heigth must be >= 0")
        self.__height = value

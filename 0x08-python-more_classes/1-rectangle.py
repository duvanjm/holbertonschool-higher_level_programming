#!/usr/bin/python3

"""define rectangle class"""


class Rectangle:
    """class: Rectangle"""
    def __init__(self, width=0, height=0):
        """init class"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """define width"""
        return self.__width

    @width.setter
    def width(self, value):
        """define pivate class"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """define height"""
        return self.__height

    @height.setter
    def height(self, value):
        """define pivate class"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

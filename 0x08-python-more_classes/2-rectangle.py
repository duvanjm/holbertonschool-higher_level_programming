#!/usr/bin/python3
"""rectangle class"""


class Rectangle:
    """define a rectangle class"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    def area(self):
        """calculate the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """calculate the perimeter of the rectangle"""
        if self.__height is 0 or self.__width is 0:
            return 0
        return self.__height * 2 + self.__width * 2

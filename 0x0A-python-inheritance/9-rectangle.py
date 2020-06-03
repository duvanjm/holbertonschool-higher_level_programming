#!/usr/bin/python3
"""module"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """define area() method"""
        return self.__width * self.__height

    def __str__(self):
        """define srt method"""
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))

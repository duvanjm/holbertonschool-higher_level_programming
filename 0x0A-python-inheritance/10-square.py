#!/usr/bin/python3
"""module"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size):
        """Instantiation"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

#!/usr/bin/python3
"""Class Square"""


class Square:
    """Class Square"""

    def __init__(self, size=0):
        """init method"""
        self.size = size

    @property
    def area__(self):
        """property for private instance"""
        return self.__size

    @area__.setter
    def area_(self, value):
        """setter for  private instance"""
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """method that calculate the area of the
        Square"""
        return self.__size * self.size

    def my_print(self):
        """print the Square"""
        if self.size == 0:
            print()
        for i in range(0, self.size):
            print("#" * self.size)

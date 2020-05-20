#!/usr/bin/python3
class Square:
    """class"""

    def __init__(self, size=0):
        """square class"""

        self.size = size

    @property
    def size(self):
        """retrieve size from class"""

        return self.__size

    @size.setter
    def size(self, value):
        """square size setter """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """calculate the square area"""

        return self.__size ** 2

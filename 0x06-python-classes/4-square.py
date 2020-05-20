#!/usr/bin/python3
"""class Square"""


class Square:
    """Defines a square by size.
    Attributes:
        size square size.
    """

    def __init__(self, size=0):
        """square class constructor.
        Parameters:
            size: square size, default value is 0
        """

        self.size = size

    @property
    def size(self):
        """Retrieve size from class.
        Returns:
        int: the square size.
        """

        return self.__size

    @size.setter
    def size(self, value):
        """square size setter.
        Parameters:
        Returns:
        int: square size
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates the square area
        Returns:
        int: the current square area
        """

        return self.__size ** 2

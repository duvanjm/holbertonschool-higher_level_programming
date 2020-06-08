#!/usr/bin/python3
"""module"""


from models.base import Base


class Rectangle(Base):
    """ """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """f """
        return self.__width

    @width.setter
    def width(self, value):
        """f """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """f """
        return self.__height

    @height.setter
    def height(self, value):
        """f """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """f """
        return self.__x

    @x.setter
    def x(self, value):
        """f """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """f"""
        return self.__y

    @y.setter
    def y(self, value):
        """f """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculate the aerea of the rectangle"""
        return self.__width * self.height

    def display(self):
        """print a rectangle"""
        print("\n" * self.__y, end="")
        for height in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """ """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

#!/usr/bin/python3
"""module
"""


from models.base import Base


class Rectangle(Base):
    """class Rectanble based in class Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter of the width
        """
        return self.__width

    @property
    def height(self):
        """getter of the height
        """
        return self.__height

    @property
    def x(self):
        """getter of the x
        """
        return self.__x

    @property
    def y(self):
        """getter of the x
        """
        return self.__y

    @width.setter
    def width(self, value):
        """setter of the width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """setter of the height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """setter of the x
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """setter of the y
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculate the aerea of the rectangle
        """
        return self.__width * self.height

    def display(self):
        """print a rectangle
        """
        print("\n" * self.__y, end="")
        for height in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """print a rectangle
        """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """update the class
        """
        if (args):
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif(kwargs):
            for position, v in kwargs.items():
                if position == "id":
                    self.id = v
                if position == "width":
                    self.__width = v
                if position == "height":
                    self.__height = v
                if position == "x":
                    self.__x = v
                if position == "y":
                    self.__y = v

    def to_dictionary(self):
        """define dictionary
        """
        dict_ = {}
        dict_['id'] = self.id
        dict_['width'] = self.width
        dict_['height'] = self.height
        dict_['x'] = self.x
        dict_['y'] = self.y
        return dict_

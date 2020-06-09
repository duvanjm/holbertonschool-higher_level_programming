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

    def update(self, *args, **kwargs):
        """ """
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

    def dictionary(self):
        """ """
        dict_ = {}
        for i in ["id", "width", "height", "x", "y"]:
            dict_.update({i: getattr(self, i)})
        return dict_

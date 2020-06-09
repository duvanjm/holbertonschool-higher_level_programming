#!/usr/bin/python3
"""module
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square based in class Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """str method
        """
        return ("[Square] {:d} {:d}/{:d} - {:d}".format(self.id, self.x,
                                                        self.y, self.width))

    @property
    def size(self):
        """getter of the size
        """
        return self.width

    @size.setter
    def size(self, value):
        """setter of the size
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update the class
        """
        if len(args) < 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                    self.height = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.x = args[3]

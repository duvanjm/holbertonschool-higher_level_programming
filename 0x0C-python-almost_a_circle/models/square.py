#!/usr/bin/python3
"""module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square based in class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """f """
        return "[Square] {:d} {:d}/{:d} - {:d}".format(self.id, self.x,
                                                        self.y, self.width)

    @property
    def size(self):
        """ """
        return self.width

    @size.setter
    def size(self, value):
        """ """
        self.width = value
        self.height = value

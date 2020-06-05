#!/usr/bin/python3
"""module"""


class Base:
    """create a base class"""
    def __init__(self, id=None):
        """class constructor"""
        __nb_objects = 0
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = __nb_objects

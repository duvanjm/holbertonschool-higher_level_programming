#!/usr/bin/python3
"""module"""


def inherits_from(obj, a_class):
    """function that compare if the object
    is an instance of a class that inherited """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False

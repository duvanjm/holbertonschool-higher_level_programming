#!/usr/bin/python3
"""module"""


def is_kind_of_class(obj, a_class):
    """function that compare if the object
    is an instance of a class that inherited"""
    if isinstance(obj, a_class):
        return True
    else:
        return False

#!/usr/bin/python3
"""class Student that defines a student"""


class Student:
    """class student"""
    def __init__(self, first_name, last_name, age):
        """class student"""
        self.first_name = first_name
        self.laste_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of a Student instance"""
        return self.__dict__

    
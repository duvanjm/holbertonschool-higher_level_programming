#!/usr/bin/python3
"""module"""

import json


class Base:
    """create a base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Dictionary to JSON string
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON string to file
        """
        list_objects = []
        if list_objs is None or len(list_objs) == 0:
            list_objects = []
        else:
            for i in list_objs:
                list_objects.append(i.to_dictionary())
        json_string = Base.to_json_string(list_objects)
        with open("{}.json".format(cls.__name__), mode='w') as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation 
        """
        if json_string is None or len(json_string) == 0:
            return "[]"
        else:
            return json.dumps(json_string)

#!/usr/bin/python3
"""
Reviewing all subjects
"""


import json
import sys


class Base(object):
    """
    Base class starting
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def to_json_string(cls, list_dictionaries):
        """Return json representation"""
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """Saving JSON file"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        json_data = []
        for obj in list_objs:
            json_data.append(cls.to_json_string(obj.to_dictionary()))
        json_data = cls.to_json_string(json_data)

        with open(filename, 'w') as file:
            file.write(json_data)

    @staticmethod
    def from_json_string(json_string):
        """Return list of JSON string rep"""
        new_list = []
        if json_string is None or json_string == []:
            return new_list
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns a list of instances"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

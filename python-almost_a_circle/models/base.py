#!/usr/bin/python3
"""
Reviewing all subjects
"""


import json
import sys


class Base:
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

    def to_json_string(list_dictionaries):
        """Return json representation"""
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

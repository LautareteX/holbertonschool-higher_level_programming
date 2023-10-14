#!/usr/bin/python3
"""I forgot to comment the code so I added this line """
import json


class Base():
    """Here we are again es es"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Here we are again os os"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Convert a list of dictionaries to Json format """
        if not list_dictionaries:
            return "[]"

        json_data = json.dumps(list_dictionaries)
        return json_data

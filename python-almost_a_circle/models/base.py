#!/usr/bin/python3
"""I forgot to comment the code so I added this line """


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

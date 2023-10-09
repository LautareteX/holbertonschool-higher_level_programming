#!/usr/bin/python3
"""I dont have more ideas for the comments"""


class Student:
    def __init__(self, first_name, last_name, age):
        """I dont have more ideas for the comments"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """I dont have more ideas for the comments"""
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for i in attrs:
                if hasattr(self, i):
                    new_dict[i] = getattr(self, i)
                    if new_dict[i] is AttributeError:
                        continue
            return new_dict

    def reload_from_json(self, json):
        for i in json:
            """I dont have more ideas for the comments"""
            if hasattr(self, i):
                """I dont have more ideas for the comments"""
                setattr(self, i, json[i])

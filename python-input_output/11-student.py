#!/usr/bin/python3
"""
returns dictionary description
"""


class Student():
    """
    student information for
    """

    def __init__(self, first_name, last_name, age):
        """New student rep"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """to json file rep"""
        return self.__dict__

    def to_json(self, attrs=None):
        """Converting new stdt"""
        if attrs is None:
            return self.__dict__

        new_dict = {}
        for i in attrs:
            if i in self.__dict__.keys():
                new_dict[i] = self.__dict__[i]
        return new_dict

    def reload_from_json(self, json):
        """replace attrs in"""
        for i, val in json.items():
            setattr(self, i, val)

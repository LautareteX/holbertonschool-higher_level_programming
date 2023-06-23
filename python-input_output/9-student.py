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

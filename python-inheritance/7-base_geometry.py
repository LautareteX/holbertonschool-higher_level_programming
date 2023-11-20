#!/usr/bin/python3
"""i hate the comments here"""


class BaseGeometry:
    """for some reason isnt commented"""
    def area(self):
        """Return an EPIC Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

#!/usr/bin/python3
"""idk i need to comment here"""


class BaseGeometry:
    """BaseGeometry? That is School Geometry"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def area(self):
        """area looks good"""
        return self.__width * self.__height

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

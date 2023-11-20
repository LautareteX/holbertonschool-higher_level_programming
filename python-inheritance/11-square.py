#!/usr/bin/python3
"""i hate the comments here"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Field to Square """
    def __init__(self, size):
        """ Initialize attributes and validations. """
        self.integer_validator("size", size)
        self.__size = size
        """ Rectangle class have a construct method """
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2

    def __str__(self) -> str:
        return (f"[Square] {self.__size}/{self.__size}")

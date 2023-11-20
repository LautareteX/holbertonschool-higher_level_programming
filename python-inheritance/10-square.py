#!/usr/bin/python3
"""i hate the comments here"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """for some reason isnt commented"""
    def __init__(self, size):
        """Intialize a god rectangule"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """return area yes"""
        return self.__size ** 2

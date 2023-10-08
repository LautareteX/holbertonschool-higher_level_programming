#!/usr/bin/python3
"""more commentssssss auu auuuu"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """oh yeah! More comments!"""
    def __init__(self, width=0, height=0):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self._Rectangle__width * self._Rectangle__height

    def __str__(self):
        return (f"[Rectangle] {self.__width}/{self.__height}")

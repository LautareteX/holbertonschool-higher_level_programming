#!/usr/bin/python3
"""
Reviewing all subjects
"""
from models.base import Base


class Rectangle(Base):
    """ Representing a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("width must be > 0")
        elif type(value) != int:
            raise TypeError("width must be an integer")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("height must be > 0")
        elif type(value) != int:
            raise TypeError("height must be an integer")
        else:
            self.__height = value

    @y.setter
    def y(self, value):
        if value <= 0:
            raise ValueError("y must be > 0")
        elif type(value) != int:
            raise TypeError("y must be an integer")
        else:
            self.__y = value

    @x.setter
    def y(self, value):
        if value <= 0:
            raise ValueError("x must be > 0")
        elif type(value) != int:
            raise TypeError("x must be an integer")
        else:
            self.__x = value


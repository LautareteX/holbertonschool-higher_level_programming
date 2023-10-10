#!/usr/bin/python3
from base import Base
"""Here we are again"""


class Rectangle(Base):
    """
    Here we are again
    """
    def __init__(self, width=0, height=0, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Here we are again
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Here we are again
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Here we are again
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Here we are again
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """
        Here we are again
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Here we are again
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Here we are again
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Here we are again
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

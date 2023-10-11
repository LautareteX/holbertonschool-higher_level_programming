#!/usr/bin/python3
"""I forgot to comment the code so I added this line """
from base import Base


class Rectangle(Base):
    """Here we are again"""
    def __init__(self, width=0, height=0, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Here we are again"""
        return self.__width

    @width.setter
    def width(self, value):
        """Here we are again"""
        if type(value) is not int:
            raise TypeError(f"width  must be an integer")
        if value < 0:
            raise ValueError(f"width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Here we are again"""
        return self.__height

    @height.setter
    def height(self, value):
        """Here we are again"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Here we are again"""
        return self.__x

    @x.setter
    def x(self, value):
        """Here we are again"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        self.__x = value

    @property
    def y(self):
        """Here we are again"""
        return self.__y

    @y.setter
    def y(self, value):
        """Here we are again"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Here we are again"""
        return self.width * self.height


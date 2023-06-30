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
        self.x = x
        self.y = y

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
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    def area(self):
        """Always return the area"""
        return self.__width * self.__height

    def display(self):
        """Print the rectangle using #"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """Return the string representation of the object"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - " \
            f"{self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """allocation of values in order or by dictionary"""
        if args:
            for iterator, count in enumerate(args, start=1):
                if iterator == 1:
                    self.id = count
                if iterator == 2:
                    self.width = count
                if iterator == 3:
                    self.height = count
                if iterator == 4:
                    self.x = count
                if iterator == 5:
                    self.y = count
        else:
            for iterator, count in kwargs.items():
                if iterator == "id":
                    self.id = count
                if iterator == "width":
                    self.width = count
                if iterator == "height":
                    self.height = count
                if iterator == "x":
                    self.x = count
                if iterator == "y":
                    self.y = count

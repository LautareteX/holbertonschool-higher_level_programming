#!/usr/bin/python3


class Rectangle:
    """Bored and empty class named rectangle"""
    def __init__(self, width=0, height=0) -> None:
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            perimetro = 0
        else:
            perimetro = (self.__height + self.__width) * 2
        return perimetro

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rect = ""
            for _ in range(self.__height):
                rect += "#" * self.__width + "\n"

            return rect[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        return print("Bye rectangle...")

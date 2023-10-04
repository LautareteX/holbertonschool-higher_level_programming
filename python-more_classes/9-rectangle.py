#!/usr/bin/python3


class Rectangle:
    """Bored and empty class named rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0, print_symbol="#") -> None:
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1
        self.print_symbol = print_symbol

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

    def print_smybol(self):
        return self.print_smybol

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        try:
            if rect_1.area() > rect_2.area():
                return rect_1
            elif rect_1.area() < rect_2.area():
                return rect_2
            else:
                return rect_1
        except:
            if rect_1 is not isinstance(Rectangle):
                raise TypeError("rect_1 must be an instance of Rectangle")
            elif rect_2 is not isinstance(Rectangle):
                raise TypeError("rect_2 must be an instance of Rectangle")

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rect = ""
            for _ in range(self.__height):
                rect += str(self.print_symbol) * self.__width + "\n"
            return rect[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        return print("Bye rectangle...")

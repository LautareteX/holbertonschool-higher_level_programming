#!/usr/bin/python3
""" a simple class"""


class Square:
    """A bored class named square"""
    def __init__(self, size=0) -> None:
        self.__size = size

    @property
    def size(self):
        """return size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        "thats an excellent point"

        if (type(value) != int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """only calculates square area :D"""
        return (self.__size ** 2)

    def my_print(self):
        """now we need to print the square"""

        if self.__size == 0:
            print()

        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()

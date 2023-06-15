#!/usr/bin/python3
"""Create class square"""


class Square:
    """Define a square"""
    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        for i in range(self.__size):
            if i != 0:
                print("")
            for j in range(self.__size):
                print("#", end="")
        print()

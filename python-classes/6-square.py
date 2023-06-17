#!/usr/bin/python3
"""Create class square"""


class Square:
    """Define a square"""
    def __init__(self, size=0, position=(0, 0)):
        if ((position[0] < 0) or (position[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(position) > 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(position[0]) != int or type(position[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__size = size
            self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

    def area(self):
        if self.__size == 0:
            print()
            return

    def my_print(self):
        if self.__size == 0:
            print()
            return

        if self.__position[1] > 0:
            for i in range(self.__position[1]):
                print()
        for i in range(self.__size):
            if i != 0:
                print("")
            for spaces in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
        print()

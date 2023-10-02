#!/usr/bin/python3
""" a simple class"""


class Square:
    """A bored class named square"""
    def __init__(self, size=0) -> None:
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """only calculates square area :D"""
        return (self.__size ** 2)

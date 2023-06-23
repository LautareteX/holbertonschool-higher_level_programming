#!/usr/bin/python3
"""
Python Reading file
"""


def read_file(filename=""):
    """
    reading and printing content
    """
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read())

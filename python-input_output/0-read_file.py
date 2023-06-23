#!/usr/bin/python3
"""
Python Reading file
"""


def read_file(filename=""):
    """
    reading and printing content
    """
    if filename:
        with open(filename, encoding="UTF8") as my_file:
            print(my_file.read())
    else:
        print("")

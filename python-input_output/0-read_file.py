#!/usr/bin/python3
"""
Python Reading file
"""


def read_file(filename=""):
    """ reading and printing content """
    with open(filename, "r", encoding="UTF8") as f:
        print(f.read(), end="")

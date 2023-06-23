#!/usr/bin/python3
"""
Python Reading file
"""


def read_file(filename=""):
    """
    reading and printing content
    """
    if filename:
        with open(filename, encoding="UTF8") as f:
            read_data = f.read()

        print(read_data)
        f.close

#!/usr/bin/python3
import os
"""now we are commenting)?"""

def read_file(filename=""):
    with open(filename, mode="r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")

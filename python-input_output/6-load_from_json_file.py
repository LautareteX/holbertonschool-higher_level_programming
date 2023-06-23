#!/usr/bin/python3
"""
JSON - Interchanger
"""


import json
import sys


def load_from_json_file(filename):
    """
    Save object into a file
    """
    with open(filename, "r", encoding="UTF-8") as my_file:
        return json.loads(my_file.read())

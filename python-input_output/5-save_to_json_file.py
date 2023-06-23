#!/usr/bin/python3
"""
JSON Interchanger
"""


import json
import sys


def save_to_json_file(my_obj, filename):
    """
    Save into a file
    """
    f_obj = json.dumps(my_obj)

    with open(filename, "w") as outfile:
        outfile.write(f_obj)
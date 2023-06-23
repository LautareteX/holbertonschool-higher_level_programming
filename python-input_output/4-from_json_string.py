#!/usr/bin/python3
"""
JSON Interchanger
"""


import json
import sys


def from_json_string(my_str):
    """
    Return object
    """
    return json.loads(my_str)

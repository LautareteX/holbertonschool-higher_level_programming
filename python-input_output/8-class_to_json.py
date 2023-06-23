#!/usr/bin/python3
"""
returns dictionary description
"""


def class_to_json(obj):
    """
    return str from obj
    """
    return obj.__dict__

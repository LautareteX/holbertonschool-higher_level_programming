#!/usr/bin/python3
"""i hate the comments here"""


def is_same_class(obj, a_class):
    """for some reason isnt commented"""
    if obj is None:
        return False

    if not type(obj) is a_class:
        return False
    return True

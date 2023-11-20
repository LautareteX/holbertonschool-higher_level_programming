#!/usr/bin/python3
"""i hate the comments here"""


def inherits_from(obj, a_class):
    """for some reason isnt commented"""
    if type(obj) == a_class:
        return False
    if issubclass(type(obj), a_class):
        return True
    return False

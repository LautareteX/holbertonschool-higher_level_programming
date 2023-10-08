#!/usr/bin/python3
"""i hate the comments here"""


def inherits_from(obj, a_class):
    """for some reason isnt commented"""
    for cls in obj.__class__.__mro__:
        if issubclass(cls, a_class):
            return True

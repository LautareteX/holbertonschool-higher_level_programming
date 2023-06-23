#!/usr/bin/python3
"""
Is the same class? Module
"""


def inherits_from(obj, a_class):
    """
    True, False
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class

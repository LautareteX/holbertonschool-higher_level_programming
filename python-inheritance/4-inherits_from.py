#!/usr/bin/python3
def inherits_from(obj, a_class):
    for cls in obj.__class__.__mro__:
        if issubclass(cls, a_class):
            return True

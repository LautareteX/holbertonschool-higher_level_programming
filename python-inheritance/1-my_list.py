#!/usr/bin/python3
"""i hate the comments here"""

class MyList(list):
    """for some reason isnt commented"""

    def print_sorted(self):
        if hasattr(self, '__str__'):
            print(sorted(self))
            return (sorted(self))

#!/usr/bin/python3
"""
Print_sorted module
"""


class MyList(list):
    """
    My list class
    """
    def print_sorted(self):
        """
        print
        """
        print(sorted(self))
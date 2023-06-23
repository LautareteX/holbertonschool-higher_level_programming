#!/usr/bin/python3
"""
Pascal triangle without fibonacci
"""


def pascal_triangle(n):
    """
    pascal triangle func
    """
    my_list = []

    if n <= 0:
        return my_list
    else:
        for i in range(n):
            res = 11**i
            my_list.append(str(res))
        return my_list

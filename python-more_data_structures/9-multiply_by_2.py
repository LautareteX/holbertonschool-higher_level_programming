#!/usr/bin/python3
def multiply_by_2(a_dictionary):

    my_dictionary = {}

    for key, val in a_dictionary.items():
        my_dictionary[key] = val * 2

    return my_dictionary

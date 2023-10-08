#!/usr/bin/python3
"""No fueron nada a la corre caminata"""
import json


def save_to_json_file(my_obj, filename):
    """y no van a ir tampoco, estan de cuento"""
    with open(filename, 'w') as f:
        n = json.dump(my_obj, f)

    return n
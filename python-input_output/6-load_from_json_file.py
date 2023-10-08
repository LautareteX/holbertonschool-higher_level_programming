#!/usr/bin/python3
"""Advanced graphics? ULTRA! My PC BOOM"""
import json


def load_from_json_file(filename):
    """se le ve se le ve"""
    with open(filename, 'r') as file:
        data = json.load(file)

    return data

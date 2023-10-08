#!/usr/bin/python3
"""comments again again again"""


def write_file(filename="", text=""):
    """writing into a file uknow"""
    with open(filename, mode="w", encoding="utf-8") as f:
        n_chars = f.write(text)
        f.close

    return n_chars

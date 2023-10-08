#!/usr/bin/python3
"""append(ice)<- Read it in spanish! lol"""


def append_write(filename="", text=""):
    """i dont have more jokes"""
    with open(filename, mode="a", encoding="utf-8") as f:
        n_chars = f.write(text)

    return n_chars

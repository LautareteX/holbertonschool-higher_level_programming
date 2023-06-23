#!/usr/bin/python3
"""
Append Write Functions
"""


def append_write(filename="", text=""):
    """Append new line and text"""
    if filename and text:
        with open(filename, "a", encoding="UTF8") as f:
            read_data = f.write(text)
            return read_data
    else:
        return ""

#!/usr/bin/python3
"""
Write into file function

"""


def write_file(filename="", text=""):
    """Write file"""
    if filename and text:
        with open(filename, "w", encoding="UTF8") as f:
            read_data = f.write(text)
            return read_data
    else:
        return ""

#!/usr/bin/python3
"""
Function to print text with new lines after ., ?, :
"""


def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")

    characters = ['.', ':', '?']

    for i in range(len(text)):
        if (text[i] in characters):
            print("{}".format(text[i]))
            print()
        else:
            print("{}".format(text[i]), end="")

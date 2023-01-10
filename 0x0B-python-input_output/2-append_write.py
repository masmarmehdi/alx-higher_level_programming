#!/usr/bin/python3
"""Defines a function that appends a text to a file"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file

    Args:
        filename (str): the filename in which we will append in
        text (str): the text that will be appended
    Returns:
        number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)

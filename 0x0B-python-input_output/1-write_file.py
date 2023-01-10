#!/usr/bin/python3
"""Defines a function that write into a text file"""


def write_file(filename="", text=""):
    """
    Writes a text into a text file (UTF-8)

    Args:
        filename (str): the file in which we want to write in
        text (str): the text we want to add into the filename
    Returns:
        number of charactes written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)

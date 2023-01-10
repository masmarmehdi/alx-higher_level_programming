#!/usr/bin/python3
"""Defines a function that reads a text file"""


def read_file(filename=""):
    """
    Print the contents of a UTF-8 file

    Args:
        filename (str): the file from which we will print its content
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

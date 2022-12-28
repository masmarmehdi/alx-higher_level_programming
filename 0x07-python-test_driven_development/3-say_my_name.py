#!/usr/bin/python3
"""Defines The print name funtion."""

def say_my_name(first_name, last_name=""):
    """
    Printing the full name (saying it)

    Args:
        first_name (str): first_name to print
        last_name (str): last_name to print (if provided)
    Raises:
        TypeError: if the first_name and last_name aren't string
    Return:
        The full name printed
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

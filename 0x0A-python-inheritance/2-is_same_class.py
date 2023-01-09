#!/usr/bin/python3
"""Defines a instance checking function"""


def is_same_class(obj, a_class):
    """
    Checks if an object is an instance of a specified class.

    Args:
        obj (any): the object to be checked
        a_class (type): the class to match the type of object
    Returns:
        True if they match. False, otherwise
    """
    return type(obj) == a_class

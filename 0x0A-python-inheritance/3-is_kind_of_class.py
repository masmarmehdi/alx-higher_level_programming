#!/usr/bin/python3
"""Defines a class checking inheritance"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or if an object is an instance
    of a class that inherited from, the specific class

    Args:
        obj (any): the object to be checked
        a_class (type): the class to match the type of object
    Returns:
        True, if it's kind of. False, otherwise.
    """
    return isinstance(obj, a_class)

#!/usr/bin/python3
"""Defines a function to inherti from"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class that inherited directly
    or inderectly fro the specified class

    Args:
        obj (any): the object to be checked
        a_class (type): the class that matches the type of object
    Returns:
        True, if matches. False, otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class

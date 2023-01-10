#!/usr/bin/python3
"""Defines a function that converts class to JSON"""


def class_to_json(obj):
    """
    Class to JSON

    Args:
        obj : instance of a class
    Returns:
        the dictionary description with simple DS for JSON serialization \
        of an object
    """
    return (obj.__dict__)

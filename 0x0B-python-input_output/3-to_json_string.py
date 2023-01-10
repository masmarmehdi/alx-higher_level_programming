#!/usr/bin/python3
import json
"""Defines a function that returns a json string"""


def to_json_string(my_obj):
    """
    JSON representation of an object

    Args:
        my_obj (str): the object used
    Returns:
        the json representation
    """
    return json.dumps(my_obj)

#!/usr/bin/python3
"""Defines a function from json to string"""
import json


def from_json_string(my_str):
    """
    From json to string

    Args:
        my_str (str): the str that will be converted
    Returns:
        an object represemted by a JSON string
    """
    return json.loads(my_str)

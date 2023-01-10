#!/usr/bin/python3
"""Defines a function to save object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """
    save an object file using a JSON representation

    Args:
        my_obj (obj): the object used
        filename : the file that will be written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)

#!/usr/bin/python3
"""Defines a function that create an object from JSON file"""
import json


def load_from_json_file(filename):
    """
    Load from a json file

    Args:
        filename : the file in which we will load
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)

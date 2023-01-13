#!/usr/bin/python3
"""Defines a Base class"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialization of a new Base

        Args:
            id (int): id of the base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save to file

        Args:
            list_objs (list): A list of inherited Base instance
        """
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dict = []
                for i in list_objs:
                    list_dict.append(i.to_dictionary())
                f.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """
        From json to dictionary

        Args:
            json_string (str): the json string to be changed to dict
        Return:
            empty list if json_string is None or empty. Otherwise
            a list representing json_string
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

#!/usr/bin/python3
"""Defines a student class"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initialization of a new student

        Args:
            first_name (str): first name of the student
            last_name (str): last name of the student
            age (int): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Converting to JSON

        Args:
            attrs (list): The attributes to represent if provided
        """
        if type(attrs) == list:
            if all(type(element) == str for element in attrs):
                return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the student instance

        Args:
            json (dict): data to change
        """
        for key, value in json.items():
            setattr(self, key, value)

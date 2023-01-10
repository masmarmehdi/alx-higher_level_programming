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

    def to_json(self):
        """Converting to JSON"""
        return self.__dict__

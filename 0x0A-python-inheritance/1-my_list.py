#!/usr/bin/python3
"""Defines a class that inherits from list"""


class MyList(list):
    """Inherit eveything in the built-in list class"""

    def print_sorted(self):
        """Prints a list in ascending order"""
        print(sorted(self))

#!/usr/bin/python3
"""Defines a locked class"""


class LockedClass:
    """Locked class

    prevents user from creating a new instance attribute
    dynamically unless the attribute is "first_name"

    """
    __slots__ = "first_name"

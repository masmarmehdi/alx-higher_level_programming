#!/usr/bin/python3

def safe_print_integer(value):
    """Function to print integers with format

    Args:
        value (any): the value used

    Return:
        If a ValueError or TypeError occurs it will return False.
        Otherwise it will return True
    """
    try:
        print("{:d}".format(value))
        return True
    except(ValueError, TypeError):
        return False

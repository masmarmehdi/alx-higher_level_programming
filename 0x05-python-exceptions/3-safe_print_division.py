#!/usr/bin/python3

def safe_print_division(a, b):
    """Function that divides 2 integers and prints the result

    Args:
        a (int): first element
        b (int): second element

    Returns:
        returns the value of the division. Otherwise None
    """
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)

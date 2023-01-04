#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Function tha print the first x elements of a list and only integers

    Args:
        my_list (list): the list given
        x (int): number of elements to print

    Returns:
        return the real number of integers printed
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except(ValueError, TypeError):
            continue
    print()
    return (count)

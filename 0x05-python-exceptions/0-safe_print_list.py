#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Function to print x elements of a list

    Args:
        my_list (list): the given list
        x (int): the number of elements to print

    Returns:
        return the number of elements printed
    """
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            count += 1
        except IndexError:
            break
    print()
    return (count)

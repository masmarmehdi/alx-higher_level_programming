#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    keys = a_dictionary.keys()
    for i in sorted(keys):
        print("{}: {}".format(i, a_dictionary[i]))

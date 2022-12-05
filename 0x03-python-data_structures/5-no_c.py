#!/usr/bin/python3

def no_c(my_string):
    new = ""
    for i in my_string:
        if i not in "Cc":
            new += i
    return new

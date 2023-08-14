#!/usr/bin/python3
def no_c(my_string):
    dup_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            dup_string += char
    return dup_string

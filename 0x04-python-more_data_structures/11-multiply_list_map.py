#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    multiplied = map(lambda i: i * number, my_list)
    # converting  the map object to a list
    new_list = list(multiplied)
    return new_list

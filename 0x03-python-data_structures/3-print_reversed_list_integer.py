#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # my_list.reverse()
    # i = 0
    # while i < len(my_list):
    #     print("{:d}".format(my_list[i]))
    #     i += 1
    # for i in my_list:
    i = len(my_list) - 1
    while i >= 0:
        print("{:d}".format(my_list[i]))
        i -= 1

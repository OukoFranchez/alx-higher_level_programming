#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    dup_list = my_list[:]
    if idx < 0:
        return (my_list)
    elif idx > len(my_list) - 1:
        return (my_list)
    else:
        dup_list[idx] = element
        return (dup_list)

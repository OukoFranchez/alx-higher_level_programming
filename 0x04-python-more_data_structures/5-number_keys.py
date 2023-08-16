#!/usr/bin/python3
def number_keys(a_dictionary):
    sum = 0
    length = len(a_dictionary)
    for i in range(length):
        sum += i
        i += 1
    return sum

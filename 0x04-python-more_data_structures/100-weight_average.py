#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list == []:
        return 0

    numerator = denominator = 0
    for tup_le in my_list:
        i, j = tup_le
        numerator += (i * j)
        denominator += j
    return numerator / denominator

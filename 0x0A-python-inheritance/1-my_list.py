#!/usr/bin/python3
"""This module provides classes for task 1"""


class MyList(list):
    """
    A subclass of the built-in `list` class in Python that adds a new method
    called `print_sorted` which prints
    the elements of the list in sorted order.
    """

    def print_sorted(self):
        """
        Sorts the elements of the list and prints them in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)

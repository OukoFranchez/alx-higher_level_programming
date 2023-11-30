#!/usr/bin/python3
"""
Module for task 6
"""


def find_peak(list_of_integers):
    """
    Return a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): List of unsorted integers.

    Returns:
        int or None: Peak element if found, None otherwise.
    """
    # Check for an empty list
    if list_of_integers == []:
        return None

    size = len(list_of_integers)

    # Check for a single-element list
    if size == 1:
        return list_of_integers[0]
    # Check for a two-element list
    elif size == 2:
        return max(list_of_integers)

    mid = int(size / 2)
    peak = list_of_integers[mid]

    # Check if the middle element is a peak
    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    # If the peak is on the left side, recurse on the left sub-list
    elif peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    # If the peak is on the right side, recurse on the right sub-list
    else:
        return find_peak(list_of_integers[mid + 1:])

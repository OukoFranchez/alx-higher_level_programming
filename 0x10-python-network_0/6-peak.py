#!/usr/bin/python3
"""
Module for task 6
"""

def find_peak(list_int):
    """
    Find the peak in a list of integers.

    Args:
        list_int (list): List of integers.

    Returns:
        int or None: Peak element if found, None otherwise.
    """
    # Check for an empty list
    if list_int == []:
        return None
    # Check for a single-element list
    elif len(list_int) == 1:
        return list_int[0]
    # Check for a two-element list
    elif len(list_int) == 2:
        return list_int[0] if list_int[0] > list_int[1] else list_int[1]
    else:
        # Iterate through the list
        for i in range(1, (len(list_int) + 1) // 2):
            back = len(list_int) - i - 1
            # Check if the current element is a peak
            if list_int[i] >= list_int[i - 1] and list_int[i] >= list_int[i + 1]:
                return list_int[i]
            # Check if the corresponding element from the end is a peak
            elif list_int[back] >= list_int[back - 1] and list_int[back] >= list_int[back + 1]:
                return list_int[back]
    # No peak found
    return None

#!/usr/bin/python3

def find_peak(lst):
    """
    Find the peak in a list of integers.

    Args:
        lst (list): List of integers.

    Returns:
        int or None: Peak element if found, None otherwise.
    """
    # Check for an empty list
    if not lst:
        return None
    # Check for a single-element list
    elif len(lst) == 1:
        return lst[0]
    # Check for a two-element list
    elif len(lst) == 2:
        return max(lst[0], lst[1])
    else:
        # Iterate through the list
        for i in range(1, (len(lst) + 1) // 2):
            back = len(lst) - i - 1
            # Check if current element is a peak
            if lst[i] >= lst[i - 1] and lst[i] >= lst[i + 1]:
                return lst[i]
            # Check if corresponding element from the end is a peak
            elif lst[back] >= lst[back - 1] and lst[back] >= lst[back + 1]:
                return lst[back]
    # No peak found
    return None

#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    r_dictn = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    decimal = 0
    for i in range(len(roman_string)):
        current = r_dictn[roman_string[i]]
        if i + 1 < len(roman_string):
            if r_dictn[roman_string[i + 1]] > current:
                current = -current
        decimal += current

    return decimal

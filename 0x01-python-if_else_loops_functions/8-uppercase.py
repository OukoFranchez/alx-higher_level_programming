#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        unicode_val = ord(char)
        if unicode_val > 96 and unicode_val < 123:
            upper_char = chr(unicode_val - 32)
            result += upper_char
        else:
            result += char
    print("{}".format(result))

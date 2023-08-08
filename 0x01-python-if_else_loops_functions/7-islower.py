#!/usr/bin/python3
def islower(c):
    unicode_val = ord(c)

    if unicode_val >= 97 and unicode_val < 123:
        return True
    else:
        return False

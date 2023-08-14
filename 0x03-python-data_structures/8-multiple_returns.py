#!/usr/bin/python3
def multiple_returns(sentence):
    sentence_tuple = tuple(sentence)
    if sentence_tuple == ():
        return (0, None)
    else:
        length = len(sentence_tuple)
        first_char = sentence_tuple[0]
        return (length, first_char)

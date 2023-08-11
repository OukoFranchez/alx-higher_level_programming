#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("1 argument:")
        print("1:", argv[1])
    else:
        x = 0
        print(len(argv) - 1, "arguments:")
        for i in argv[1:]:
            x += 1
            print(str(x) + ":", i)

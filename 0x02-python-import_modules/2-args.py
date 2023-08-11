#!/usr/bin/python3
import sys
if len(sys.argv) == 1:
    print("0 arguments")
elif len(sys.argv) == 2:
    print("1 argument:")
    print("1:", sys.argv[1])
else:
    x = 0
    print(len(sys.argv) - 1, "arguments:")
    for i in sys.argv[1:]:
        x += 1
        print(str(x) + ":", i)

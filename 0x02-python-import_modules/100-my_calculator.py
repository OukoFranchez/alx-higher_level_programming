#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":
    if len(argv) < 3:
        print("Usage:", argv[0], "<a> <operator> <b>")
        quit(1)

    operators = ['+', '-', '*', '/']

    if argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        quit(1)

    a = int(argv[1])
    b = int(argv[3])

    if argv[2] == "+":
        print(a, argv[2], b, "=", add(a, b))
    elif argv[2] == "-":
        print(a, argv[2], b, "=", sub(a, b))
    elif argv[2] == "*":
        print(a, argv[2], b, "=", mul(a, b))
    else:
        print(a, argv[2], b, "=", div(a, b))

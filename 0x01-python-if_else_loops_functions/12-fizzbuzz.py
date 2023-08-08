#!/usr/bin/python3
def fizzbuzz():
    fizz = "Fizz"
    buzz = "Buzz"
    fiz_and_buzz = "FizzBuzz"
    for i in range(1, 101):
        if ((i % 3 == 0) and (i % 5 == 0)):
            print(f"{fiz_and_buzz} ", end="")
        elif i % 3 == 0:
            print(f"{fizz} ", end="")
        elif i % 5 == 0:
            print(f"{buzz} ", end="")
        else:
            print(f"{i} ", end="")

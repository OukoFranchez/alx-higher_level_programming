#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
last_digit_str = "and is less than 6 and not 0"
if (last_digit > 5):
    print("Last digit of", number, "is", last_digit, "and is greater than 5")
elif (last_digit == 0):
    print("Last digit of", number, "is", last_digit, "and is 0")
elif (last_digit < 6 and not 0):
    print("Last digit of", number, "is", -last_digit, last_digit_str)
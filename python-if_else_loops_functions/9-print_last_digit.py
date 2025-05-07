#!/usr/bin/python3

def print_last_digit(number):
    if number >= 0:
        print("{}".format(number % 10), end="")
        return (number % 10)
    else:
        num = abs(number) % 10
        print("{}".format(num), end="")
        return (num)

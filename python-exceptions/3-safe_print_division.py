#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        r = a / b
        print("Inside result: {}".format(r))
        return r
    except ZeroDivisionError:
        print("Inside result: {}".format(None))
        return None

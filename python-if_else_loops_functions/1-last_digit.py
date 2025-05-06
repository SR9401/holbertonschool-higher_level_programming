#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number % 10
if number < 0:
    num = abs(number) % 10
    if num == 0:
        print("Last digit of %s is 0 and is 0" % (number))
    else:
        print("Last digit of %s is -%s" % (number, num), end=" ")
        print("and is less than 6 and not 0")
elif number > 0:
    if num <= 5:
        print("Last digit of %s is %s" % (number, num), end=" ")
        print("and is less than 6 and not 0")
    elif num > 5:
        print("Last digit of %s is %s and is greater than 5" % (number, num))
    else:
        print("Last digit of %s is 0 and is 0" % (number))
else:
    print("Last digit of %s is 0 and is 0" % (number))

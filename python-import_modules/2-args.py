#!/usr/bin/python3
import sys
count = len(sys.argv) - 1
i = 1
if count == 0:
    print("{} arguments.".format(count))
elif count == 1:
    print("{} argument.".format(count))
    print("{}: {}".format(i, sys.argv[i]))
else:
    print("{} arguments:".format(count))
    while i <= count:
        print("{}: {}".format(i, sys.argv[i]))
        i += 1

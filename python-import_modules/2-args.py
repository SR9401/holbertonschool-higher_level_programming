#!/usr/bin/python3
import sys
count = len(sys.argv) - 1
i = 1
if count == 0:
    print("{} argument.".format(count))
else:
    print("{} argument:".format(count))
    while i <= count:
        print("{}: {}".format(i, sys.argv[i]))
        i += 1

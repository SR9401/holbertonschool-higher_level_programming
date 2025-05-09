#!/usr/bin/python3
import sys
count = len(sys.argv)
i = 1
res = 0
while i <= count:
	y = sys.argv[i]
	x = int(y)
	res += x
	i += 1
print("{}".format(res))
#!/usr/bin/python3

print("\n".join("{0} = {1}".format(i, hex(i)) for i in range(99)if chr(i)))

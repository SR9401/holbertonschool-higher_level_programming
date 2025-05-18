#!/usr/bin/python3
def print_square(size):
	if size < 0:
		raise ValueError("size must be >= 0")
	if not isinstance(size, (int)):
		raise TypeError("size must be an integer")
	if size > 0:
		i = 1
		while i <= size:
			j = 1
			while j <= size:
				print("#", end="")
				j += 1
			print("")
			i += 1
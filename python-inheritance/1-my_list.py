#!/usr/bin/python3

class MyList(list):
    """class mylist inheritance of list"""

    def print_sorted(self):
        """sorted list"""

        print("{}".format(sorted(self)))

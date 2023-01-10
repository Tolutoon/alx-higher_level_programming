#!/usr/bin/python3
""" Class MyList inherits from list """


class MyList(list):
    """ Prints the list but in sorted format """
    def print_sorted(self):
        """ prints the list in sorted format """
        print(sorted(self))

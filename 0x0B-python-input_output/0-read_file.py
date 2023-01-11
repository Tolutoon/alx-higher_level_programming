#!/usr/bin/python3
""" Defines a function that reads a UTF8 text file """


def read_file(filename=""):
    """Prints the details of the file to stdout. """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")


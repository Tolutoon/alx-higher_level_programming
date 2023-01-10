#!/usr/bin/python3
""" A function that returns true if the object is the same instance
    as the specified class
"""

def is_same_class(obj, a_class):
    """returns True if the object is exactly an instance """
    if type(obj) == a_class:
        return True
    return False

#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Returns the integer addition of aruguments a and b.


    Float arguments are casted to ints before any arthmetric
    operation is taken place.

    Raises:
        TypeError: If either of a or b is non-integer and non-float.
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

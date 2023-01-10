#!/usr/bin/python3

""" Defines a class and inherited class-checking function """


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited intsance of a class.

    Args:
        obj: The object to check.
	a_class: The class to match the type.
    Returns:
        True if the object is an instance of the a_class
	Otherwise - False.
    """
    return (isinstance(obj, a_class))
   

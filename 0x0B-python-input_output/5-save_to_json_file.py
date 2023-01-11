#!/usr/bin/python3
""" Defines a JSON file-writing function. """
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON represntation."""
    with open(filename, "w") as myFile:
        json.dump(my_obj, myFile)

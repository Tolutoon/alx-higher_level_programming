#!/usr/bin/python3
import string

for letter in string.ascii_lowercase:
    if letter != "q" and letter != "e":
        print("{}".format(letter), end="")

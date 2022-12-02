#!/usr/bin/python3

from sys import argv

def add_args():
    argc = len(argv)
    i = 1
    sum = 0
    while i < argc:
        sum += int(argv[i])
        i += 1
    print("{:d}".format(sum))

if __name__ == "__main__":
    add_args()

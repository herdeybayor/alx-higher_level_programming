#!/usr/bin/python3

"""
function that appends a string at the end of a text file (UTF8)
"""


def append_write(filename, text=""):
    """ module append_write """
    with open(filename, 'a') as f:
        return f.write(text)

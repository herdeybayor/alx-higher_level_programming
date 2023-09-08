#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Return the sum of two integers.

    Args:
        a (int): The first integer to add.
        b (int): The second integer to add.

    Returns:
        The return value. a + b

    Raises:
        TypeError: If either of a or b is a non-integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

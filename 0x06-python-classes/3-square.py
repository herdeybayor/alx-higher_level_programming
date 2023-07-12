#!/usr/bin/python3
""" Define a class Square """


class Square:
    """ Represent a square """
    def __init__(self, size=0):
        """ Initialize Square class
        Args: size(int): size of a side of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2
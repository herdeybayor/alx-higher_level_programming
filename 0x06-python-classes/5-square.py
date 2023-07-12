#!/usr/bin/python3
""" Define a class Square """


class Square:
    """ Represent a square """
    def __init__(self, size=0):
        """ Initialize Square class
        Args: size(int): size of a side of the square
        """
        self.__size = size

    @property
    def size(self):
        """ Getter method """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter method
        Args: value(int): size of a side of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the # character."""
        for x in range(self.__size):
            print("#" * self.__size)
        if self.__size == 0:
            print("")

#!/usr/bin/python3
""" Module that defines a singly linked list """


class Node:
    """ Defines a node of a singly linked list """

    def __init__(self, data, next_node=None):
        """Initializes the node object
        Args:
            data (int): data of the node
            next_node (Node): next node
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ Getter of data
        Returns:
            data of the node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """ Setter of data
        Args:
            value (int): data of the node
        Returns:
            data of the node
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ Getter of next_node
        Returns:
            next_node of the node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Setter of next_node
        Args:
            value (Node): next node
        Returns:
            next_node of the node
        """
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ Defines a singly linked list """

    def __init__(self):
        """ Initializes the singly linked list """
        self.__head = None

    def sorted_insert(self, value):
        """ Inserts a new node in the correct sorted position
        Args:
            value (int): data of the node
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
            return
        if self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        current = self.__head
        while current.next_node is not None:
            if current.next_node.data > value:
                break
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """ Prints the singly linked list
        Returns:
            Formatted string representing the singly linked list
        """
        current = self.__head
        string = ""
        while current is not None:
            string += str(current.data) + "\n"
            current = current.next_node
        return string[:-1]

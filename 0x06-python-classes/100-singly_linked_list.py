#!/usr/bin/python3
"""
Module 100-singly_linked_list
"""


class Node:
    """
    class Node definition
    """

    def __init__(self, data, next_node=None):
        """
        Initializes node

        Args:
            data (int): private
            next_node : private; can be None or Node object
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """"
        Get
        Return: data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """"
        Get
        Return: next_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set
        """
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    class SinglyLinkedList definition
    """

    def __init__(self):
        """
        Initializes singly linked list

        Args:
            head: private
        """
        self.__head = None

    def __str__(self):
        """
        Sets the string representation of singly linked list needed to be print
        """
        sll_string = ""
        node = self.__head
        while node is not None:
            sll_string += str(node.data) + "\n"
            node = node.next_node

        return sll_string

    def sorted_insert(self, value):
        """
        Inserts new nodes in sorted order.

        Args:
        value: int data for node
        """
        node = self.__head

        if node is None or self.__head.data >= value:
            self.__head = Node(value, self.__head)
        else:
            while node.next_node is not None and node.next_node.data < value:
                node = node.next_node
            node.next_node = Node(value, node.next_node)

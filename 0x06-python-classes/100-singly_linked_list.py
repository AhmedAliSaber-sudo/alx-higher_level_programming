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
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
            return

        tmp = self.__head
        if new_node.data < tmp.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        while (tmp.next_node is not None) and (new_node.data > tmp.next_node.data):
            tmp = tmp.next_node
        new_node.next_node = tmp.next_node
        tmp.next_node = new_node
        return

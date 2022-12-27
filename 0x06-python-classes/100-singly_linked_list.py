#!/usr/bin/python3

""" Define a Node class """

class Node:
    """ Node Class """
    def __init__(self, data, next_node=None):
        """ Initialize a new node.
        
        Args:
            data (int): new Node's data.
            next_node (Node): next node of the Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Get data of the node. """
        return (self.__data)

    @data.setter
    def data(self, value):
        """ Set data of the node. """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ Get the next node of the node. """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """ Set the next node of the node. """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ Singly linked list class """
    def __init__(self):
        """ Initialize a new Singly linked list """
        self.__head = None
    
    def sorted_insert(self, value):
        """ Inserting a new Node to the SinglyLinkedList class.

        The node is inserted in the list in an ordered way.

        Args:
            value (Node): the new Node to insert.
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head
            while temp.next_node is not None and temp.next_node.data < value:
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self):
        """ Returning elements of the SinglyLinkedList to print. """
        elements = []
        temp = self.__head
        while temp is not None:
            elements.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(elements))


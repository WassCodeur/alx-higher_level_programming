#!/usr/bin/python3
"""single linked list"""


class Node:
    """Node templates"""

    def __init__(self, data, next_node=None):
        self._data = None
        self._next_node = None
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """get current node value"""
        return self._data

    @data.setter
    def data(self, value):
        """set new value to the current node"""
        if not isinstance(value, int):
            raise TypeError("data doit être un entier")
        self._data = value

    @property
    def next_node(self):
        """next node"""
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """set value to the next_noe"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node doit être un objet Node")
        self._next_node = value


class SinglyLinkedList:
    """class singly linked list"""

    def __init__(self):
        """initialization"""
        self.head = None

    def sorted_insert(self, value):
        """public method to insert a new node"""
        new_node = Node(value)

        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while (current.next_node is not None and
                    current.next_node.data < value):
                current = current.next_node

            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """ public method __str__"""
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)

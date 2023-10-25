#!/usr/bin/python3
"""NODE CLASS"""


class Node():
    """data representation"""
    def __init__(self, value, next_node):
        """initiate the value"""

        if (type(value) is not int):
            raise TypeError("data must be an integer")
            return
        if (type(value) is not Node or type(value) is not None):
            raise TypeError("next_node must be a Node object")
            return
        self.__data = value
        self.__next_node = next_node

    @property
    def data(self):
        """get data"""
        return (self.__value)

    @data.setter
    def data(self, value):
        """set data"""
        if (type(value) is not int):
            raise TypeError("data must be an integer")
            return
        self.__data = value

    @property
    def next_node(self):
        """get next_node"""
        return (self.next_node)

    @data.setter
    def next_node(self, value):
        """sett next_node"""
        if (type(value) is not Node or type(value) is not None):
            raise TypeError("next_node must be a Node object")
            return
        self.__next_node = value


class SinglyLinkedList():
    def __init__(self, head):
        self.__head = head

    def __str__(self):
        """make list printable"""
        list = []
        node = self.__head
        while (node is not None):
            list.append(node.data)
            node = node.next_node
        print(list[::-1])

        def sorted_insert(self, value):
            """
            Insert a node , in s sorted way
            value: the value of the node
            """

            new = Node(value)
            if self.__head is None:
                new.next_node = None
                self.__head = new
            elif self.__head.data > value:
                new.next_node = self.__head
                self.__head = new
            else:
                tmp = self.__head
                while (tmp.next_node is not None and
                        tmp.next_node.data < value):
                    tmp = tmp.next_node
                new.next_node = tmp.next_node
                tmp.next_node = new

from doubly_node import Node
from typing import Any

class DoublyLinkedList:
    def __init__(self, head: Node=None, tail: Node=None) -> None:
        """ Instantiate the linked list with a node if any are given """
        self.head = head
        self.tail = tail

        # Adjust for single node entries
        if self.head != None and self.tail == None:
            self.tail = head
        if self.head == None and self.tail != None:
            self.head = tail

    def insertAtEnd(self, node: Node=None) -> None:
        """ This is useful when using a DLL as a queue or stack """

        # Start of DLL edge case
        if self.head == None:
            self.head = node
        else:
            self.tail.setNext(node)

        self.tail = node

    def insertByIndex(self, node: Node=None, index=0) -> bool:
        """ This is useful for specified insertions of nodes, returns whether the node was added or not """

        # Start of DLL edge case
        if index == 0:
            # Edge case: DLL is empty
            if self.head == None:
                self.tail = node
            else:
                self.head.setPrev(node)

            self.head = node
            return True

        else:
            count = 0
            current_node = self.head

            # Loop until end of the DLL
            while current_node != None:
                if count == index:
                    # Insert at end case
                    if current_node.getNext() == None:
                        current_node.setNext(node)
                        self.tail = node
                        node.setPrev(current_node)
                        return True

                    # Insert in middle case
                    else:
                        # Store the next, next node
                        right_side = current_node.getNext().getNext()
                        current_node.setNext(node)
                        node.setNext(right_side)
                        right_side.setPrev(node)
                        return True

        return False

    def remove(self, value: Any=None) -> Node:
        """ Removes the node and returns it, if it exists """
        
        # Edge case: Size of DDL is 1
        if self.head.getValue() == self.tail.getValue() == value and self.head.getNext() == None:
            node = Node(value=self.head.getValue())
            self.head = None
            self.tail = None

            return node

        # Edge case: Size of DDL is not 1, removing head
        if self.head.getValue() == value:
            node = Node(value=self.head.getValue())
            self.head = self.head.getNext()
            self.head.setPrev(None)

            return node

        # Edge case: Size of DDL is not 1, removing tail
        if self.tail.getValue() == value:
            node = Node(value=self.tail.getValue())
            self.tail = self.tail.getPrev()
            self.tail.setNext(None)

            return node

        # Normal removal case, node is in the middle and size of DDL >= 3
        current_node = self.head.getNext()
        while current_node != None:
            if current_node.getValue() == value:
                node = Node(value=current_node.getValue())
                # Reassign the links
                current_node.getPrev().setNext(current_node.getNext())
                current_node.getNext().setPrev(current_node.getPrev())
                # Remove links
                current_node.setNext(None)
                current_node.setPrev(None)

                return node

        return None





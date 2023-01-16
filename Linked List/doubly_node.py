# This import allows the Node class to reference itself in type hints
from __future__ import annotations

# Helpful for the Any typing for type hints
from typing import Any

class Node:
    def __init__(self, value: Node=None, prev: Node=None, next: Node=None):
        """ Instantiate a node that supports doubly linked operations """
        self.value = value
        self.prev = prev
        self.next = next

    def getPrev(self) -> Node:
        return self.prev

    def getNext(self) -> Node:
        return self.next

    def getValue(self) -> Any:
        return self.value

    def setPrev(self, prev: Node=None) -> None:
        self.prev = prev

    def setNext(self, next: Node=None) -> None:
        self.next = next

    def setValue(self, value: Any=None) -> None:
        self.value = value
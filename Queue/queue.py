from typing import Any

class Queue:
    def __init__(self):
        """ Instantiate an empty queue """
        self.values = []

    def push(self, value: Any):
        """ Insert an item to the back of the queue """
        self.values.append(value)

    def pop(self) -> Any:
        """ Delete the value and return it, if it exists """

        # Edge case: queue is empty
        if len(self.values) == 0:
            return None

        return self.values.pop(0)

    def size(self) -> int:
        """ Return the size of the queue """
        return len(self.values)

    def peek(self) -> Any:
        """ Return the value of the next item in the queue, if any, without removing it """

        # Edge case: queue is empty
        if len(self.values) == 0:
            return None

        return self.values[0]
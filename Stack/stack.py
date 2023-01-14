import typing


class Stack:
    def __init__(self):
        self.values = []

    def push(self, value: typing.Any) -> None:
        """ Inserts a value onto the top of the stack """
        self.values.append(value)

    def pop(self) -> typing.Any:
        """ Removes the top most value and returns that value, if any """
        if len(self.values) == 0:
            return None

        value = self.values[-1]
        del self.values[-1]
        return value

    def peek(self) -> typing.Any:
        """ Returns the top most value on the stack, if any """
        if len(self.values) == 0:
            return None

        return self.values[-1]

    def size(self) -> int:
        """ Returns the size of the stack """
        return len(self.values)
    
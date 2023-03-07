class Stack():
    def __init__(self, size: int) -> None:
        self._stack = []
        self._size = size


    def push(self, value):
        if len(self._stack) == self._size:
            return -1
        else:
            self._stack.append(value)

    def pop(self):
        return self._stack.pop()

    def peek(self):
        print(self._stack[-1])

    def clear(self):
        self._stack.clear()

    def display(self):
        print(self._stack)

    def empty(self):
        return len(self._stack) == 0

from collections import deque
class Dstack(Stack):
    def __init__(self, size=None) -> None:
        self._stack = deque()
        self._size = size

    def push(self, value):
        self._stack.append(value)

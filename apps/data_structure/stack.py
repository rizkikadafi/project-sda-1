class Stack():
    stack = []

    def __init__(self, size: int) -> None:
        self.size = size


    def push(self, value):
        if len(self.stack) == self.size:
            return -1
        else:
            self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        print(self.stack[-1])

    def clear(self):
        self.stack.clear()

    def display(self):
        print(self.stack)

    def empty(self):
        return len(self.stack) == 0

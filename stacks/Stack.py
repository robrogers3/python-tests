from collections import deque

class Stack():
    def __init__(self):
        self.stack = deque()

    def push(self, item):
        self.stack.append(item)

        return self

    def pop(self):
        if self.empty():
            raise Exception('stack is empty')

        return self.stack.pop()

    def peek(self):
        if self.empty():
            raise Exception('stack is empty')

        return self.stack[-1]

    def empty(self):
        return len(self.stack) == 0

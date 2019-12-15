from collections import deque

class StackWithMax:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def empty(self, stack):
        return len(stack) == 0

    def max(self):
        if self.empty(self.max_stack):
            raise Exception('max stack empty')

        return self.max_stack[-1]

    def push(self, item):
        if self.empty(self.max_stack) or item >= self.max():
            self.max_stack.append(item)


        self.stack.append(item)

    def pop(self):
        if self.empty(self.stack):
            raise Exception('stack empty')

        item = self.stack.pop()

        if item == self.max():
            self.max_stack.pop()

        return item


class StackWithMaxX:
    def __init__(self):
        self.stack = deque()
        self.max_stack = deque()

    def empty(self, stack):
        return len(stack) == 0

    def max(self):
        if self.empty(self.max_stack):
            raise Exception('max stack empty')

        return self.max_stack[-1]

    def push(self, item):
        if self.empty(self.max_stack):
            self.max_stack.append(item)

        if item > self.max():
            self.max_stack.append(item)

        self.stack.append(item)

    def pop(self):
        if self.empty(self.stack):
            raise Exception('stack is empty')

        item = self.stack.pop()

        if item == self.max():
            self.max_stack.pop()

        return item

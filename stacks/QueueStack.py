from collections import deque

class QueueStack():
    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()

    def enqueue(self, item):
        self.s1.append(item)

    def dequeue(self):
        if self.empty(self.s2):
            self.flushToS2()
        if self.empty(self.s2):
            raise Exception('stack is empty')

        return self.s2.pop()

    def flushToS2(self):
        while(not self.empty(self.s1)):
            self.s2.append(self.s1.pop())

    def empty(self, s):
        return len(s) == 0

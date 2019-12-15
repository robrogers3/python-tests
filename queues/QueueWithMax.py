import queue
from collections import deque

class QueueWithMax:
    def __init__(self):
        self.mainq = queue.Queue()
        self.maxq = deque()

    def enqueue(self, item):
        self.mainq.put(item)

        while len(self.maxq) and self.maxq[0] < item:
            self.maxq.popleft()

        self.maxq.appendleft(item)

    def deque(self):
        item = self.mainq.get()

        if self.maxq[-1] == item:
            popped = self.maxq.pop()

        return item

    def findMax(self):
        return self.maxq[-1]

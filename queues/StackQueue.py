class StackQueue:
    def __init__(self):
        self.writeQ = []
        self.readQ = []

    def add(self, item):
        self.writeQ.append(item)

    def get(self):
        if self.empty(self.readQ):
            self.flushToReadQ()

        if self.empty(self.readQ):
            raise Exception('Queue is empty')

        return self.readQ.pop()

    def flushToReadQ(self):
        while not self.empty(self.writeQ):
            self.readQ.append(self.writeQ.pop())

    def empty(self, q):
        return len(q) == 0

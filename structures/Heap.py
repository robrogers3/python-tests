class Heap:
    def __init__(self, capacity):
        self.items = [None] * capacity
        self.size = 0

    def __len__(self):
        return self.size

    def empty(self):
        return self.size == 0

    def length(self):
        return self.size

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def isValid(self,i):
        return i >= 0 and i < self.size

from heaps import MaxHeap
from collections import defaultdict

class BuildingMap:
    def __init__(self):
        self.map = defaultdict(list)
        self.heap = MaxHeap()

    def put(self, height):
        self.heap.push(height)
        self.map[height].append(height)

    def remove(self, height):
        if height not in self.map:
            print(f'height {height} not in map')
            return

        n = self.map[height].pop()

        self.heap.remove(n)

        if len(self.map[height]) == 0:
            self.map.pop(height)

    def getMax(self):
        if self.heap.empty():
            return 0
        return self.heap.peek()

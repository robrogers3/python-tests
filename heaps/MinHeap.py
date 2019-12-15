import heapq

class MinHeap:
    def __init__(self, items = []):
        self.heap = items[:]
        heapq.heapify(self.heap)

    def push(self, item):
        heapq.heappush(self.heap, item)
        return self

    def pop(self):
        return heapq.heappop(self.heap)

    def peek(self):
        return self.heap[0]

    def remove(self, item):
        if item not in self.heap:
            return None

        reheapify = False
        if self.peek() == item:
            reheapify = True

        self.heap.remove(item)

        if reheapify:
            heapq.heapify(self.heap)
        return item

    def empty(self):
        return len(self.heap) == 0

    def __getitem__(self, item):
        return self.heap[item]
    def __len__(self):
        return len(self.heap)

    def getItems(self):
        return self.heap

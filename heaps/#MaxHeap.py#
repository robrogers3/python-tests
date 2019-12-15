import heapq
import inspect
from heaps.MinHeap import MinHeap

class Comparator:
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return repr(self.val)

    def __eq__(self, other):
        return self.val == other

    def __lt__(self, other):
        return self.val > other.val

    def __le__(self, other):
        return self.val >= other.val

    def __gt__(self, other):
        return self.val < other

    def __ge__(self, other):
        return self.val <= other.val

    def __eq__(self, other):
        return self.val == other

    def __ne__(self, other):
        return self.val != other

class MaxHeap(MinHeap):
    def push(self, item):
        heapq.heappush(self.heap, Comparator(item))
        return self
    def peek(self):
        return self.heap[0].val

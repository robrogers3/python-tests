from structures import Utils, Heap
import sys

class MinHeap(Heap):
    def peek(self):
        return self.getMin()

    def getMin(self):
        if self.size == 0:
            raise Exception('HeapEmpty')

        return self.items[0]

    def push(self,item):
        if self.size >= len(self.items):
            raise Exception('HeapFull')

        self.items[self.size] = item

        indexItem = self.size

        self.size += 1

        self.propagateUp(indexItem)

        return self

    def propagateUp(self,i):
        parent = self.parent(i)
        while i > 0 and self.items[parent] > self.items[i]:
            Utils.swap(self.items, parent, i)
            i = parent
            parent = self.parent(i)

    def pop(self):
        return self.removeMin()

    def removeMin(self):
        if self.size == 0:
            raise Exception('HeapEmpty')

        item = self.items[0]

        Utils.swap(self.items, 0, self.size - 1)

        self.size -= 1

        self.heapify(0)

        return item

    def heapify(self, i):
        if not self.isValid(i):
            return

        left =  self.items[self.left(i)]  if self.isValid(self.left(i)) else 999999
        right = self.items[self.right(i)] if self.isValid(self.right(i)) else 999999

        minEl = min(left,right,self.items[i])

        minIdx = i
        if minEl == left:
            minIdx = self.left(i)
        elif minEl == right:
            minIdx = self.right(i)

        if minIdx != i:
            Utils.swap(self.items, i, minIdx)
            self.heapify(minIdx)

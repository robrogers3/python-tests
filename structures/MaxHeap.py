from . import Utils, Heap
import sys

class MaxHeap(Heap):
    def peek(self):
        return self.getMax()

    def getMax(self):
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

    def pop(self):
        return self.removeMax()

    def removeMax(self):
        if self.size == 0:
            raise Exception('HeapEmpty')

        item = self.items[0]

        Utils.swap(self.items, 0, self.size - 1)

        self.size -= 1

        self.heapify(0)

        return item

    def remove(self,i):
        if not self.isValid(i):
            raise Exception('Illegale node index')

        item = self.items[i]

        Utils.swap(self.items, i, self.size - 1)

        self.size -= 1

        if i != 0 and self.items[self.parent(i)] < self.items[i]:
            self.propagateUp(i)
        else:
            self.heapify(i)

        return item

    def propagateUp(self,i):
        parent = self.parent(i)
        while i > 0 and self.items[parent] < self.items[i]:
            Utils.swap(self.items, parent, i)
            i = parent
            parent = self.parent(i)

    def heapify(self, i):
        if not self.isValid(i):
            return

        left =  self.items[self.left(i)]  if self.isValid(self.left(i)) else -999999
        right = self.items[self.right(i)] if self.isValid(self.right(i)) else -999999

        maxEl = max(left,right,self.items[i])

        maxIdx = i
        if maxEl == left:
            maxIdx = self.left(i)
        elif maxEl == right:
            maxIdx = self.right(i)

        if maxIdx != i:
            Utils.swap(self.items, i, maxIdx)
            self.heapify(maxIdx)

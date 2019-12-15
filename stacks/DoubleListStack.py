from numpy import ndarray

class DoubleListStack:
    def __init__(self, size):
        if size < 2:
            raise Exception('stack size must be greater than one')
        self.size = size
        self.stack = [None] * size
        self.sp1 = 0
        self.sp2 = size - 1

    def pushLeft(self, item):
        if self.sp1 > self.sp2:
            raise Exception('stack full')

        self.stack[self.sp1] = item

        self.sp1 += 1

    def pushRight(self, item):
        if self.sp1 > self.sp2:
            raise Exception('stack full')

        self.stack[self.sp2] = item
        self.sp2 -= 1

    def popLeft(self):
        if self.sp1 == 0:
            raise Exception('stack empty')
        self.sp1 -= 1
        item = self.stack[self.sp1]
        return item

    def popRight(self):
        if self.sp2 == self.size - 1:
            raise Exception('stack empty')
        self.sp2 += 1
        item = self.stack[self.sp2]
        return item


class DoubleListStackX:
    def __init__(self,size):
        if size < 2:
            raise Exception('Stack Size must be greater than two')
        self.size = size
        self.stack = ndarray((size,), int)
        self.s1p = 0
        self.s2p = size - 1

    def pushLeft(self, item):
        if self.s1p > self.s2p:
            raise Exception('stack full')

        self.stack[self.s1p] = item

        self.s1p += 1

    def pushRight(self, item):
        if self.s1p > self.s2p:
            raise Exception('stack full')

        self.stack[self.s2p] = item

        self.s2p -= 1

    def popLeft(self):
        if self.s1p < 1:
            raise Exception('left stack empty')

        self.s1p -= 1

        item = self.stack[self.s1p]

        return item


    def popRight(self):
        if self.s2p == self.size - 1:
            raise Exception('right stack empty')

        self.s1p -= 1

        item = self.stack[self.s1p]

        return item

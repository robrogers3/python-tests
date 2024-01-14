from . import MinHeap, MaxHeap

class RunningMedian:
    def __init__(self):
        self.high = MinHeap(60)
        self.low = MaxHeap(60)

    def median(self):
        if self.low.empty() and self.high.empty():
            raise Exception('No data')

        if self.high.length() == self.low.length():
            return (self.high.peek() + self.low.peek())/2.0

        # high has median if high is longer
        return self.high.peek()

    def insert(self, num):
        if self.high.empty():
            self.high.push(num)
            return self

        #need to incr high as high should be larger than low
        if self.high.length() == self.low.length():
            #retain len high >= low
            if num < self.low.peek():
                self.high.push(self.low.pop())
                self.low.push(num)
            else:
                self.high.push(num)
        else:
            #retain len high >= low
            if num > self.high.peek():
                self.low.push(self.high.pop())
                self.high.push(num)
            else:
                self.low.push(num)

        return self


    def insertMany(self, nums):
        for num in nums:
            self.insert(num)

        return self

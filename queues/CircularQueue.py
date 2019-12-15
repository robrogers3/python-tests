class CircularQueue:
    def __init__(self, max_size):
        if max_size < 1:
            raise Exception('Size must be greater than zero')

        self.max_size = max_size
        self.q = list()
        self.front = 0
        self.back = 0
        self.length = 0


    def __str__(self):
        data = [f"{item}" for item in self.q]
        rv =  'q = ' + ', '.join(data)
        return rv

    def enqueue(self, item):
        if self.full():
            raise Exception('Queue Full')

        self.q.insert(self.back,item)
        self.back = (self.back + 1) % self.max_size
        self.length += 1
        return self

    def dequeue(self):
        if self.empty():
            raise Exception('Queue Empty')

        item = self.q[self.front]

        self.front = (self.front + 1) % self.max_size
        self.length -= 1

        return item

    def full(self):
        return self.length == self.max_size - 1
    #    return self.size() == self.max_size - 1

    def empty(self):
        return self.length == 0
        return self.size() == 0

    def size(self):
        return self.length
        if self.back >= self.front:

            return self.back - self.front

        return self.max_size - (self.front - self.back)

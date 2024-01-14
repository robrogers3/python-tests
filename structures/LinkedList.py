class Pointer:
    def __init__(self, value = None):
        self.value = value
        self.next = None

    # def __repr__(self):
    #     return f'repr: {self.value}'

    def __str__(self):
        return f'{self.value} -> {self.next}'

class LinkedList:
    def __init__(self, items = []):
        self.head = Pointer()
        self.tail = Pointer()
        self.head.next = self.tail
        if not len(items):
            return

        self.head.next = Pointer(items[0])
        curr = self.head.next
        for item in items[1:]:
            curr.next = Pointer(item)
            curr = curr.next

        curr.next = self.tail
        print(self.tail)

    def add(self, item):
        if self.head == self.tail:
            self.head.next = Pointer(item)
            pointer.next = self.tail
            return


        pointer =  self.head
        while pointer.next != self.tail:
            pointer = pointer.next

        pointer.next = Pointer(item)
        pointer.next = self.tail


    def __len__(self):
        c = 0
        p = self.head.next
        while p:
            print(type(p))
            c += 1
            p = p.next

        return c

    def __str__(self):
        c = 0
        p = self.head
        b = []
        while p.next:
            p = p.next
            b.append(f'{p.value}')
            c += 1
        return '->'.join(b)

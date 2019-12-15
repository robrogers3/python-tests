import unittest
from queues import CircularQueue, QueueWithMax, StackQueue

class TestQueues(unittest.TestCase):
    def test_stack_queue(self):
        q = StackQueue()
        q.add(1)
        q.add(2)
        el = q.get()
        self.assertEqual(el,1)
        q.add(3)
        el = q.get()
        self.assertEqual(el,2)

    def test_it_dequeues_in_proper_order(self):
        q = CircularQueue(3)
        q.enqueue(1)
        q.enqueue(2)
        item = q.dequeue()
        self.assertEqual(item, 1)
        item = q.dequeue()
        self.assertEqual(item, 2)

    def test_it_respects_constraints(self):
        q = CircularQueue(3)
        r = q.empty()
        self.assertEqual(r, True)
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(q.full(), True)
        item = q.dequeue()
        self.assertEqual(item, 1)
        q.enqueue(3)
        item = q.dequeue()
        self.assertEqual(item, 2)
        item = q.dequeue()
        self.assertEqual(item, 3)

    def test_queue_with_max_knows_the_max(self):
        q = QueueWithMax()
        q.enqueue(1)
        q.enqueue(4)
        self.assertEqual(4,q.findMax())
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(4,q.findMax())
        self.assertEqual(1,q.deque())
        self.assertEqual(4,q.deque())
        self.assertEqual(3,q.findMax())

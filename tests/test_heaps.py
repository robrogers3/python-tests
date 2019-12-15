import unittest

from heaps import MinHeap, MaxHeap

class TestHeaps(unittest.TestCase):
    def test_it_can_make_heaps(self):
        minHeap = MinHeap()
        self.assertIsInstance(minHeap, MinHeap)
        maxHeap = MaxHeap()
        self.assertIsInstance(maxHeap, MaxHeap)

    def test_min_heap_has_min_at_top(self):
        minHeap = MinHeap()
        minHeap.push(10)
        minHeap.push(1)
        self.assertEqual(minHeap.peek(), 1)

    def test_max_heap_has_max_at_top(self):
        maxHeap = MaxHeap()
        maxHeap.push(2)
        maxHeap.push(10)
        maxHeap.push(20)
        maxHeap.push(1)
        r = maxHeap.peek()
        self.assertEqual(20,maxHeap.peek())
        self.assertEqual(r, 20)

    def test_heaps_empty(self):
        maxHeap = MaxHeap()
        self.assertEqual(True, maxHeap.empty())

    def test_max_heap_max_is_retained(self):
        maxHeap = MaxHeap()
        maxHeap.push(7)
        maxHeap.push(4)
        maxHeap.push(10)
        maxHeap.push(6)
        maxHeap.push(5)

        self.assertEqual(10, maxHeap.peek())
        maxHeap.remove(10)
        self.assertEqual(7, maxHeap.peek())
        maxHeap.remove(6)
        self.assertEqual(7, maxHeap.peek())

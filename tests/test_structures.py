import unittest
from structures import MaxHeap, MinHeap, RunningMedian

class TestStructures(unittest.TestCase):
    def test_it_makes_a_max_heap(self):
        heap = MaxHeap(100)
        self.assertIsInstance(heap,MaxHeap)

    def test_it_max_heaps(self):
        heap = MaxHeap(100)
        self.assertEqual(heap.empty(), True)
        heap.push(10)
        heap.push(1)
        heap.push(20)
        heap.push(3)
        self.assertEqual(4, heap.length())
        maxV = heap.getMax()
        self.assertEqual(maxV, 20)
        maxV = heap.getMax()
        self.assertEqual(maxV, 20)
        heap.removeMax()
        self.assertEqual(3, heap.length())
        maxV = heap.getMax()
        self.assertEqual(maxV, 10)
        heap.push(5)
        heap.push(4)
        heap.push(7)
        maxV = heap.removeMax()
        self.assertEqual(maxV, 10)
        maxV = heap.getMax()
        self.assertEqual(maxV, 7)
        item = heap.remove(1)
        self.assertEqual(item,5)
        item = heap.removeMax()
        self.assertEqual(item, 7)


    def test_it_min_heaps(self):
        heap = MinHeap(10)
        self.assertEqual(heap.empty(), True)
        heap.push(4)
        heap.push(10)
        heap.push(1)
        heap.push(20)
        self.assertEqual(4, heap.length())
        minV = heap.getMin()
        self.assertEqual(minV, 1)
        self.assertEqual(minV, heap.peek())
        minV = heap.removeMin()
        self.assertEqual(3, heap.length())
        self.assertEqual(minV, 1)
        minV = heap.getMin()
        self.assertEqual(minV, 4)

    def test_running_median(self):
        # rmed = RunningMedian()
        # self.assertIsInstance(rmed, RunningMedian)
        # nums = [3,2,1,4,5]
        # rmed.insertMany(nums)
        # self.assertEqual(3, rmed.median())
        rmed = RunningMedian()
        nums = [5,6,3,7]
        med = rmed.insertMany(nums).median()

        #med = rmed.median()
        self.assertEqual(5.5, med)
        return
        rmed = RunningMedian()
        nums = [1,5,6,3,7,100]
        rmed.insertMany(nums)
        med = rmed.median()



if __name__ == '__main__':
    unittest.main()

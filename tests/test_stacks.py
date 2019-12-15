import unittest

from stacks import QueueStack
from stacks import DoubleListStack, StackWithMax


class TestStacks(unittest.TestCase):
    def test_stack_with_max(self):
        s = StackWithMax()
        s.push(3)
        s.push(1)
        max = s.max()
        self.assertEqual(max, 3)
        s.push(4)
        max = s.max()
        self.assertEqual(max, 4)
        el = s.pop()
        self.assertEqual(el, 4)
        max = s.max()
        self.assertEqual(max, 3)

    def test_queue_stack(self):
        s = QueueStack()
        s.enqueue(1)
        s.enqueue(2)
        el = s.dequeue()
        self.assertEqual(1, el)

    def test_queue_stack_raises_exception_on_empty(self):
        s = QueueStack()
        self.assertRaises(Exception, s.dequeue)

    def test_two_list_stacks(self):
        s = DoubleListStack(4)
        s.pushLeft(10)
        s.pushRight(20)
        r1 = s.popLeft()
        r2 = s.popRight()
        self.assertEqual(10, r1)
        self.assertEqual(20, r2)

    def test_two_list_stacks_raises_exception_on_full(self):
        s = DoubleListStack(2)
        s.pushLeft(10)
        self.assertRaises(Exception,s.pushRight)

    def test_two_list_stacks_raises_exception_on_empty(self):
        s = DoubleListStack(2)
        self.assertRaises(Exception,s.popRight)

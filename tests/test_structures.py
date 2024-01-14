import unittest
from structures import MaxHeap, MinHeap, RunningMedian
from structures import BinaryTree, TreeNode, LinkedList, Pointer

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


    def test_reconstruct_tree(self):
        preorder = [4,2,1,3,6,5,7]
        inorder =  [1,2,3,4,5,6,7]
        t = BinaryTree.reconstructTree(preorder,inorder)
        l = []
        x = lambda el: l.append(el.data)
        BinaryTree.preorderProcess(t, x)
        self.assertEqual(preorder,l)
        l = []
        BinaryTree.inorderProcess(t, x)
        self.assertEqual(inorder,l)
        l = []
        BinaryTree.postorderProcess(t,x)
        self.assertEqual([1, 3, 2, 5, 7, 6, 4], l)

    def test_tree_height(self):
        preorder = [4,2,1,3,6,5,7]
        inorder =  [1,2,3,4,5,6,7]
        root = BinaryTree.reconstructTree(preorder,inorder)
        tree = BinaryTree(root)
        h = tree.getHeight()
        self.assertEqual(2,h)
        h = BinaryTree.height(root)
        self.assertEqual(h,2)

    def test_get_paths(self):
        preorder = [4,2,1,3,6,5,7]
        inorder =  [1,2,3,4,5,6,7]
        t = BinaryTree.reconstructTree(preorder,inorder)
        tree = BinaryTree(t)
        paths = tree.getPaths()
        e = [[4, 2, 1], [4, 2, 3], [4, 6, 5], [4, 6, 7]]
        e = [[4, 2, 1], [4, 2, 3], [4, 6, 5], [4, 6, 7]]
        r = [[4, 2, 1], [4, 2, 3], [4, 6, 5], [4, 6, 7]]
        p = [[4, 2, 1], [4, 2, 3], [4, 6, 5], [4, 6, 7]]
        ps = []
        for path in paths:
            l = []
            for n in path:
                l.append(n.data)
            ps.append(l)

    def test_tree_height2(self):
        preorder = [4,2,1,3,6,5,7]
        inorder =  [1,2,3,4,5,6,7]
        root = BinaryTree.reconstructTree(preorder,inorder)
        h = BinaryTree.height(root)
        self.assertEqual(2,h)

    def test_tree_balanced(self):
        preorder = [4,2,1,3,6,5,7]
        inorder =  [1,2,3,4,5,6,7]
        root = BinaryTree.reconstructTree(preorder,inorder)
        t = BinaryTree(root)
        b = t.balanced()
        self.assertEqual(True, b)
        preorder = [4,2,1,3,6,5,7,8,9]
        inorder =  [1,2,3,4,5,6,7,8,9]
        root = BinaryTree.reconstructTree(preorder,inorder)
        t = BinaryTree(root)
        b = t.balanced()
        self.assertEqual(False, b)

    def test_tree_lca(self):
        preorder = [4,2,1,3,6,5,7]
        inorder =  [1,2,3,4,5,6,7]
        root = BinaryTree.reconstructTree(preorder,inorder)
        t = BinaryTree(root)
        lca = root.left
        a = root.left.left
        b = root.left.right
        c = root.right.right
        r = t.lca(a,b)
        self.assertEqual(lca,r)
        r = t.lca(a,lca)
        self.assertEqual(r,lca)
        r = t.lca(a,c)
        self.assertEqual(root, r)

    def test_linked_list(self):
        inorder =  [1,2,3,4,5,6,7]
        l = LinkedList(inorder)
        self.assertEqual(len(l), len(inorder))

        self.assertEqual(len(l), 8)

if __name__ == '__main__':
    unittest.main()

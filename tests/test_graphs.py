import unittest
from graphs import Graph, Node

def foo(val):
    def bar(node):
        return node.getData() == val

    return bar

class TestGraphs(unittest.TestCase):
    def setUp(self):
        n6 = Node(6)
        n5 = Node(5,[n6])
        n4 = Node(4, [n6])
        n3 = Node(3, [n4,n5])
        n2 = Node(2, [n4])
        n1 = Node(1, [n2,n3])
        self.g = Graph([n1,n2,n3,n4,n5,n6])

    def test_it_can_topo_sort_a_graph(self):
        n5 = Node(105)
        n3 = Node(103, [n5])
        n4 = Node(104)
        n2 = Node(102, [n3,n4,n5])
        n1 = Node(101, [n2,n4])
        g = Graph([n1,n2,n3,n4,n5])
        topoSorted = g.topo_sort()
        r = g.min_path(topoSorted)
        self.assertEqual(r,[1, 2, 3, 4, 5])

    def test_it_can_calculate_diameter(self):
        i = Node('i')
        h = Node('h', [i])
        g = Node('g')
        f = Node('f', [h,g])
        e = Node('e', [i])
        d = Node('d', [e])
        c = Node('c')
        b = Node('b', [c,f])
        a = Node('a', [b,d])
        g = Graph([a,b,c,d,e,f,g,h,i])
        r = g.diameter()
        print('dia',r)


    def test_it_can_print_level(self):
        return
        self.g.printLevels()

    def test_it_can_find_a_node(self):
        self.assertEqual(True, self.g.dfs(foo(5)))
        self.g.reset()
        self.assertEqual(True, self.g.dfs(foo(6)))

    def test_it_can_find_a_node_with_bfs(self):
        self.assertEqual(True, self.g.bfs(foo(5)))
        self.g.reset()
        self.assertEqual(True, self.g.bfs(foo(6)))

    def test_it_can_clone_a_graph(self):
        return
        nodes = self.g.getNodes()
        clone = self.g.clone()
        return
        for n in clone.getNeighbors():
            print(n)
        return
        self.assertEqual(True, clone.dfs(foo(5)))
        self.g.reset()
        self.assertEqual(True, self.g.dfs(foo(6)))

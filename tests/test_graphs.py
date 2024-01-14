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
        #print('dia',r)


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

    def test_it_can_detect_cycles(self):
        # r = self.g.hasCycle()
        # self.assertEqual(r,False)
        n5 = Node(105)
        n3 = Node(103, [n5])
        n4 = Node(104)
        n2 = Node(102, [n3,n4,n5])
        n1 = Node(101, [n2,n4])
        n4.addNeighbor(n1)
        g = Graph([n1,n2,n3,n4,n5])
        r = g.hasCycle()
        self.assertEqual(r, True)
        a = [1,2,3]

    def test_bipartite(self):
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        n1.addNeighbor(n4)
        n1.addNeighbor(n2)
        n2.addNeighbor(n1)
        n2.addNeighbor(n3)
        n3.addNeighbor(n2)
        n3.addNeighbor(n4)
        n4.addNeighbor(n1)
        n4.addNeighbor(n3)

        g = Graph([n1,n2,n3,n4])
        groups = g.bipartite()
        odds = groups[0]
        evens = groups[1]
        self.assertEqual(len(odds),len(evens))
        self.assertEqual(len(odds),2)
        self.assertEqual(odds[0], n4)
        n5 = Node(5)
        n5.addNeighbor(n1)
        n1.addNeighbor(n5)
        n4.addNeighbor(n5)
        n5.addNeighbor(n4)
        g.addNode(n5)
        #odd man
        groups = g.bipartite()
        self.assertEqual(groups,[])

    def test_it_can_group(self):
        def makeUsing(init):
            class using:
                def __init__(self, val):
                    self.val = val
                def next(self):
                    self.val += 1
                def val(self):
                    return self.val

            u = using(init)
            return u

        u = makeUsing(1)
        print(u.val)
        u.next()
        print(u.val)
        return
        groupings = self.g.groupConnectedNodes(1)
        # print(len(groupings))
        self.assertEqual(len(groupings[1]), len(self.g.getNodes()))
        self.assertEqual(len(groupings.keys()),1)
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        n4 = Node(4)
        n1.addNeighbor(n4)
        n4.addNeighbor(n1)
        g = Graph([n1,n2,n3,n4])
        groupings = g.groupConnectedNodes(1)
        self.assertEqual(list(groupings.keys()), [1,2,3])
        self.assertEqual(n1 in groupings[1], True)
        self.assertEqual(n3 in groupings[1], False)

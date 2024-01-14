import itertools
import queue
from graphs.Node import Node
from collections import defaultdict
class Graph:
    def __init__(self, nodes):
        self.nodes = nodes[:]

    def addNode(self, node):
        self.nodes.append(node)

    def getNodes(self):
        return self.nodes

    def __repr__(self):
        buffer = '{} ' * len(self.nodes)
        data =  [node.getData() for node in self.nodes]
        return buffer.format(*data)


    def __str__(self):
        buffer = '{} ' * len(self.nodes)
        data =  [node.getData() for node in self.nodes]
        return buffer.format(*data)

    def reset(self):
        [node.reset() for node in self.nodes]
        return self

    def len(self):
        return len(self.nodes)

    def topo_sort(self):
        stack = []
        for node in self.nodes:
            if node.getState() == 'unvisited':
                self.dfs_visit(node, stack)

        return stack

    def diameter(self):
        sorted_stack =  self.topo_sort()

        diameter = 0
        while sorted_stack:
            current = sorted_stack.pop()
            diameter = max(diameter, current.getLongestPath())
            for node in current.getNeighbors():
                if (current.getLongestPath() + 1) > node.getLongestPath():
                    node.setLongestPath(current.getLongestPath() + 1)
        return diameter

    def groupConnectedNodes(self, using):
        for node in self.nodes:
            if node.getState() == 'unvisited':
                self.dfsGroup(node, using)
                using += 1

        groupings = defaultdict(list)
        for node in self.nodes:
            groupings[node.getGrouping()].append(node)

        return groupings

    def dfsGroup(self, node, using):
        node.setState('visiting')
        node.setGrouping(using)
        for neighbor in node.getNeighbors():
            if neighbor.getState() == 'unvisited':
                self.dfsGroup(neighbor, using)

        node.setState('visited')
    def dfs_visit(self, node, stack):
        node.setState('visiting')
        for neighbor in node.getNeighbors():
            if neighbor.getState() == 'unvisited':
                self.dfs_visit(neighbor, stack)

        node.setState('visited')
        stack.append(node)

    def min_path(self, sorted_stack):
        sorted_stack.reverse()
        results = [-1] * len(sorted_stack)
        current = sorted_stack[0]
        results[0] = 1
        for i in range(1,len(results)):
            results[i] = max(results[i], results[i-1] + 1)
            for node in current.getNeighbors():
                results[i] = max(results[i], results[i - 1] + 1)

            current = sorted_stack[i]
            i += 1

        return results

    def clone(self):
        rootNode = self.nodes[0]
        hash_map = dict()
        rootCopy = Node(rootNode.getData())
        hash_map[rootNode] = rootCopy
        Graph.dfsClone(rootNode, hash_map)

        return rootCopy

    def dfsClone(root, hash_map):
        root.setState('visiting')

        for neighbor in root.getNeighbors():
            if neighbor not in hash_map:
                hash_map[neighbor] = Node(neighbor.getData())

            rootCopy = hash_map[root]
            neighborCopy = hash_map[neighbor]
            rootCopy.addNeighbor(neighborCopy)

            if neighbor.getState() == 'unvisited':
                Graph.dfsClone(neighbor,hash_map)
                neighbor.setState('visiting')

        root.setState('visited')

    def printLevels(self):
        currentLevel = queue.Queue()
        nextLevel = queue.Queue()
        root = self.nodes[0]

        currentLevel.put(root)
        root.setState('visiting')
        print("\nprint level", end="\n\n")
        while not currentLevel.empty():
            curr = currentLevel.get()
            print(curr)

            for node in curr.getNeighbors():
                if node.getState() == 'unvisited':
                    nextLevel.put(node)
                    node.setState('visiting')

            curr.setState('visited')

            if currentLevel.empty():
                print("+++++++")
                currentLevel = nextLevel
                nextLevel = queue.Queue()

    def bfs(self, func):
        for node in self.nodes:
            if node.getState() == 'unvisited' and self.bfsSearch(node, func):
                return True
            return False

    def bfsSearch(self, start, func):
        q = queue.Queue()
        q.put(start)
        start.setState('visiting')
        while q:
            curr = q.get()
            if func(curr):
                curr.setState('visited')
                return True

            for node in curr.getNeighbors():
                if node.getState() == 'unvisited':
                    q.put(node)
                    node.setState('visiting')

            curr.setState('visited')

        return False


    def dfs(self, func):
        for node in self.nodes:
            if node.getState() == 'unvisited' and self.dfsSearch(node, func):
                return True

        return False

    def dfsSearch(self, node, func):
        node.setState('visiting')
        if func(node):
            return True

        for neighbor in node.getNeighbors():
            if neighbor.getState() == 'unvisited' and self.dfsSearch(neighbor, func):
                return True

        node.setState('visited')
        return False

    def dfsHasCycle(self,node,func):
        node.setState('visiting')
        for neighbor in node.getNeighbors():
            if neighbor.getState() == 'unvisited' and self.dfsHasCycle(neighbor,func):
                return True
            elif neighbor.getState() == 'visiting':
                return True

        node.setState('visited')
        return False

    def hasCycle(self):
        def func(node):
            return node.getState() == 'visiting'
        for node in self.nodes:
            if node.getState() == 'unvisited' and self.dfsHasCycle(node, func):
                return True
        return False

    def bipartite(self):
        group1 = []
        group2 = []
        for node in self.nodes:
            node.setState('unvisited')
            node.setLevel(-1)

        for node in self.nodes:
            if node.getState() == 'unvisited':
                groups = self.getBipartiteGroups(node);
                if not groups:
                    return []

                group1.extend(groups[0])
                group2.extend(groups[1])

        return [group1,group2]

    def getBipartiteGroups(self,start):
        q = queue.Queue()
        odds =  []
        evens = []
        start.setLevel(0)
        start.setState('visiting')
        q.put(start)
        while not q.empty():
            curr = q.get()
            if curr.getLevel() % 2 == 0:
                evens.append(curr)
            else:
                odds.append(curr)

            for node in curr.getNeighbors():
                if node.getState() == 'unvisited':
                    node.setLevel(curr.getLevel() + 1)
                    q.put(node)
                    node.setState('visiting')
                elif node.getLevel() == curr.getLevel():
                    #same level so odd cycle found
                    return None

            curr.setState('visited')

        return [odds, evens]

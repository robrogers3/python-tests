class Node:
    def __init__(self, data, neighbors=[]):
        self.data = data
        self.neighbors = neighbors[:]
        self.state = 'unvisited'
        self.longest_path = 0
        self.level = -1
        self.grouping = None

    def __str__(self):
        buffer = '{} ' * len(self.neighbors)
        data = [n.getData() for n in self.neighbors]
        formatted = buffer.format(*data) or '[]'
        return f"data {self.data}. neighbors:[" + formatted + f"] state '{self.state}'"

    def __repr__(self):
        buffer = '{} ' * len(self.neighbors)
        data = [n.getData() for n in self.neighbors]
        formatted = buffer.format(*data)
        return f"data {self.data}. neighbors:[" + formatted + f"] state {self.state}"

    def setGrouping(self, grouping):
        self.grouping = grouping
        return self

    def getGrouping(self):
        return self.grouping

    def getLongestPath(self):
        return self.longest_path

    def setLongestPath(self, length):
        self.longest_path = length
        return self

    def setLevel(self,level):
        self.level = level
        return self

    def getLevel(self):
        return self.level

    def addNeighbor(self, node):
        self.neighbors.append(node)

    def getNeighbors(self):
        return self.neighbors

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setState(self,state):
        self.state = state
        return self

    def getState(self):
        return self.state

    def reset(self):
        self.state = 'unvisited'
        return self

class Node:
    def __init__(self, data, neighbors = []):
        self.data = data
        self.neighbors = neighbors
        self.state = 'unvisited'
        self.longest_path = 0

    def __str__(self):
        buffer = '{} ' * len(self.neighbors)
        data = [n.getData() for n in self.neighbors]
        formatted = buffer.format(*data)
        return f"data {self.data}. neighbors:" + formatted + f" state {self.state}"

    def getLongestPath(self):
        return self.longest_path

    def setLongestPath(self, length):
        self.longest_path = length
        return self

    def addNeighbor(self, node):
        self.neighbors.append(node)
        return self

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

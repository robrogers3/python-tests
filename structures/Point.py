import functools
@functools.total_ordering
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __lt__(self, other):
        return self.x, self.y < other.x, other.y
    def __eq__(self, other):
        return self.x, self.y == other.x, other.y

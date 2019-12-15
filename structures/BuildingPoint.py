import functools

@functools.total_ordering
class BuildingPoint:
    def __init__(self,height,location,isStart):
        self.height = height
        self.location = location
        self.isStart = isStart

    def __eq__(self, other):
        return self.location == other.location and self.height == other.height and self.isStart == other.isStart

    def __lt__(self,other):
        if self.location == other.location:
            return self.isStart

        return self.location < other.location

    def __repr__(self):
        return f'height {self.height} location {self.location} isStart {self.isStart}'

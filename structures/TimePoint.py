import functools

@functools.total_ordering
class TimePoint:
    def __init__(self, time, isStart):
        self.time = time
        self.isStart = isStart

    def __eq__(self, other):
        return self.time == other.time and self.isStart == other.isStart

    def __lt__(self,other):
        if self.time == other.time:
            return self.isStart
        return self.time < other.time

    def __str__(self):
        return 'time: {} is Start {}'.format(self.time, self.isStart)

    def __repr__(self):
        return 'time: {} is Start {}'.format(self.time, self.isStart)

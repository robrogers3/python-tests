class TimeScheduler:
    def __init__(self, timepoints = []):
        self.timePoints = timepoints
        self.timePoints.sort()

    def hasOverlap(self):
        count = 0
        for p in self.timePoints:
            count += 1 if p.isStart else -1
            if count > 1:
                return True

        return False

    def collapseSchedule(self):
        schedule = []
        startpoint = None
        numIntervals = 0
        for point in self.timePoints:
            if point.isStart:
                numIntervals += 1
                if numIntervals == 1:
                    startpoint = point
            else:
                numIntervals -= 1
                if numIntervals == 0:
                    schedule.append((startpoint.time, point.time))

        return schedule


    @staticmethod
    def overlapping(points):
        events = [(p[0], True) for p in points]
        events += [(p[1], False) for p in points]
        events.sort()
        count = 0
        for event in events:
            count += 1 if event[1] else -1
            if count > 1:
                return True


        return False

    def scheduleCollapse(points):
        events = [(p[0], True) for p in points]
        events += [(p[1], False) for p in points]
        events.sort()
        startPoint = None
        numIntervals = 0
        schedule = []
        for event in events:
            if event[1]:
                numIntervals += 1
                if numIntervals == 1:
                    startPoint = event[0]
            else:
                numIntervals -= 1
                if numIntervals == 0:
                    schedule.append((startPoint, event[0]))

        return schedule

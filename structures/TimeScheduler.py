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
    def maxNumberOfOverlappingEvents(timePeriods):
        # True means event start
        events = [(p[0], True) for p in timePeriods]
        # False means event end
        events += [(p[1], False) for p in timePeriods]

        # sort them to be sure events are in order
        events.sort()
        numIntervals = 0
        # if you are just interested numIntervals then this isn’t needed, and replace overlapping with numIntervals in call to max
        overlapping = 0
        # max number of overlapping events
        mymax = 0
        for event in events:
            # event start, increase numintervals, record max
            if event[1]:
                numIntervals += 1
                mymax = max(mymax,numIntervals)
            # an event end, decrease number of intervals
            else:
                numIntervals -= 1

        return mymax

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

    @staticmethod
    def scheduleCollapse(points):
        events =  [(p[0],True) for p in points]
        events += [(p[1],False) for p in points]
        events.sort()
        schedule = []
        numOpenIntervals = 0
        startEvent = None
        for event in events:
            if event[1]:
                numOpenIntervals += 1
                if numOpenIntervals == 1:
                    startEvent = event[0]
            else:
                numOpenIntervals -= 1
                if numOpenIntervals == 0:
                    schedule.append((startEvent, event[0]))

        return schedule


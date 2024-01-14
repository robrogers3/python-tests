import unittest
from operator import itemgetter
from structures import BuildingPoint, BuildingMap, TimePoint, TimeScheduler, Skyline
import heapq
def getSkyline(buildings):
        # add start-building events
        # also add end-building events(acts as buildings with 0 height)
        # and sort the events in left -> right order
        events = [(L, -H, R) for L, R, H in buildings]
        #events += list({(R, 0, 0) for _, R, _ in buildings})
        events += [(R, 0, 0) for _, R, _ in buildings]
        events.sort()

        # res: result, [x, height]
        # live: heap, [-height, ending position]
        res = [(0, 0)]
        live = [(0, float("inf"))]
        for pos, negH, R in events:
            # 1, pop buildings that are already ended
            # 2, if it's the start-building event, make the building alive
            # 3, if previous keypoint height != current highest height, edit the result
            while live[0][1] <= pos:
                heapq.heappop(live)
            if negH: heapq.heappush(live, (negH, R))
            if res[-1][1] != -live[0][0]:
                res += [ (pos, -live[0][0]) ]
        return res[1:]

class TestLineSweep(unittest.TestCase):
    def test_time_points(self):
        p1 = TimePoint(1, True)
        p2 = TimePoint(2, False)
        p3 = TimePoint(3, True)
        p4 = TimePoint(5, False)
        p5 = TimePoint(4, True)
        p6 = TimePoint(6, False)

        l = [p3,p2,p4,p1,p5,p6]
        l.sort()

    def test_time_schedule_has_overlaps(self):
        p1 = TimePoint(1, True)
        p2 = TimePoint(2, False)
        p3 = TimePoint(3, True)
        p4 = TimePoint(5, False)
        p5 = TimePoint(4, True)
        p6 = TimePoint(6, False)

        l = [p3,p2,p4,p1,p5,p6]
        ts = TimeScheduler(l[:])
        r = ts.hasOverlap()
        self.assertEqual(True, r)

        ts = TimeScheduler([p1,p2,p5,p6])
        r = ts.hasOverlap()
        self.assertEqual(False, r)

    def test_collapse_time_schedule(self):
        p1 = TimePoint(1, True)
        p2 = TimePoint(3, False)
        p3 = TimePoint(3, True)
        p4 = TimePoint(5, False)
        p5 = TimePoint(6, True)
        p6 = TimePoint(8, False)
        p7 = TimePoint(7, True)
        p8 = TimePoint(9, False)
        l = [p8,p2,p1,p3,p7,p5,p6,p4]
        ts = TimeScheduler(l[:])
        r = ts.collapseSchedule()
        self.assertEqual(r, [(1, 5), (6, 9)])

    def test_building_ports_sort(self):
        bp1 = BuildingPoint(1,1, True)
        bp2 = BuildingPoint(1,3, False)
        bp3 = BuildingPoint(2,2, True)
        bp4 = BuildingPoint(2,4, False)

        bl = [bp4,bp3,bp2,bp1]

        bl.sort()
        self.assertEqual(bl[0], bp1)

    def test_a_building_map_is_one(self):
        bmap = BuildingMap()
        self.assertIsInstance(bmap, BuildingMap)

    def test_you_can_use_a_building_map(self):
        bmap = BuildingMap()
        bmap.put(10)
        bmap.put(12)
        bmap.put(3)

        self.assertEqual(12, bmap.getMax())

        bmap.remove(12)

        self.assertEqual(10, bmap.getMax())

    def test_skyline(self):
        buildings = [
            {'height': 4, 'start': 1, 'end': 5},
            {'height': 2, 'start': 3, 'end': 7},
            {'height': 2, 'start': 5, 'end': 8},
            {'height': 6, 'start': 9, 'end': 15},
            {'height': 8, 'start': 9, 'end': 13},
        ]
        skyline = Skyline(buildings)

        r = skyline.draw()

        points = [[2, 9, 10],[3, 7, 15], [5, 12,12], [11,14,100], [15, 20, 10], [19, 24, 8]]
        buildings = []
        for p in points:
            buildings.append({'height': p[2], 'start':p[0], 'end':p[1]})

        skyline = Skyline(buildings)
        r = skyline.draw()
        e = [(2, 10), (3, 15), (7, 12), (11, 100), (14, 0), (15, 10), (20, 8), (24, 0)]
        self.assertEqual(r,e)

    def test_def_skyline(self):
        points = [[2, 9, 10],[3, 7, 15], [5, 12,12], [11,14,100], [15, 20, 10], [19, 24, 8]]
        e = [(2, 10), (3, 15), (7, 12), (11, 100), (14, 0), (15, 10), (20, 8), (24, 0)]
        r = getSkyline(points)
        self.assertEqual(r,e)

    def test_time_points_collapse(self):
        points = [[10,13],[0,3],[2,5],[6,7]]
        r = TimeScheduler.scheduleCollapse(points)
        e = [(0, 5), (6, 7), (10, 13)]
        self.assertEqual(r,e)

    def test_time_points_overlapping(self):
        points = [[10,13],[0,3],[2,5],[6,7]]
        r = TimeScheduler.overlapping(points)
        self.assertEqual(r, True)
        return
        events = [(p[0], True) for p in points]
        events += [(p[1], False) for p in points]
        events.sort(key=itemgetter(0,1))
        print(events)


    def test_num_overlapping(self):
        pointsInTime = [[10,13],[0,3],[1,4],[2,5],[6,7],[7,9],[8,10],[9,11]]
        pointsInTime = [[6,7],[7,9],[8,10],[9,11],[10,13],[11,12]]
        results = TimeScheduler.maxNumberOfOverlappingEvents(pointsInTime)
        self.assertEqual(results,2)

    def test_skyline_foo(self):
        points = [[2, 9, 10],[3, 7, 15], [5, 12,12], [11,14,100], [15, 20, 10], [19, 24, 8]]
        e = [(2, 10), (3, 15), (7, 12), (11, 100), (14, 0), (15, 10), (20, 8), (24, 0)]
        print()
        r = Skyline.skylineFromPoints(points)
        self.assertEqual(r,e)

    def test_skyline_zed(self):
        points = [[2, 9, 10],[3, 7, 15], [5, 12,12], [11,14,100], [15, 20, 10], [19, 24, 8]]
        e = [(2, 10), (3, 15), (7, 12), (11, 100), (14, 0), (15, 10), (20, 8), (24, 0)]
        print()
        r = Skyline.pointsToSkyline(points)
        self.assertEqual(r,e)

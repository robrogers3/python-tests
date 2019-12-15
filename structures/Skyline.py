from structures.BuildingPoint import BuildingPoint
#from structures.BuildingMap import BuildingMap
import heapq
from collections import defaultdict

class BuildingMap:
    def __init__(self):
        self.map = defaultdict(list)
        self.heap = []
        heapq.heapify(self.heap)

    def put(self, height):
        heapq.heappush(self.heap, -height)
        self.map[height].append(height)

    def remove(self, height):
        if height not in self.map:
            print('height not in map')
            return

        n = self.map[height].pop()

        self.heap.remove(-n)

        heapq.heapify(self.heap)

        if len(self.map[height]) == 0:
            self.map.pop(height)


    def getMax(self):
        if len(self.heap) == 0:
            return 0

        return -self.heap[0]
class Skyline:
    def __init__(self, buildings):
        self.buildingPoints = []
        self.map = BuildingMap()
        for building in buildings:
            self.buildingPoints.append(BuildingPoint(building['height'], building['start'], True))
            self.buildingPoints.append(BuildingPoint(building['height'], building['end'], False))
        self.buildingPoints.sort()

    def draw(self):
        currentMaxHeight = 0
        currentStartX = 0
        results = []
        for building in self.buildingPoints:
            if building.isStart:
                self.map.put(building.height)
                if building.height > currentMaxHeight:
                    self.drawHorizontal(currentStartX, building.location,currentMaxHeight)
                    results.append(self.drawVertical(building.location, currentMaxHeight, building.height))
                    currentMaxHeight = building.height
                    currentStartX = building.location
            else:
                self.map.remove(building.height)
                if building.height == currentMaxHeight:
                    self.drawHorizontal(currentStartX, building.location, building.height)
                    oldMax = currentMaxHeight
                    currentMaxHeight = self.map.getMax()
                    currentStartX = building.location
                    results.append(self.drawVertical(building.location, oldMax, currentMaxHeight))
        return results

    def drawHorizontal(self, x1, x2, y, debug=False):
        if debug:
            print(f'draw horizontal from location {x1} to  {x2} at height {y}')
        return ('horz',x1,x2,y)

    def drawVertical(self, x, y1, y2, debug=False):
        if debug:
            print(f'draw vertical   at   location {x} from {y1} to {y2}')
        return (x,y2)

    @staticmethod
    def skylineFromPoints(points):
        events = [(L,-H,R) for L,R,H in points]
        events+= [(R,0,0) for _, R,_ in points]
        events.sort()

        #res: result, [x,height]
        #live: heap, [-height, ending position]
        res = [(0,0)]
        live = [(0, float("inf"))]
        for pos, negH, R, in events:
            # pop buildings that have already ended
            while live[0][1] <= pos: heapq.heappop(live)

            # if it's start of building, add it to live
            if negH: heapq.heappush(live, (negH, R))

            # if previous keypoint height != current highest height, edit result

            if res[-1][1] != -live[0][0]:
                res += [(pos, -live[0][0])]
        return res[1:]

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        distances = []

        heapq.heapify(distances)

        for i, point in enumerate(points):

            dist = pow((pow(point[0], 2) + pow(point[1], 2)), .5)
            heapq.heappush(distances, (-dist, i))

            if len(distances) > k:
                heapq.heappop(distances)

        return [points[dist[1]] for dist in distances]

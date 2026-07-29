class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        distance = []

        for i in range(len(points)):
            x1, y1 = 0, 0 # origin
            x2, y2 = points[i][0], points[i][1]

            d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2) # euclidian distance
            distance.append([d, i])

        heapq.heapify(distance)

        res = []
        for _ in range(k):
            d, i = heapq.heappop(distance)
            res.append(points[i])
        return res

        # Time complexity: O(n + k*log n)
        # Space complexity: O(n + k)


        

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = stones
        heapq.heapify_max(maxHeap)

        while len(maxHeap) > 1:
            y = heapq.heappop_max(maxHeap)
            x = heapq.heappop_max(maxHeap)

            if x < y:
                heapq.heappush_max(maxHeap, y - x)

        return maxHeap[0] if maxHeap else 0
                
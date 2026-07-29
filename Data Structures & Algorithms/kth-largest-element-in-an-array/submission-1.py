class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = nums
        heapq.heapify_max(nums)

        maxElement = None
        for _ in range(k):
            maxElement = heapq.heappop_max(maxHeap)
        
        return maxElement
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        for x in nums:
            count[x] = count.get(x, 0) + 1

        # Create a heap of (-frequency, number), aka a max heap
        heap = [(-freq, num) for num, freq in count.items()]
        heapq.heapify(heap)

        # Extract top k elements
        result = []
        for _ in range(k):
            freq, num = heapq.heappop(heap)
            result.append(num)

        return result
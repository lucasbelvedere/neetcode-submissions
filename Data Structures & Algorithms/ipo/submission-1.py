class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        class Node:
            def __init__(self, idx):
                self.idx = idx

            def __lt__(self, other): # Operator overload required for heap; using rich comparison methods
                if capital[self.idx] != capital[other.idx]:
                    return capital[self.idx] < capital[other.idx]
                return self.idx < other.idx

        minCapital = []
        maxProfit = []
        for i in range(len(capital)):
            heapq.heappush(minCapital, Node(i))
        
        for _ in range(k):
            while minCapital and capital[minCapital[0].idx] <= w:
                idx = heapq.heappop(minCapital).idx
                heapq.heappush_max(maxProfit, profits[idx])

            if not maxProfit:
                break
            w += heapq.heappop_max(maxProfit)

        return w

# time complexity: O(n*log(n))
# space complexity: O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal, maxProfit = float("inf"), 0
        for i in range(len(prices)):
            maxProfit = max(maxProfit, prices[i] - minVal)
            minVal = min(minVal, prices[i])
        return maxProfit
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxValue = max(piles) # max value of the piles
        left, right = 1, maxValue
        res = right

        while left <= right: 
            k = (left + right) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h: # for this binary search, remember that if we find a solution k where hours equals to h, we must keep looking for other possible solutions
                res = min(res, k)
                right = k - 1
            else:
                left = k + 1


        return res

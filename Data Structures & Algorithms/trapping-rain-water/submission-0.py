class Solution:
    def trap(self, height: List[int]) -> int:
        # if a matrix was given to us rather than a list, then a prefix sum approach
        # could be used, and subset of the array could give us the answer 
        # (Subset B (INDEX) - Subset A (INDEX) - 1 - NumBarsBetweenBandA)

        lenHeight = len(height)
        if lenHeight <= 2:
            return 0

        maxLeft = [0] * lenHeight
        maxRight = [0] * lenHeight
        minHeight = [0] * lenHeight

        # populate maxLeft with preSum
        for i in range(lenHeight):
            maxLeft[i] = max(maxLeft[i - 1], height[i - 1]) if i != 0 else 0

        # populate minLeft with postSum
        for i in range(lenHeight - 1, -1, -1):
            maxRight[i] = max(maxRight[i + 1], height[i + 1]) if i < lenHeight - 1 else 0

        # populate minHeight
        for i in range(lenHeight):
            minHeight[i] = min(maxLeft[i], maxRight[i])

        print(minHeight)
        areaOfWater = 0
        for i in range(1, lenHeight - 1): # jump left and right corner, since there is no way to have bars both sides
            areaOfWater += (minHeight[i] - height[i]) if height[i] < minHeight[i] else 0
        return areaOfWater

        

        
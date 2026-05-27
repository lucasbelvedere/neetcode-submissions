class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointers approach
        left, right, vol = 0, len(heights) - 1, 0
        
        while left < right:
            volume = (right - left) * min(heights[left], heights[right])
            vol = volume if volume > vol else vol # set vol to greater value
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
                right -= 1

        return vol
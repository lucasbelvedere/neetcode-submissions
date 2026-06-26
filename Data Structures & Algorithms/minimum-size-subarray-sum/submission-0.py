class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen, left, sum = float("inf"), 0, 0
        for right in range(len(nums)):
            sum += nums[right]
            while sum >= target:
                minLen = min(minLen, right - left + 1)
                sum -= nums[left]
                left += 1

        return 0 if minLen == float("inf") else minLen
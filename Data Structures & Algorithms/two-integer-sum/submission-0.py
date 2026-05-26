class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}
        for i in range(len(nums)):
            tmp = target - nums[i]
            if tmp in indexes:
                return [indexes[tmp],i]
            indexes[nums[i]] = i
        return []
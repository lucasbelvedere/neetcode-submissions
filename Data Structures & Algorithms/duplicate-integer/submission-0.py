class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_values = set()
        for i in range(len(nums)):
            if nums[i] in unique_values:
                return True
            else:
                unique_values.add(nums[i])
        return False
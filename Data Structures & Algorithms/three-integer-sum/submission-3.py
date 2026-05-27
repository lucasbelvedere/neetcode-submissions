class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, val in enumerate(nums):
            if val > 0: # why? for 3 values to sum and be equal to 0, there must be a negative value, so val must be negative or 0
                break
            if i > 0 and val == nums[i - 1]:
                continue
            
            left = i + 1 # left pointer
            right = len(nums) - 1 # right pointer
            
            while left < right:
                _3sum = val + nums[left] + nums[right]
                if _3sum > 0:
                    right -= 1
                elif _3sum < 0:
                    left += 1
                else:
                    res.append([val, nums[left], nums[right]])
                    # if 3sum = 0, you move both pointers inwards
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return res
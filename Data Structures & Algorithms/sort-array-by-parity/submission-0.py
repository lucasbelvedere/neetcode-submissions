'''
Input: an integer array nums that we need to sort based on parity

Approach: two pointers, one pointing to the beginning of the array,
another one pointing to the end. Whenever swapping is necessary, we
do so.

PLAN:
- left, right = 0, len(nums) - 1
- while left < right:
    - if nums sub left is odd:
        - swap nums sub i with nums sub j
        - decrement right
    - else increment left
- return the list

'''

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] % 2 != 0:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1

        return nums
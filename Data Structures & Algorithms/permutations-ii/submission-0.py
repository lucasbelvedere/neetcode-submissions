'''
Input: an array nums of integers, may contain duplicates
Output: all possible permutations (a list of lists)

Approach: A decision tree. Similar to permutations I, but we will have to sort nums, and 
At each level of the tree, we add a new element. For every list from the level above, we make a copy and insert the new element in every possible position (n + 1 positions for a list of size n).
                        [ ]
                         |
                        [1]
                      /    X
                    [1,1]  [1,1]
                /    |    \
         [2,1,1] [1,2,1] [1,1,2]...
* As you can tell from the decision tree, we will have n levels and n! leaves at the bottom level, and each leaf is a list of size n.
* We can do it either iteratively or recursively. Recursively, we get the permutations of nums[1:] first and then insert nums[0] into each of them, so the tree is built from the end of the array.
* The extra step we will have to take compared to permutations I is to sort nums

PLAN:
- if len(nums) is 0:
    - return [[]]
- perms = self.permute(nums[1:])
- res = []
- for every perm in perms:
    - for i in range(len(perm) + 1):
        - create a copy of perm
        - insert nums[0] at position i in the copy
        - append the copy to res
- return res

# Time complexity: O(n * n!). We end up with n! permutations, and each one costs O(n) to copy and insert into. The levels above the last one are much smaller, so the last level dominates.
# Space complexity: O(n * n!), because the output holds n! lists of size n. Not counting the output, the recursion stack only goes n levels deep, so that part is O(n).
'''

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not len(nums):
            return [[]]

        perms = self.permuteUnique(nums[1:])
        res = []

        for perm in perms:
            for i in range(len(perm) + 1):
                perm_copy = perm.copy()
                perm_copy.insert(i, nums[0])
                res.append(perm_copy)
                if i < len(perm) and perm[i] == nums[0]:
                    break

        return res
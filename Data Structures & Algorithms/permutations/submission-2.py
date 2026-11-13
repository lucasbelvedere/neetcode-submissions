'''
Input: an array nums of unique integers
Output: all possible permutations (a list of lists)

Approach: A decision tree. It's not exactly backtracking, but it's similar to questions like 'combinations'.
At each level of the tree, we add a new element. For every list from the level above, we make a copy and insert the new element in every possible position (n + 1 positions for a list of size n).
                        [ ]
                         |
                        [1]
                      /    \
                    [1,2]  [2,1]
                /    |    \
         [3,1,2] [1,3,2] [1,2,3]...
* As you can tell from the decision tree, we will have n levels and n! leaves at the bottom level, and each leaf is a list of size n.
* We can do it either iteratively or recursively. Recursively, we get the permutations of nums[1:] first and then insert nums[0] into each of them, so the tree is built from the end of the array.

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
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not len(nums):
            return [[]]

        perms = self.permute(nums[1:])
        res = []

        for perm in perms:
            for i in range(len(perm) + 1):
                perm_copy = perm.copy()
                perm_copy.insert(i, nums[0])
                res.append(perm_copy)

        return res

'''
why is the output size n! and not 2^n, and how is this different from subsets or combinations?

*Because in permutations the position of each element counts, so [1,2] and [2,1] are two different answers. For the first position, we have n choices, then for the second one we have n - 1, since one element is already used, and so on until we reach 1 for the last position, so we end up with n times n - 1 all the way down to 1, which is n!. In subsets, the order does not matter, so [1,2] and [2,1] are the same thing. For each element, we just decide whether it is in or out, so that is 2 choices for every element, which gives us 2^n. Combinations are basically subsets of a fixed size k, so there are C(n, k) of them, and if we add those up for every k from 0 to n, we get 2^n again.
'''
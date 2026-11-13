'''
Input: an array nums of unique integers
Output: all possible permutations (list of lists)

Approach: A decision tree, not exactly backtracking but similar to questions like 'combinations'
For each level of the tree, we add a new elements, but at the same time we make a copy of the list, and try to insert the element in every possible place of the list (O(n))
                        [ ]
                         |
                        [1]
                      /    \
                    [1,2]  [2,1]
                /    |    \
         [3,1,2] [1,3,2] [1,2,3]...
* As you can tell from the decision tree, we will have about n levels and n! branches in the leaf level of the tree, leaving us with a O(n*n!). In addition, an O(n) extra space will be required.
* We can either do it iteratively or recursively

PLAN:
- if len(nums) is 0:
    - return [[]]
- perms = self.permute(nums[1:])
- res = []
- for every list in perms
    - for i in range(len(p) + 1):
        - create copy of list
        - insert nums sub 0 to position i in the copy
        - append to res
- return res

# Time complexity: O(n^2*n!), we end up having n^2 instead of n, as mentioned earlier, because of the fact that for each copy and insertion in the list, there is an extra O(n)
# Space complexity: O(n*n!), just look at the last branch of the decision tree times the height of the tree
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
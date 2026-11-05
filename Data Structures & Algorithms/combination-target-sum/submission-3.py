'''
Input: an array of distinct positive nums and a target integer
Output: a list of all unique combinations (lists) of nums whose sum equals the target, where the same number can be used an unlimited number of times

* A combination is != a permutation (the order of the numbers in a combination doesn't matter)

Approach: backtracking, think about a decision tree where, for every number in nums, we either go left and include nums[i] while staying at the same index (so we can reuse it), or go right and skip nums[i] by moving to index + 1 (so a recursive solution). We keep a running total so we don't have to sum the temp list every call.

PLAN:
- declare and initialize res equals to an empty list
- declare and initialize a dfs function (helper) that will take an index, a temp list, and the running total
    - Base case: if total equals to the target, then we add a copy of temp to res and return.
    - Base case: if index is out of bounds, or total is greater than the target, we return.
    - temp.append(nums[index])
    - call dfs with the index we are currently in, temp, and total + nums[index]
    - pop from temp to try the decision tree without the current number
    - call dfs with index + 1, temp, and total
- call dfs with index 0, an empty list, and a total of 0
- return res
'''

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index: int, temp: List[int], total: int):
            if total == target:
                res.append(temp.copy())
                return

            if index >= len(nums) or total > target:
                return

            temp.append(nums[index])
            dfs(index, temp, total + nums[index])
            temp.pop()
            dfs(index + 1, temp, total)
               

        dfs(0, [], 0)
        return res

'''
Time complexity for recursive solution: O(2^(t/m))
    - We have a factor of 2 since we call dfs recursively twice (one with index and one with index + 1)
    - t stands for the target value
    - m is the minimum value in nums
    - t/m is the max depth of the tree, since the longest path keeps adding the smallest number until it reaches the target
Space complexity: O(t/m)
    - the recursion stack and temp are at most t/m deep (not counting res)
'''

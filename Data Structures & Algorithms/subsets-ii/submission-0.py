'''
Input: An array of integers that can contain duplicates
Output: An array with all the subsets, without any duplicates

Approach: Similar to Subsets I, we will backtrack as follows:
            [  ]
         /         \
      [1]           []
    /    \         /  \
[1, 2]    [1]    [2]   []

The decision tree above shows an example where nums is [1, 2].
At every level of the decision tree, we recursively call the function twice: once to go to the left branch and include the current number, and once to go right and not include it (as the tree shows).
* In this case, we have to sort the array first. Then, before going to the second branch at every level of the decision tree, we keep moving i forward until nums[i + 1] is different from nums[i], so we skip the duplicates.

PLAN:
- Declare and initialize an empty subsets list, as well as a temp list
- Sort nums
- Declare a helper function that takes the index
    - if i >= len(nums):
        - subsets.append(temp.copy())
        - return
    - temp.append(nums[i])
    - helper(i + 1)
    - temp.pop(), which is where the backtracking happens
    - while i + 1 < len(nums) and nums[i] == nums[i + 1]:
        - i += 1
    - helper(i + 1)
- helper(0)
- return subsets

Time complexity: O(n * 2^n)
Space complexity: O(n * 2^n)

Explanation:
    Why the n? Because of the line where we copy (temp.copy()).
    Why the 2? Because at every level we make one decision that splits into two branches.
    Why the power of n? Because we have n nums, so there are n levels of decisions (n + 1 levels counting the leaves), and each one doubles the number of branches.
'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets, temp = [], []
        nums.sort()

        def backtracking_dfs(i):
            if i >= len(nums):
                subsets.append(temp.copy())
                return

            temp.append(nums[i])
            backtracking_dfs(i + 1)
            temp.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtracking_dfs(i + 1)

        backtracking_dfs(0)
        return subsets

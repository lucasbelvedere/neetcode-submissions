'''
Input: An array nums of unique integers
Output: An array with all subsets of nums, without duplicates

Approach: Backtracking. Think of it this way:
            [  ]
         /         \
      [1]           []
    /    \         /  \
[1, 2]    [1]    [2]   []

The decision tree above shows an example where nums is [1, 2].
At every level of the decision tree, we recursively call the function twice: once to go to the left branch and include the current number, and once to go right and not include it (as the tree shows).

PLAN:
- Declare and initialize an empty subsets list, as well as a temp list
- Declare a helper function that takes the index
    - if i >= len(nums):
        - subsets.append(temp.copy())
        - return
    - temp.append(nums[i])
    - helper(i + 1)
    - temp.pop(), which is where the backtracking happens
    - helper(i + 1)
- helper(0)
- return subsets

Time complexity: Look at the decision tree, every level we make one decision. In addition, add to the subsets a copy of temp. That is O(n*2^n)
Space complexity: O(n*2^n)
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets, temp = [], []

        def backtracking_dfs(index):
            if index >= len(nums):
                subsets.append(temp.copy())
                return
            
            temp.append(nums[index])
            backtracking_dfs(index + 1)
            temp.pop()
            backtracking_dfs(index + 1)

        backtracking_dfs(0)
        return subsets

        
        
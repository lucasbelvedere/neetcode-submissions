'''
Input: An array nums of unique integers
Output: An array with all subsets of nums without duplicates

Approach: Backtracking; think of it the following way:
            [  ]
         /         \
      [1]           []
    /    \         /  \
[1, 2]    [1]    [2]   []

the decision tree above shows an example where nums has [1,2].
For every level of the decision tree, we decide recursively call the function to go to the left branch and include the current number, or call right and not include it (as the tree shows)

PLAN:
- Declare and initialize an empty subsets list, as well as a temp list
- Declare a helper function that takes the index
    - if i >= len(nums):
        - subsets.append(temp.copy())
        - return
    - temp.append(nums[i])
    - helper(i + 1)
    - temp.pop() which is where our backtracking is
    - helper(i + 1)
- helper(0)
- return subsets
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

        
        
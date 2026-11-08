'''
Input: two integers n and k
Output: all possible combinations of k numbers chosen from the range [1, n]

Approach: backtracking, decision tree, similar to subsets, but one that we can stop once the size of the temp list > k
            [  ]              n = 3, k = 2 example
         /         \
      [1]           []
    /    \         /  \
[1, 2]    [1]    [2]   []
 /
[1, 2, 3] (pop, since k is 2)

At every level of the decision tree, we recursively call the function twice: once to go to the left branch and include the current number, and once to go right and not include it (as the tree shows).
* In this case, once the size of the temp list is greater than k, we return and pop a number from temp (backtrack)

PLAN:
- Declare and initialize an empty subsets list, as well as a temp list
- Declare a helper function that takes num
    - if num > n:
        - if len(temp) == k:
            - subsets.append(temp.copy())
        - return
    - temp.append(num)
    - helper(num + 1)
    - temp.pop(), which is where the backtracking happens
    - helper(num + 1)
- helper(1)
- return subsets

Time complexity: O(k * 2^n)
Space complexity: O(k * 2^n)
'''

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        subsets, temp = [], []

        def backtrack_dfs(num):
            if num > n:
                if len(temp) == k:
                    subsets.append(temp.copy())
                return
            temp.append(num)
            backtrack_dfs(num + 1)
            temp.pop()
            backtrack_dfs(num + 1)

        backtrack_dfs(1)
        return subsets
        
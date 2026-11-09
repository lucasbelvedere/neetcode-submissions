'''
Input: an array of integers candidates (may contain duplicates) as well as a target integer
Output: a list of all unique combinations of candidates where the chosen numbers sum to target (list of lists)

Approach: backtracking, decision tree, where for every level of this decision tree, there are 2 branches, one that you choose to use the current num from candidates, one that you don't

            [  ]
         /         \
      [1]           []
    /    \         /  \
[1, 2]    [1]    [2]   []

* One extra step we will take for this question is to sort candidates and then, when backtracking to follow the second branch in the decision tree, loop until we get a value different than the current index. We are doing that since candidates have duplicates, and this extra step costs us O(nlog(n)).

PLAN:
- Declare and initialize a combinations and temp lists
- Declare and initialize a backtrack_dfs that takes an index as a parameter and a total
- sort candidates
    - if index >= len(candidates) or total > target:
        - return
    - if total == target:
        - combinations.append(temp.copy()), takes O(n)
    - temp.append(candidates[i])
    - backtrack_dfs(index, total + candidates[i])
    - temp.pop()
    - while index + 1 < len(candidates) and index == index + 1:
        - index += 1
    - backtrack_dfs(index + 1, total)
- backtrack_dfs(0, 0)
- return combinations

Time complexity: O(n*2^n)
Space complexity: O(n*2^n) taking into consideration the output list.
'''

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations, temp = [], []
        candidates.sort()

        def backtrack_dfs(i, total):
            if total == target:
                combinations.append(temp.copy())
                return
            if i >= len(candidates) or total > target:
                return

            temp.append(candidates[i])
            backtrack_dfs(i + 1, total + candidates[i])
            temp.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack_dfs(i + 1, total)

        backtrack_dfs(0, 0)
        return combinations

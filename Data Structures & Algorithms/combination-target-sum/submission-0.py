'''
Input: an array of distinc integers + an integer target.
Return: list of all unique combinations of nums where the chosen numbers sum to target.

- Same number may be chosen from nums an unlimited number of times.
- Two combinations are the same if the frequency of each of the chosen numbers is the same


'''

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                cur.append(nums[j])
                dfs(j, cur, total + nums[j])
                cur.pop()

        dfs(0, [], 0)
        return res
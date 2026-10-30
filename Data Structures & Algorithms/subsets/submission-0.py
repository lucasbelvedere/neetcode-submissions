'''
Input is an array of ints, output is all possible subsets of nums

Approach: we could use backtracking or brute force. In my opinion, for this
question, iteratively finding all possibilities is easier than thinking about
backtracking.

PLAN:
- Declare and initialize res equal to a list with an empty list in it
- for num in nums:
    - res += [subset + [num] for subset in res]
- return res


'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            res += [subset + [num] for subset in res]

        return res

        

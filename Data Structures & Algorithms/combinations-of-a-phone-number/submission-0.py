'''
Input: a string digits made up of digits from 2 to 9
Output: all possible letter combinations that digits could represent

Approach: backtracking, decision tree. Rather than 2 branchs, we could have 4, since the number 9 can be represented by 4 characters.

                          [ "" ]                       # i=0, digit '2'
             /              |              \
         ["a"]            ["b"]            ["c"]       # i=1, digit '3'
        /  |  \          /  |  \          /  |  \
   ["ad"]["ae"]["af"]["bd"]["be"]["bf"]["cd"]["ce"]["cf"]   # i=2 == len(digits), add to result

*We might need O(n) extra space to know what character possibilities we have.

PLAN:
- Declare and initialize a res list as well as a temp list
- Declare and intitialize a dictionary with digit (key) and characters (string, value)
- Declare and initialize a backtrack_dfs that takes index i of the digit string:
    if i > len(digits):
        res.append("".join(temp))
        return

    for every character in dictionary[digit]:
        temp.append(character)
        backtrack_dfs(i + 1)
        temp.pop()
- backtrack_dfs(0)
- return res

Time complexity: O(n*4^n)
Space complexity: O(n)
'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        res, temp = [], []
        digit_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        } # dictionary with all possible combinations of digit: character

        def backtrack_dfs(i):
            if i == len(digits):
                res.append("".join(temp))
                return

            for c in digit_to_char[digits[i]]:
                temp.append(c)
                backtrack_dfs(i + 1)
                temp.pop()

        backtrack_dfs(0)
        return res
        
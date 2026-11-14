'''
Input: an integer n
Output: a list of strings with all the well-formed parentheses strings that can be generated with n pairs of parentheses

Approach: backtracking with a decision tree. The left branch of the decision tree adds an opening parenthesis, and the right branch adds a closing one, as long as we follow these rules:
1. if the opening count == the closing count == n, then we join the list into a string and add it to the results
2. if the opening count is lower than n, then we add an opening parenthesis and recurse with opening count + 1 and the same closing count
3. if the closing count is lower than the opening count, then we add a closing parenthesis and recurse with closing count + 1 and the same opening count
* for both 2 and 3, we need to pop after the recursive call returns, to undo the choice before trying the next branch

Decision tree for n = 3:
                                [(]
                    /                         \
                [((]                          [()]
            /          \                    /       \
        [(((]          [(()]             [()(]       [x]
          |           /     \            /    \
       [((()]     [(()(]   [(())]    [()((]   [()()]
          |          |        |         |        |
       [((())]   [(()()]   [(())(]   [()(()]  [()()(]
          |          |        |         |        |
       [((()))]  [(()())]  [(())()]  [()(())]  [()()()]
* the x means that branch is not allowed, because closing would be greater than opening
* a | means only one branch is allowed at that spot, because one of the rules blocks the other
* the bottom row has the 5 strings that get added to res

PLAN:
- temp, res = [], []
- declare backtracking(opening_count, closing_count):
    - if opening_count == closing_count == n:
        - res.append("".join(temp))
        - return
    - if opening_count < n:
        - temp.append('(')
        - backtracking(opening_count + 1, closing_count)
        - temp.pop()
    - if closing_count < opening_count:
        - temp.append(')')
        - backtracking(opening_count, closing_count + 1)
        - temp.pop()
- call backtracking(0, 0)
- return res

# Time complexity: O(4^n / sqrt(n)). Each string has 2n characters, and each character has at most 2 choices, so a loose upper bound is 2^(2n) = O(4^n). The rules cut a lot of branches, though, and the number of valid strings is the nth Catalan number, which grows like 4^n / (n * sqrt(n)). Each valid string costs O(n) to join, so the total comes out to O(4^n / sqrt(n)).
# Space complexity: O(n) not counting the output, because the recursion stack and temp both go at most 2n deep. Counting the output, it is O(4^n / sqrt(n)), since res holds all the valid strings of size 2n.
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        temp, res = [], []

        def backtracking_dfs(opening, closing):
            if opening == closing == n:
                res.append("".join(temp))
                return
            
            if opening < n:
                temp.append('(')
                backtracking_dfs(opening + 1, closing)
                temp.pop()

            if closing < opening:
                temp.append(')')
                backtracking_dfs(opening, closing + 1)
                temp.pop()

        backtracking_dfs(0, 0)
        return res
        
'''
Input: an integer n
Output: a list of lists of strings, where each list is one distinct solution to the n-queens puzzle

Approach: a decision tree with backtracking. Each level of the tree is one row of the board, and each branch is a column where we try to place the queen in that row, so every level has at most n branches. Before we place a queen, we check if that spot is safe from the queens already on the board. If it isn't, we prune that branch.
                        n = 4
        /           /           \           \
    ["Q..."]    [".Q.."]        ["..Q."]    ["...Q"]
    /       \
[".Q.."]     ["..Q."]
(PRUNE)        ...

* We need a helper function, checkSolution, that checks if a spot is safe by comparing it against every queen in the rows above it. If another queen is in the same column or on the same diagonal, it returns False, otherwise it returns True. We don't need to check rows, since we only place one queen per row.
* If checkSolution returns False, we stop exploring that branch!

PLAN:
- declare and initialize self.res and self.temp = [], []
- call backtrack(0)
- return self.res

- declare and initialize backtrack that takes r and n:
    - if r == n:
        - self.res.append(self.temp.copy())
        - return

    - for c in range(n):
        - if self.checkSolution(r, c):
            - self.temp.append("." * c + "Q" + "." * (n - c - 1))
            - backtrack(r + 1)
            - self.temp.pop()

- declare and initialize checkSolution(self, row, col):
    - for r in range(len(self.temp)):
        - q_col = self.temp[r].index("Q")      # column of the queen in row r
        - if q_col == col:                     # vertical
            - return False
        - if abs(row - r) == abs(col - q_col): # diagonal
            - return False
    - return True

Time complexity: O(n!), since the first row has n choices, the second has at most n - 1 safe choices, and so on. Each checkSolution call also scans the rows above, but n! dominates.
Space complexity: O(n^2) for temp (n rows of length n), plus O(n) for the recursion stack, not counting the output.
'''

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.res, self.temp = [], []
        self.backtrack(0)
        return self.res
    
    def backtrack(self, r):
        if r == self.n:
            self.res.append(self.temp.copy())
            return

        for c in range(self.n):
            if self.checkSolution(r, c):
                self.temp.append("." * c + "Q" + "." * (self.n - c - 1))
                self.backtrack(r + 1)
                self.temp.pop()


    def checkSolution(self, row, col):
        for r in range(len(self.temp)):
            q_col = self.temp[r].index("Q")
            if q_col == col: # vertical
                return False
            if abs(row - r) == abs(col - q_col): # diagonal
                return False

        return True
        
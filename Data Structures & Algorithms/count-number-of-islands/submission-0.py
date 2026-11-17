'''
Input: a grid with 0s and 1s
Output: the number of islands

Approach: a for loop in the graph (grid) that whenever it finds a 1, it increments the count to 1 and calls a dfs in it to mark all the adjacent spots that equal to 1 with an X so we don't revisit it.

                                (1,1) ✓
              /             /           \            \
         (0,1) ✓       (2,1) ✗         (1,0) ✗       (1,2) ✗
        /       \      is 0              is 0          is 0
   (0,0) ✓    (0,2) ✓
      |          |
   (1,0) ✓    (1,2) ✗ is 0
      |
   (2,0) ✓
      |
   (2,1) ✗ is 0                        ✓ = marked the spot from 1 to X

PLAN:
- declare numIslands(grid):
    self.grid = grid
    self.ROWS = len(grid)
    self.COLS = len(grid[0])
    count = 0
    for i in range(self.ROWS):
        for j in range(self.COLS):
            if self.grid[i][j] == 1:
                count +=1
                self.dfs(i, j)
    return count

- declare dfs(self, row, col):
    if min(row, col) < 0 or row == self.ROWS or col == self.COLS:
        return
    if self.grid[row][col] == "0" or self.grid[row][col] == "x"
        return

    self.grid[row][col] = "x"

    self.dfs(row + 1, col)
    self.dfs(row - 1, col)
    self.dfs(row, col + 1)
    self.dfs(row, col - 1)

Time complexity: O(4^(m*n)) since we take 4 recursive decisions that will be to the power of at most m times n
Space complexity: Recurisve call stack takes O(m*n) 
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.ROWS = len(grid)
        self.COLS = len(grid[0])
        
        count = 0

        for i in range(self.ROWS):
            for j in range(self.COLS):
                if self.grid[i][j] == "1":
                    count +=1
                    self.dfs(i, j)

        return count
    
    def dfs(self, row, col):
        if min(row, col) < 0 or row == self.ROWS or col == self.COLS:
            return
        if self.grid[row][col] == "0" or self.grid[row][col] == "x":
            return

        self.grid[row][col] = "x"

        self.dfs(row + 1, col)
        self.dfs(row - 1, col)
        self.dfs(row, col + 1)
        self.dfs(row, col - 1)
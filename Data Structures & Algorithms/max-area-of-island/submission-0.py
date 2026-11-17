'''
Input: a grid of "0"s and "1"s, where "1" is land and "0" is water
Output: the maximum area of an island in the grid

Approach: graph DFS. We loop through every cell in the grid, and whenever we find a "1", we call a DFS on it to count the max number of squares within that island. The DFS marks that cell and every connected "1" with an "x", so we never count or revisit the same island again.

Grid:            After island 1:     After island 2:
1 1 1            x x x               x x x
1 1 0            x x 0               x x 0
1 0 1            x 0 1               x 0 x

Island 1, DFS starting at (0,0) (out of bounds branches left out):

                    (0,0) ✓
                /            \
          (1,0) ✓          (0,1) ✗ already x
         /       \
    (2,0) ✓     (1,1) ✓
       |       /     |      \
  (2,1) ✗   (2,1) ✗ (0,1) ✓  (1,2) ✗
   is 0      is 0     |       is 0
                    (0,2) ✓
                      |
                    (1,2) ✗ is 0

Island 2, DFS starting at (2,2):

    (2,2) ✓   (every neighbor is 0 or out of bounds)

count = 2                                    ✓ = marked the spot from "1" to "x"

PLAN:
- declare numIslands(grid):
    - self.grid = grid
    - self.ROWS = len(grid)
    - self.COLS = len(grid[0])
    - maxArea = 0
    - for i in range(self.ROWS):
        - for j in range(self.COLS):
            - if self.grid[i][j] == "1":
                - maxArea = max(maxArea, self.dfs(i, j))
    - return maxArea

- declare dfs(self, row, col):
    - if min(row, col) < 0 or row == self.ROWS or col == self.COLS:
        - return 0
    - if self.grid[row][col] == "0" or self.grid[row][col] == "x":
        - return 0

    - self.grid[row][col] = "x"
    - islandCount = 1

    - islandCount += self.dfs(row + 1, col)
    - islandCount += self.dfs(row - 1, col)
    - islandCount += self.dfs(row, col + 1)
    - islandCount += self.dfs(row, col - 1)

    - return islandCount

Time complexity: O(m * n), where m is the number of rows and n is the number of columns, since each cell gets marked "x" at most once and is never visited again
Space complexity: O(m * n) for the recursion call stack in the worst case, when the whole grid is one island
'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.ROWS = len(grid)
        self.COLS = len(grid[0])
        
        maxArea = 0

        for i in range(self.ROWS):
            for j in range(self.COLS):
                if self.grid[i][j] == 1:
                    maxArea = max(maxArea, self.dfs(i, j))

        return maxArea
    
    def dfs(self, row, col) -> int:
        if min(row, col) < 0 or row == self.ROWS or col == self.COLS:
            return 0
        if self.grid[row][col] == 0 or self.grid[row][col] == -1:
            return 0

        self.grid[row][col] = -1
        islandCount = 1

        islandCount += self.dfs(row + 1, col)
        islandCount += self.dfs(row - 1, col)
        islandCount += self.dfs(row, col + 1)
        islandCount += self.dfs(row, col - 1)

        return islandCount
'''
1. What if we can't modify the input grid?
   Instead of marking cells with "x", I'd keep a visited set of (row, col) tuples and skip any cell that's already in it. Time stays O(m * n), but now the set adds O(m * n) extra space.

2. What if the grid is huge and the recursion goes too deep?
   I'd switch from recursive DFS to BFS with a queue, so I never hit Python's recursion limit. Time stays O(m * n), and I'd mark cells as visited when I add them to the queue so none get added twice.
'''
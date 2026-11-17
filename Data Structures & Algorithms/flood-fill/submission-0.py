'''
Input: an image (represented by a grid), sr and sc (starting row/column ints), and color (int)
Output: the same image/grid, but with every pixel that has the same color as grid[sr][sc] and is connected to (sr, sc) changed to color

Approach: graph DFS. We first save the color of the (sr, sc) pixel, change it, and then run a DFS by recursively calling the DFS function on the pixels at the top, bottom, left, and right of the initial one. By calling it recursively, we run the same process for the neighbors of every pixel we paint, so the color spreads to every connected pixel with the original color.

                              (1,1) ✓
              /             /           \            \
         (0,1) ✓       (2,1) ✗         (1,0) ✗       (1,2) ✗
        /       \      is 0         already 2      is 0
   (0,0) ✓    (0,2) ✓
      |          |
   (1,0) ✓    (1,2) ✗ is 0
      |
   (2,0) ✓
      |
   (2,1) ✗ is 0

Before:          After:
1 1 1            2 2 2
1 [1] 0          2 2 0
1 0 1            2 0 1

PLAN:
- declare a function floodFill (default function):
    - self.grid = grid
    - self.ROWS = len(grid)
    - self.COLS = len(grid[0])
    - self.cur_color = grid[sr][sc]
    - self.color = color
    - if self.cur_color == self.color:
        - return self.grid
    - self.dfsFill(sr, sc)
    - return self.grid

- declare a function called dfsFill that takes a row and column:
    - if min(row, col) < 0 or row == self.ROWS or col == self.COLS:
        - return
    - if self.grid[row][col] != self.cur_color:
        - return

    - self.grid[row][col] = self.color

    - self.dfsFill(row + 1, col)
    - self.dfsFill(row - 1, col)
    - self.dfsFill(row, col + 1)
    - self.dfsFill(row, col - 1)

Time complexity: O(n * m), where n is the number of rows and m is the number of columns, since each pixel gets painted at most once
Space complexity: O(n * m) for the recursion stack in the worst case, when every pixel needs to be painted
'''

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.grid = image
        self.ROWS = len(image)
        self.COLS = len(image[0])
        self.cur_color = image[sr][sc]
        self.color = color
        if self.cur_color == color:
            return self.grid
        self.dfsFill(sr, sc)
        return self.grid
        
    
    def dfsFill(self, row, col):
        if min(row, col) < 0 or row == self.ROWS or col == self.COLS:
            return
        if self.grid[row][col] != self.cur_color:
            return

        self.grid[row][col] = self.color

        self.dfsFill(row + 1, col)
        self.dfsFill(row - 1, col)
        self.dfsFill(row, col + 1)
        self.dfsFill(row, col - 1)
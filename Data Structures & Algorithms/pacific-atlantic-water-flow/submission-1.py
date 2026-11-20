'''
Input: a rectangular island of heights, where each position has a number representing the height above sea level at that specific [row, col]
Output: a list of coordinates [row, col], where each coordinate is a cell where water can flow to BOTH the Pacific and Atlantic oceans

Approach: BFS (or DFS), but backwards. Instead of checking where water flows from every cell, we start from the borders, since those cells already touch an ocean, and go "uphill" to neighbors with equal or larger heights. If water can climb up from the ocean to a cell, then water from that cell can flow down to the ocean.
We run the BFS twice:
    - once starting from the Pacific borders (top row and left column)
    - once starting from the Atlantic borders (bottom row and right column)
Each BFS fills its own set with every cell that can reach that ocean. The answer is every cell that is in BOTH sets.

PLAN:
- inside the pacificAtlantic function, declare and initialize self.ROWS, self.COLS, self.grid, self.queue, self.pacific, and self.atlantic
    - traverse the Pacific borders (top row and left column), add them to the queue, and add them to self.pacific
    - call bfs for the pacific
    - traverse the Atlantic borders (bottom row and right column), add them to the queue, and add them to self.atlantic
    - call bfs for the atlantic
    - return every cell that is in both sets (the intersection), as a list of [row, col] lists

- inside a function called bfs that takes which ocean we are running it for:
    - directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    - pick the set for that ocean (self.pacific or self.atlantic)
    - while queue:
        - temp = pop from the queue
        - for dr, dc in directions:
            - nr, nc = temp[0] + dr, temp[1] + dc
            - if (nr, nc) is out of the grid's boundaries, already in the set, or lower than temp's height:
                - continue
            - add (nr, nc) to the set and to the queue

Time complexity: O(m * n), where m is the number of rows and n is the number of columns, since each BFS visits each cell at most once
Space complexity: O(m * n) for the two sets and the queue
'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.ROWS = len(heights)
        self.COLS = len(heights[0])
        self.queue = deque()
        self.grid = heights
        self.pacific, self.atlantic = set(), set()

        for i in range(self.ROWS):
            self.queue.append((i, 0))
            self.pacific.add((i, 0))
        for j in range(self.COLS):
            self.queue.append((0, j))
            self.pacific.add((0, j))


        # call bfs
        self.bfs()

        for i in range(self.ROWS):
            self.queue.append((i, self.COLS - 1))
            self.atlantic.add((i, self.COLS - 1))
        for j in range(self.COLS):
            self.queue.append((self.ROWS - 1, j))
            self.atlantic.add((self.ROWS - 1, j))

        # call bfs second time
        self.bfs("atlantic")

        # return a union of the two sets
        return [list(c) for c in self.pacific & self.atlantic]
    
    def bfs(self, val = "pacific"):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while self.queue:
            for _ in range(len(self.queue)):
                temp = self.queue.popleft()
                for dr, dc in directions:
                    nr, nc = temp[0] + dr, temp[1] + dc
                    if min(nr, nc) < 0 or nr == self.ROWS or nc == self.COLS:
                        continue
                    if self.grid[nr][nc] >= self.grid[temp[0]][temp[1]]:
                        if val == "pacific" and (nr, nc) not in self.pacific:
                            self.queue.append((nr, nc))
                            self.pacific.add((nr, nc))
                        if val == "atlantic" and (nr, nc) not in self.atlantic:
                            self.queue.append((nr, nc))
                            self.atlantic.add((nr, nc))


                    
        
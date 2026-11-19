'''
Input: a graph, represented by a matrix, where -1 is water, 0 is a treasure, and INF (2147483647) is land
Output: the same graph, modified in place, where every land cell holds its shortest distance to a treasure (it stays INF if it can't reach any treasure)

Approach: multi-source BFS from every 0 position. In other words, we start the queue with all the positions with value == 0, and then run BFS one level at a time. The first time the BFS reaches a land cell, that level is its shortest distance to a treasure, so we write it into the grid. Since that cell isn't INF anymore, we never visit it again.

Plan:
In the main function:
    - make self.grid, self.ROWS, self.COLS, and self.queue
    - traverse the grid to find all positions where val == 0 and add them to the queue
    - call the helper bfs
    - return the grid

In a separate function called bfs that doesn't take any parameters:
    - count = 0
    - directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    - while queue:
        - count += 1
        - for _ in range(len(queue)):
            - pop from the queue and save it to temp
            - for dr, dc in directions:
                - nr, nc = temp[0] + dr, temp[1] + dc
                - if (nr, nc) is out of bounds or grid[nr][nc] isn't INF (water, treasure, or already visited):
                    - continue
                - grid[nr][nc] = count
                - add (nr, nc) to the queue

Time complexity: O(m * n), where m is the number of rows and n is the number of columns, since each cell gets added to the queue at most once
Space complexity: O(m * n) for the queue
'''


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        self.grid = grid
        self.ROWS = len(grid)
        self.COLS = len(grid[0])
        self.queue = deque()

        for i in range(self.ROWS):
            for j in range(self.COLS):
                if grid[i][j] == 0:
                    self.queue.append((i, j))

        self.bfs()
        return None


    def bfs(self):
        count = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while self.queue:
            count += 1
            for _ in range(len(self.queue)):
                temp = self.queue.popleft()
                for dr, dc in directions:
                    nr, nc = temp[0] + dr, temp[1] + dc
                    if min(nr, nc) < 0 or nr == self.ROWS or nc == self.COLS or self.grid[nr][nc] != 2147483647:
                        continue
                    self.grid[nr][nc] = count
                    self.queue.append((nr, nc))
        
'''
Input: an n x n binary matrix
Output: the length of the shortest clear path from (0, 0) to (n - 1, n - 1), counting the number of cells in the path, or -1 if there is no clear path

Approach: BFS using a queue in this graph. We can move in all 8 directions (including diagonals).

Grid:
[0] 1  0
 1 [0] 0
 1  1 [0]

level 1:                  (0,0) ✓
                    /        |        \
level 2:      (0,1) ✗     (1,0) ✗     (1,1) ✓
               is 1        is 1     /    |    \
level 3:                      (0,2) ✓ (1,2) ✓ (2,2) ✓ target! return 3

(the other neighbors of (1,1) are 1s or already visited, so they're left out)

*Every time we go to a different level of the graph, we increment a count, and once we find out that we are at position (n - 1, n - 1), we can return this count.

PLAN:
- if grid[0][0] == 1:
    - return -1
- declare and initialize n = len(grid)
- declare and initialize a set visited with (0, 0) in it, so we don't change the initial grid
- declare and initialize a queue with the initial position (0, 0)
- declare and initialize directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
- declare and initialize a count variable equal to 0
- while queue:
    - count += 1
    - for _ in range(len(queue)):
        - pos = queue.popleft()
        - if pos[0] == pos[1] == n - 1:
            - return count
        - for dr, dc in directions:
            - nr, nc = pos[0] + dr, pos[1] + dc
            - if min(nr, nc) < 0 or nr == n or nc == n or grid[nr][nc] == 1 or (nr, nc) in visited:
                - continue
            - visited.add((nr, nc))
            - queue.append((nr, nc))
- return -1

Time complexity: O(n * n), since each cell gets added to the queue at most once and we check 8 directions for each one
Space complexity: O(n * n) for the visited set and the queue
'''

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        queue = deque([(0, 0)])
        n = len(grid)
        visited = set([(0, 0)])
        directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
        count = 0

        while queue:
            count += 1
            for _ in range(len(queue)):
                pos = queue.popleft()
                if pos[0] == pos[1] == n - 1:
                    return count
                for dr, dc in directions:
                    nr, nc = pos[0] + dr, pos[1] + dc
                    if min(nr, nc) < 0 or nr == n or nc == n or grid[nr][nc] == 1 or (nr, nc) in visited:
                        continue
                    visited.add((nr, nc))
                    queue.append((nr, nc))

        return -1
        
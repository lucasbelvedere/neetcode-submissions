'''
Input: a grid where 0 is an empty cell, 1 is a fresh fruit, and 2 is a rotten fruit
Output: the number of minutes it takes for all the fruits to get rotten, or -1 if at least one fruit never gets rotten

Approach: multi-source BFS in the grid, with two sets: one for fresh fruits, and one for rotten fruits that also works as visited once we start the BFS.
First, we traverse the whole grid to find all the rotten and fresh fruits and add them to their sets.
Then, we add all the rotten fruits to a queue, start a timer = 0, and run the BFS one level at a time, where each level is one minute. Whenever a fruit gets rotten, we add it to the rotten set and remove it from the fresh set.
Finally, we return -1 if freshSet still has fruits, otherwise we return the timer.

PLAN:
- n, m = len(grid), len(grid[0])
- freshSet, rottenSet = set(), set()
- queue = deque()
- for i in range(n):
    - for j in range(m):
        - if grid[i][j] == 1:
            - freshSet.add((i, j))
        - if grid[i][j] == 2:
            - rottenSet.add((i, j))
            - queue.append((i, j))
- timer = 0
- directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
- while queue and freshSet:
    - timer += 1
    - for _ in range(len(queue)):
        - pos = queue.popleft()
        - for dr, dc in directions:
            - nr, nc = pos[0] + dr, pos[1] + dc
            - if min(nr, nc) < 0 or nr == n or nc == m or (nr, nc) in rottenSet:
                - continue
            - if grid[nr][nc] == 1:
                - freshSet.remove((nr, nc))
                - rottenSet.add((nr, nc))
                - queue.append((nr, nc))
- return -1 if freshSet else timer

Time complexity: O(n * m)
Space complexity: O(n * m)
'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        freshSet, rottenSet = set(), set()
        queue = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    freshSet.add((i, j))

                if grid[i][j] == 2:
                    rottenSet.add((i, j))
                    queue.append((i, j))

        timer = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue and freshSet:
            timer += 1

            for _ in range(len(queue)):
                pos = queue.popleft()

                for dr, dc in directions:
                    nr, nc = pos[0] + dr, pos[1] + dc

                    if min(nr, nc) < 0 or nr == n or nc == m or (nr, nc) in rottenSet:
                        continue

                    if grid[nr][nc] == 1:
                        freshSet.remove((nr, nc))
                        rottenSet.add((nr, nc))
                        queue.append((nr, nc))

        return -1 if freshSet else timer
        
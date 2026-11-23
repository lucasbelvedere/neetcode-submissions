'''
Input: a board (m x n matrix) containing either "X" or "O"
Output: nothing, the board is modified in place so that every surrounded region is captured

Approach: BFS from the edge cells. We add every edge cell that equals "O" to a queue and run BFS to add the coordinates of every "O" connected to them to a set.
Once we're done, we loop through the inner cells of the board, and every "O" whose coordinates are not in the set gets updated to "X".

Plan:
- def solve:
    - it takes board, and we save it as self.board
    - declare self.queue and self.visited
    - call self.bfs
    - for every position that is not on the edge of the board:
        - if it equals "O" and is not in visited, update it to "X"
- def a function bfs:
    - declare any missing variables, including directions, the queue (if it wasn't declared in the main function), etc.
    - while queue:
        - for _ in range(len(queue)):
            - temp = queue.popleft()
            - for dr, dc in directions:
                - nr, nc = temp[0] + dr, temp[1] + dc
                - if (nr, nc) is not within the board, continue
                - else, if it equals "O", add it to the visited set

Time complexity: O(m * n), where m and n are self.rows and self.cols
Space complexity: O(m * n) extra space for the queue and the set
'''

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if len(board) == 1:
            return
        self.board = board
        self.queue, self.visited = deque(), set()
        self.rows, self.cols = len(board), len(board[0])
       
        for i in range(self.rows):
            if board[i][0] == "O":
                self.queue.append((i, 0))
                self.visited.add((i, 0))
            if board[i][self.cols - 1] == "O":
                self.queue.append((i, self.cols - 1))
                self.visited.add((i, self.cols - 1))


        if len(board) > 1: # missing edges
            for j in range(self.cols):
                if board[0][j] == "O":
                    self.queue.append((0, j))
                    self.visited.add((0, j))
                if board[self.rows - 1][j] == "O":
                    self.queue.append((self.rows - 1, j))
                    self.visited.add((self.rows - 1, j))


        self.bfs()
        for i in range(1, self.rows - 1):
            for j in range(1, self. cols - 1):
                if (i, j) not in self.visited and board[i][j] == "O":
                    board[i][j] = "X"

    def bfs(self):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while self.queue:
            for _ in range(len(self.queue)):
                temp = self.queue.popleft()
                for dr, dc in directions:
                    nr, nc = temp[0] + dr, temp[1] + dc
                    if min(nr, nc) < 0 or nr == self.rows or nc == self.cols:
                        continue
                    if (nr, nc) not in self.visited and self.board[nr][nc] == "O":
                        self.visited.add((nr, nc))
                        self.queue.append((nr, nc))
        
        
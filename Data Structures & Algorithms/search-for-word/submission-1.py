'''
Input: a list of lists that represents a board, and a word
Output: True if the word is present in the board, False otherwise

Approach: DFS with backtracking, building a decision tree. We first traverse the board. Once we find a letter that equals word[0], we call the helper function, which recursively builds the decision tree by trying all 4 directions (north, south, east, west) from each matching letter.
        [C]
    [B]  [A]  [D]
...

PLAN:
- Declare and initialize ROWS = len(board) and COLS = len(board[0])
- Declare and initialize a temp list, empty
- Declare and initialize a helper function backtrack that takes i (index in word) and position:
    - if temp's len equals word's len:
        - return "".join(temp) == word
    - if position is lower than 0 or greater than or equal to ROWS * COLS:
        - return False
    - curr_row = position // COLS
    - curr_col = position % COLS
    - if board[curr_row][curr_col] != word[i]:
        - return False

    - declare and initialize found = False
    - temp.append the character
    - mark board[curr_row][curr_col] = "#" as visited, so we don't reuse the same cell
    - if curr_row - 1 >= 0 and not found:      #North
        - found = backtrack(i + 1, position - COLS)
    - if curr_row + 1 < ROWS and not found:    #South
        - found = backtrack(i + 1, position + COLS)
    - if curr_col + 1 < COLS and not found:    #East
        - found = backtrack(i + 1, position + 1)
    - if curr_col - 1 >= 0 and not found:      #West
        - found = backtrack(i + 1, position - 1)
    - unmark the cell: board[curr_row][curr_col] = word[i]
    - temp.pop
    - return found

- Main:
    - for position in range(ROWS * COLS):
        - if backtrack(0, position):
            - return True
    - return False
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        temp = []

        def backtrack(i, pos):
            if len(temp) == len(word):
                return "".join(temp) == word
            if pos < 0 or pos >= ROWS * COLS:
                return False

            row = pos // COLS
            col = pos % COLS

            if board[row][col] != word[i]:
                return False
            if len(temp) + 1 == len(word):
                return True

            found = False
            temp.append(word[i])
            board[row][col] = "#"

            # visit north, south, east, west
            if row - 1 >= 0 and not found:
                found = backtrack(i + 1, pos - COLS)
            if row + 1 < ROWS and not found:
                found = backtrack(i + 1, pos + COLS)
            if col + 1 < COLS and not found:
                found = backtrack(i + 1, pos + 1)
            if col - 1 >= 0 and not found:
                found = backtrack(i + 1, pos - 1)
        
            board[row][col] = word[i]
            temp.pop()
            return found

        for position in range(ROWS * COLS):
            if backtrack(0, position):
                return True
        return False
        
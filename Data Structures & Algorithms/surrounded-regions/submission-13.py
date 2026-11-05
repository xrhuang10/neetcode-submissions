class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def surround(row, col):

            if not (0 <= row < ROWS and 0 <= col < COLS and board[row][col] == 'O'):
                return
            board[row][col] = 'S'
            for dr, dc in directions:
                surround((row + dr), (col + dc))
            return

        for i in range(ROWS):
            if board[i][0] == 'O':
                surround(i, 0)
            if board[i][COLS - 1] == 'O':
                surround(i, COLS - 1)
        
        for j in range(COLS):
            if board[0][j] == 'O':
                surround(0, j)
            if board[ROWS - 1][j] == 'O':
                surround(ROWS - 1, j)
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'S':
                    board[i][j] = 'O'
        
        
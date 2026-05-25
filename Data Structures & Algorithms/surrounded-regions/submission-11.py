class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ROWS = len(board)
        COLS = len(board[0])
        safe = set()

        #start from borders. if Os are connceted, add to safe. then, iterate thorugh grid if not safe, make X.

        def dfs(row, col):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or board[row][col] == 'X' or (row, col) in safe:
                return

            safe.add((row, col))
            
            for dr, dc in directions:
                newrow, newcol = row + dr, col + dc
                dfs(newrow, newcol)
            

        for col in range(COLS):
            if board[0][col] == 'O':
                dfs(0, col)
            if board[ROWS - 1][col] == 'O':
                dfs(ROWS - 1, col)
        
        for row in range(ROWS):
            if board[row][0] == 'O':
                dfs(row, 0)
            if board[row][COLS - 1] == 'O':
                dfs(row, COLS - 1)
            
        
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'O' and (row, col) not in safe:
                    board[row][col] = 'X'


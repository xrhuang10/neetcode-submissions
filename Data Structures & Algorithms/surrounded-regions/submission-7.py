class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ROWS = len(board)
        COLS = len(board[0])
        safe = set()

        def dfs(row, col):
            safe.add((row, col))
            for dr, dc in directions:
                newrow = row + dr
                newcol = col + dc
                if newrow < 0 or newrow >= ROWS or newcol < 0 or newcol >= COLS or board[newrow][newcol] == 'X' or (newrow, newcol) in safe:
                    continue
            
                dfs(newrow, newcol)

        
        for c in range(COLS):
            if board[0][c] == 'O': 
                dfs(0, c)
                safe.add((0, c))
            if board[ROWS-1][c] == 'O': 
                dfs(ROWS-1, c)
                safe.add((ROWS - 1, c))

        for r in range(ROWS):
            if board[r][0] == 'O': 
                dfs(r, 0)
                safe.add((r, 0))
            if board[r][COLS - 1] == 'O': 
                dfs(r, COLS - 1)
                safe.add((r, COLS - 1))
    
        
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in safe and board[i][j] == 'O':
                    board[i][j] = 'X'
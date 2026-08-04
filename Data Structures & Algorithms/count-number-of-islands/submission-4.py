class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        counter = 0

        def backtrack(row, col):
            if not(0 <= row < ROWS and 0<= col < COLS and grid[row][col] == '1'):
                return False
            grid[row][col] = '0'
            for dr, dc in directions:
                backtrack(row + dr, col + dc)
            return True
    

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    backtrack(i, j)
                    counter += 1
        
        return counter

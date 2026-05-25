class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0
        seen = set()
        ROWS = len(grid)
        COLS = len(grid[0])


        def backtrack(row, col):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or (row, col) in seen or grid[row][col] == 0:
                return 0


            seen.add((row, col))
            
            return 1 + backtrack(row - 1, col) + backtrack(row + 1, col) + backtrack(row, col - 1) + backtrack(row, col + 1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in seen:
                    maxarea = max(maxarea, backtrack(i, j))
        
        return maxarea
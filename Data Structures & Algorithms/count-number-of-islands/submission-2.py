class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.counter = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        seen = set()


        def backtrack(row, col, seen):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or (row, col) in seen or grid[row][col] == '0':
                return 

            seen.add((row, col))
            backtrack(row - 1, col, seen)
            backtrack(row + 1, col, seen) 
            backtrack(row, col - 1, seen) 
            backtrack(row, col + 1, seen) 
            
            return 
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in seen:
                    backtrack(i, j, seen)
                    self.counter += 1

                
        
        return self.counter
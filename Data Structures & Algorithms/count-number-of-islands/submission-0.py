class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.counter = 0
        rows_count = len(grid)
        cols_count = len(grid[0])
        

        def backtrack(row, col):
            
            if row >= rows_count or row < 0 or col >= cols_count or col < 0  or grid[row][col] == '0':
                return False
            
            grid[row][col] = '0'
            
            backtrack(row + 1, col) 
            backtrack(row - 1, col) 
            backtrack(row, col + 1) 
            backtrack(row, col - 1)

            return True

            
            
            
        for i in range(rows_count):
            for j in range(cols_count):

                if backtrack(i, j):
                    self.counter += 1
                
            
        

        
        return self.counter
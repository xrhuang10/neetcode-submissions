class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maximum = 0
        rows_count = len(grid)
        cols_count = len(grid[0])
        seen = set()
        

        def backtrack(row, col):
            
            if row >= rows_count or row < 0 or col >= cols_count or col < 0  or (row, col) in seen or grid[row][col] == 0:
                return 0
            
            counter = 1
            seen.add((row, col))
            
            counter += backtrack(row + 1, col) 
            counter += backtrack(row - 1, col) 
            counter += backtrack(row, col + 1) 
            counter += backtrack(row, col - 1)


            return counter
            
            
        for i in range(rows_count):
            for j in range(cols_count):
                
                counter = backtrack(i, j)
                
                maximum = max(maximum, counter)
                
        
        
        return maximum
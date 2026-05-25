class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        ROWS = len(grid)
        COLS = len(grid[0])



        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i, j))

        distance = 0
        
        
        while q:
            distance += 1
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    newrow, newcol = row + dr, col + dc
                    if newrow >= 0 and newrow < ROWS and newcol >= 0 and newcol < COLS and grid[newrow][newcol] == 2147483647:
                        grid[newrow][newcol] = distance
                        q.append((newrow, newcol))
            
            
            
        





        
        
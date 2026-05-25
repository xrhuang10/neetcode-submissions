class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = deque()
        minutes = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
        

        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    newrow = row + dr
                    newcol = col + dc
                    if newrow >= 0 and newrow < len(grid) and newcol >= 0 and newcol < len(grid[0]) and grid[newrow][newcol] == 1:
                        grid[newrow][newcol] = 2 
                        q.append((newrow, newcol))     
            if q:
                minutes += 1

        


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return minutes

            
        
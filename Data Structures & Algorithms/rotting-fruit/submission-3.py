class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = deque()
        minutes = 0

        def isvalid(row, col, grid):
            if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]):
                return True
            else:
                return False

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))

        while q:
            
            for orange in range(len(q)):
                row, col = q.popleft()
                
                for dr, dc in directions:
                    newrow, newcol = row + dr, col + dc
                    if isvalid(newrow, newcol, grid) and grid[newrow][newcol] == 1:
                        grid[newrow][newcol] = 2
                        q.append((newrow, newcol))
            if q:
                minutes += 1

            

        if any(1 in row for row in grid):
            return -1
        
        return minutes
                    

            
        
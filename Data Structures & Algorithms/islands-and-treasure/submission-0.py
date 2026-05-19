class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def isvalid(row, col, grid):
            if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]):
                return True
            else:
                return False
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i, j))
        
        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                newrow, newcol = row + dr, col + dc
                if isvalid(newrow, newcol, grid) and grid[newrow][newcol] == 2147483647:
                    grid[newrow][newcol] = grid[row][col] + 1
                    q.append((newrow, newcol))



        
        
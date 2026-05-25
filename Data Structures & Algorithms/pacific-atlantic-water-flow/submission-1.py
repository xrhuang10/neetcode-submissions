class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pac = set()
        atl = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        res = []

        def dfs(row, col, visit, prevheight):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or (row, col) in visit or heights[row][col] < prevheight:
                return
            
            visit.add((row, col))
            for dr, dc in directions:
                dfs(row + dr, col + dc, visit, heights[row][col])
        
        for col in range(COLS):
            dfs(0, col, pac, 0)
            dfs(ROWS - 1, col, atl, 0)
        
        for row in range(ROWS):
            dfs(row, 0, pac, 0)
            dfs(row, COLS - 1, atl, 0)
        

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])
        
        return res
            


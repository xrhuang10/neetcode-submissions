class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pac = set()
        atl = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(row, col, visit, prevHeight):
            if not (row >= 0 and row < ROWS and col >= 0 and col < COLS and (row, col) not in visit and heights[row][col] >= prevHeight):
                return
            
            visit.add((row, col))

            for dr, dc in directions:
                dfs(row + dr, col + dc, visit, heights[row][col])


        for c in range(COLS):
            dfs(0, c, pac, 0)
            dfs(ROWS - 1, c, atl, 0)

        for r in range(ROWS):
            dfs(r, 0, pac, 0)
            dfs(r, COLS - 1, atl, 0)

        answer = []
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) in pac and (i, j) in atl:
                    answer.append([i, j])
        
        return answer

            


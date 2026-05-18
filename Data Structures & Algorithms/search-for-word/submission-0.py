class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_total = len(board)
        col_total = len(board[0])
        seen = set()
        

        def backtrack(row, col, i):
            if i == len(word):
                return True
            if row >= row_total or row < 0 or col >= col_total or col < 0 or (row, col) in seen or board[row][col] != word[i] :
                return False
            
 
           
            seen.add((row, col))
            res = backtrack(row + 1, col, i + 1) or backtrack(row - 1, col, i + 1) or backtrack(row, col + 1, i + 1) or backtrack(row, col - 1, i + 1)
            seen.remove((row, col))

            return res
        
        for i in range(row_total):
            for j in range(col_total):
                if backtrack(i, j, 0) == True:
                    return True
        
        return False
        
            



class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [n * ['.'] for i in range(n)]
        print(board)
        
        res = []

        cols = set()
        posdiag = set()
        negdiag = set()

        def backtrack(row):
            if row == n:
                copy = [''.join(row) for row in board]
                res.append(copy)
                return
            
            for col in range(n):
                if row - col in negdiag or row + col in posdiag or col in cols:
                    continue
                
                board[row][col] = 'Q'
                
                cols.add(col)
                negdiag.add(row - col)
                posdiag.add(row + col)

                
                backtrack(row + 1)

                board[row][col] = '.'

                cols.remove(col)
                negdiag.remove(row - col)
                posdiag.remove(row + col)
            
            return
        
        backtrack(0)
        return res






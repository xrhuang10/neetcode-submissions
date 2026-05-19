class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [n * ["."] for i in range(n)]
        result = []
        print(result)

        cols = set()
        posdiag = set()
        negdiag = set()
        
        def backtrack(row):
            if row == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return

            for col in range(n):
                if row - col in negdiag or row + col in posdiag or col in cols:
                    continue
            
                cols.add(col)
                negdiag.add(row - col)
                posdiag.add(row + col)
                board[row][col] = "Q"

                backtrack(row + 1)

                cols.remove(col)
                negdiag.remove(row - col)
                posdiag.remove(row + col)

                board[row][col] = "."
        
        backtrack(0)

        return result




class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = board
        COLS = board[0]

        rowseen = defaultdict(set)
        colseen = defaultdict(set)
        gridseen = defaultdict(set)

        

        for row in range(len(ROWS)):
            for col in range(len(COLS)):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in rowseen[row] or board[row][col] in colseen[col] or board[row][col] in gridseen[(row//3, col//3)]:
                    return False

                else:
                    rowseen[row].add(board[row][col])
                    colseen[col].add(board[row][col])
                    gridseen[(row//3, col//3)].add(board[row][col])
        
        return True

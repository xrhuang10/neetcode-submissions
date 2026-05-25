class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])


        def backtrack(row, col, seen, letter):
            if letter == len(word):
                return True
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or (row, col) in seen or board[row][col] != word[letter]:
                return False
            
            seen.add((row, col))
            letter += 1
            
            res = backtrack(row + 1, col, seen, letter) or backtrack(row - 1, col, seen, letter) or backtrack(row, col - 1, seen, letter) or backtrack(row, col + 1, seen, letter)
            seen.remove((row, col))
            return res
            

    
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, set(), 0):
                    return True
            
        
        return False

        
            



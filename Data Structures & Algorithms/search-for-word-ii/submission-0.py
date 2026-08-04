class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ROWS = len(board)
        COLS = len(board[0])
        seen = set()
        answer = set()

        def backtrack(row, col, word, node):
            if row < 0 or row == ROWS or col < 0 or col == COLS or (row, col) in seen or board[row][col] not in node.children:
                return
            
            seen.add((row, col))
            word += board[row][col]
            node = node.children[board[row][col]]
            if node.isWord:
                answer.add(word)

            for dr, dc in directions:
                backtrack(row + dr, col + dc, word, node)
            
            seen.remove((row, col))
        
        for i in range(ROWS):
            for j in range(COLS):
                backtrack(i, j, "", root)
        
        return list(answer)




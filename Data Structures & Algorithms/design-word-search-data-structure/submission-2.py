class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True

    def search(self, word: str) -> bool:
        def dfs(node, index):
            if index == len(word):
                return node.isWord
            for c in word[index:]:
                if c == '.':
                    return any(dfs(child, index+1) for child in node.children.values())
                elif c not in node.children:
                    return False

                node = node.children[c]
                index += 1
            return node.isWord

        
        curr = self.root
        return dfs(curr, 0)

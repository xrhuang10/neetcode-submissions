class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or endWord == beginWord:
            return 0
        
        adj = defaultdict(list)
        n = len(wordList)

        for i in range(n):
            word = wordList[i]
            for j in range(len(word)):
                key = word[:j] + '*' + word[j + 1:]
                adj[key].append(word)
        
        seen = set()
        seen.add(beginWord)

        q = collections.deque()
        q.append(beginWord)
        counter = 1

        while q:
            for i in range(len(q)):
                src = q.popleft()
                if src == endWord:
                    return counter
                for j in range(len(src)):
                    key = src[:j] + '*' + src[j + 1:]
                    for neighbor in adj[key]:
                        if neighbor not in seen:
                            seen.add(neighbor)
                            q.append(neighbor)
            
            counter += 1
        
        return 0



            

            
            
            


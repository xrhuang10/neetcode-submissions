class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        partition = []

        def ispalindrome(word):
            left = 0
            right = len(word) - 1
            while left < right:
                if word[left] != word[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(i):
            if i == len(s):
               res.append(partition.copy())
               return
            
            for j in range(i, len(s)):
                word = s[i:j + 1]
                if ispalindrome(word):
                    partition.append(word)
                    backtrack(j + 1)
                    partition.pop()
                    
            return None
        backtrack(0)
        return res




       
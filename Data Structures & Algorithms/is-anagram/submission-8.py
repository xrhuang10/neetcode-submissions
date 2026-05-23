class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashs = 26*[0]
        hasht = 26*[0]
        for i in range(len(s)):
            hashs[ord(s[i]) - ord('a')] += 1
        
        for j in range(len(t)):
            hasht[ord(t[j]) - ord('a')] += 1
        
        return hasht == hashs
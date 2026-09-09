class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx, resLen = 0, 1
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            for j in range(0, i):
                if s[i] == s[j] and (i - j <= 2 or dp[j+1][i-1] == True):
                    dp[j][i] = True

                    if i - j + 1 > resLen:
                        resLen = i - j + 1
                        resIdx = j
        
        return s[resIdx:resIdx+resLen]
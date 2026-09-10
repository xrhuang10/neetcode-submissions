class Solution:
    def countSubstrings(self, s: str) -> int:

        answer = 0
        n = len(s)
        dp = [[False]*n for _ in range(n)]

        for i in range(n):
            for j in range(i):
                if s[i] == s[j] and (i - j <= 2 or dp[j+1][i-1] == True):
                    dp[j][i] = True
                    answer += 1
        
        return answer + n
                


        

        
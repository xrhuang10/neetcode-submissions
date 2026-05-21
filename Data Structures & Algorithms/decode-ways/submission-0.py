class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}
        self.res = 0

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            self.res += dfs(i + 1)
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and
                s[i + 1] in "0123456"
            ):
                self.res += dfs(i + 2)
            dp[i] = self.res
            return self.res

        return dfs(0)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for tchar in t:
            need[tchar] = 1 + need.get(tchar, 0)
    
        have = {}
        l = 0
        required = len(need)
        formed = 0
        answer = ''

        for r in range(len(s)):
            have[s[r]] = 1 + have.get(s[r], 0)
            if s[r] in need and have[s[r]] == need[s[r]]:
                formed += 1
            
            while formed == required:
                if not answer or r - l + 1 < len(answer):
                    answer = s[l:r+1]
                have[s[l]] -= 1
                if s[l] in need and have[s[l]] < need[s[l]]:
                    formed -= 1
                l += 1
        
        return answer


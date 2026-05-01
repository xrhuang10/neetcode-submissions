class Solution:
    def minWindow(self, s: str, t: str) -> str:

        have = {}
        need = {}
        minlength = float("infinity")
        indices = [-1,-1]

        if len(t) > len(s):
            return ""

        for i in range(len(t)):
            need[t[i]] = 1 + need.get(t[i], 0)
        
        left = 0
        needCount = len(need)
        haveCount = 0

        for right in range(len(s)):

            have[s[right]] = 1 + have.get(s[right], 0)

            if s[right] in need and have[s[right]] == need[s[right]]:
                haveCount += 1

            while needCount == haveCount:
                if right - left + 1 < minlength:
                    minlength = right - left + 1
                    indices = [left, right]

                have[s[left]] -= 1

                if s[left] in need and have[s[left]] < need[s[left]]:
                    haveCount -= 1
                    

                left += 1
        
        return s[indices[0]:indices[1]+1] if indices != [-1,-1] else ""
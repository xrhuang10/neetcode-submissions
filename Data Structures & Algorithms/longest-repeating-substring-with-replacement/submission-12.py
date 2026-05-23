class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        answer = 0
        count = {}
        maxfreq = 0

        for r in range(len(s)):
            c = s[r]
            count[c] = 1 + count.get(c, 0)
            maxfreq = max(maxfreq, count.get(c, 0))

            while r - l - maxfreq >= k:
                count[s[l]] -= 1
                l += 1
            
            answer = max(answer, r - l + 1)

        return answer
            


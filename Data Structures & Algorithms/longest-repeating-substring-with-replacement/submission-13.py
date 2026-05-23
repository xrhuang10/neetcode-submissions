class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        answer = 0
        count = {}
        maxfreq = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            
            maxfreq = max(maxfreq, count[s[r]])

            while r - l + 1 - maxfreq > k:
                count[s[l]] -= 1
                l += 1
            
            answer = max(answer, r - l + 1)

        return answer

            


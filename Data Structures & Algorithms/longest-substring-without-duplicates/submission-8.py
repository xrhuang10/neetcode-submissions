class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        answer = 0
        hashmap = {}

        for right in range(len(s)):
            if s[right] in hashmap:
                left = max(hashmap[s[right]] + 1, left)
            hashmap[s[right]] = right
            answer = max(answer, right - left + 1)
        
        return answer
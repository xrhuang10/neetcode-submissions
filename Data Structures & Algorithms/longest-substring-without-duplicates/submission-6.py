class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        hashmap = {}
        answer = 0

        for right in range(len(s)):
            if s[right] in hashmap:
                left = max(hashmap[s[right]] + 1, left)
            hashmap[s[right]] = right

            answer = max(right - left + 1, answer)

        return answer

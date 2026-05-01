class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        seenchars = set()
        answer = 0
        while right < len(s):

            while right < len(s) and s[right] not in seenchars:
                seenchars.add(s[right])
                right += 1
                
            answer = max(answer, right - left)

            while right < len(s) and s[right] in seenchars and left < len(s):
                seenchars.remove(s[left])
                left += 1
            
            
        
        return answer





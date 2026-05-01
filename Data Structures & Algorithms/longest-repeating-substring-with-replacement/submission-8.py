class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        answer = 0 
        hashmap = {}
        maxfrequency = 0

        for right in range(len(s)):
            hashmap[s[right]] = 1 + hashmap.get(s[right], 0)
            maxfrequency = max(maxfrequency, hashmap[s[right]])

            while right - left + 1 - maxfrequency > k:
                hashmap[s[left]] -= 1
                left += 1
                
            answer = max(right - left + 1, answer)
        
        return answer


            

            
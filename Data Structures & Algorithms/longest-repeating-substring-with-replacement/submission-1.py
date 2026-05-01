class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        leftptr = 0
        res = 0
        
        for rightptr in range(len(s)):
            hashmap[s[rightptr]] = 1 + hashmap.get(s[rightptr], 0)
            
            while (rightptr - leftptr + 1) - max(hashmap.values()) > k:
                hashmap[s[leftptr]] -= 1
                leftptr += 1
            res = max(rightptr - leftptr + 1, res)
            

        return res

            

            
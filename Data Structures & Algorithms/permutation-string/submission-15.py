class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        substringmap = 26*[0]
        for r1 in range(len(s1)):
            substringmap[ord(s1[r1]) - ord('a')] += 1
        

        hashmap = 26*[0]
        l2 = 0
        for r2 in range(0, len(s2)):
            
            
            hashmap[ord(s2[r2]) - ord('a')] += 1
            
            if r2 >= len(s1):
                hashmap[ord(s2[l2]) - ord('a')] -= 1
                l2 += 1
                
            print("substringmap: " + str(substringmap))
            print(hashmap)
            if hashmap == substringmap:
                return True
            
        
        return False
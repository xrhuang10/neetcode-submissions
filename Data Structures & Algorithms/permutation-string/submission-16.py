class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1map = 26*[0]

        for i in range(len(s1)):
            s1map[ord(s1[i]) - ord('a')] += 1
        print('S1: ' + str(s1map))
        s2map = 26*[0]

        l = 0
        for r in range(len(s2)):
            
            s2map[ord(s2[r]) - ord('a')] += 1

            print('S2: ' + str(s2map) +'\n')
            if s1map == s2map:
                return True

            if r >= len(s1) - 1:
                s2map[ord(s2[l]) - ord('a')] -= 1
                l += 1


            
            
        
        
        return False
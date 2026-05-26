class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = {}
        for k in range(len(s)):
            hashmap[s[k]] = k
        

        res = []
        size = 0
        end = 0

        for i, c in enumerate(s):
            end = max(end, hashmap[c])
            size += 1

            if i == end:
                res.append(size)
                size = 0
            
        
        return res


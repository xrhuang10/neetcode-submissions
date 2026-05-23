class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = {}
        for k in range(len(s)):
            hashmap[s[k]] = k

        res = []
        size = 0
        end = 0

        for i, c in enumerate(s):
            size += 1
            end = max(end, hashmap[c])

            if i == end:
                res.append(size)
                size = 0
            
        return res


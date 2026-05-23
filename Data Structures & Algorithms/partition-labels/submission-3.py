class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = defaultdict(list)
        for k in range(len(s)):
            hashmap[s[k]].append(k)

        res = []
        i = 0
        end = -1
        
        while i < len(s):
            start = i
            end = max(hashmap[s[i]])
            j = i
            while j < end:
                end = max(end, max(hashmap[s[j]]))
                j += 1
            res.append(end - start + 1)
            
            i = end + 1
        
        return res


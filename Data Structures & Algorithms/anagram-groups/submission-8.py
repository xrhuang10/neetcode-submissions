class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)

        for string in strs:
            freq = 26*[0]
            for char in string:
                freq[ord(char) - ord('a')] += 1
            hashmap[tuple(freq)].append(string)
        

        answer = []
        for key in hashmap:
            answer.append(hashmap[key])
        return answer
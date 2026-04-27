class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        frequencies = [[] for i in range(len(nums) + 1)]

        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        

        for num, c in hashmap.items():
            frequencies[c].append(num)
        
        print(frequencies)

        result = []
        for i in range((len(frequencies) - 1), 0, -1):
            for number in frequencies[i]:
                result.append(number)
                if len(result) == k:
                    return result
        
                



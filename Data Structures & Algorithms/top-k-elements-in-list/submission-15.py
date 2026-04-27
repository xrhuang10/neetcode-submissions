class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num] += 1
        print(hashmap.items())
        hashmap = sorted(hashmap.items(), reverse=False, key=lambda x: x[1])

        answer = []
        for i in range(k):
            answer.append(hashmap.pop()[0])
        
        return answer


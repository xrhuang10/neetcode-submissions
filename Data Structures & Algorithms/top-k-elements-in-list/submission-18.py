class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for i in range(len(nums)):
            hashmap[nums[i]] += 1

        array = []
        for num, count in hashmap.items():
            array.append([count, num])
        
        array.sort(reverse = True)
        answer = []
        for i in range(k):
            answer.append(array[i][1])
        return answer

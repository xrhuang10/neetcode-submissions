class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        answer = 0
        for num in nums:
            if num - 1 not in nums:
                start = num
                count = 1
                while start + 1 in nums:
                    start += 1
                    count += 1
            
                answer = max(answer, count)
        return answer
                
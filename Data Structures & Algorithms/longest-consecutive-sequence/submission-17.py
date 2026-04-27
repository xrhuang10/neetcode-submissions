class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums = set(nums)

        counter = 1
        answer = 1
        for num in nums:
            if num - 1 not in nums:
                start = num
                while start + 1 in nums:
                    counter += 1
                    start += 1

                answer = max(answer, counter)
                counter = 1

        return answer


       
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for i, num in enumerate(nums):
            if target - num in numbers:
                return [numbers[target - num], i]
            else:
                numbers[num] = i


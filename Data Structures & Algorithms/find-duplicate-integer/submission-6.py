class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            idxtonegative = abs(nums[i]) - 1
            if nums[idxtonegative] < 0:
                return idxtonegative + 1
            nums[idxtonegative] *= -1

            
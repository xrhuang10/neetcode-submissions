class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        SUM = sum(nums)
        if SUM%2 == 1:
            return False
        else:
            TARGET = SUM//2
        
        seen = set()
        seen.add(0)
        for j in range(len(nums) - 1, -1, -1):
            for i in seen.copy():
                seen.add(nums[j] + i)
        
        return TARGET in seen

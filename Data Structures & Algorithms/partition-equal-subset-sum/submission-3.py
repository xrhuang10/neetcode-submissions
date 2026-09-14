class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        SUM = sum(nums)
        if SUM%2 == 1:
            return False
        TARGET = SUM/2

        seen = set()
        seen.add(0)

        for i in range(len(nums)):
            for j in seen.copy():
                seen.add(j + nums[i])
        
        return TARGET in seen
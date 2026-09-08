class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        earnings = [num for num in nums]
        earnings[1] = max(nums[0], nums[1])
        for i in range(2, len(earnings)):
   
            earnings[i] = max(earnings[i-1], earnings[i-2] + nums[i])

        
        return max(earnings)



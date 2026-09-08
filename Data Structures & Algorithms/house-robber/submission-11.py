class Solution:
    def rob(self, nums: List[int]) -> int:
        earnings = [num for num in nums]
        for i in range(2, len(earnings)):
            if i > 2:
                earnings[i] = max(earnings[i-2], earnings[i-3]) + nums[i]
            else:
                earnings[i] = earnings[i-2] + nums[i]
        
        return max(earnings)



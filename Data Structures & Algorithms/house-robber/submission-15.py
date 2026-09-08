class Solution:
    def rob(self, nums: List[int]) -> int:
        earnings = [num for num in nums]
        n = len(earnings)

        for i in range(2, n):
            if i == 2:
                earnings[i] = earnings[i-2] + nums[i]
            else:
                earnings[i] = max(earnings[i-2], earnings[i-3]) + nums[i]
        
        return max(earnings)



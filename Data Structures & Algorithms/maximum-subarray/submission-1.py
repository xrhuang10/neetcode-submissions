class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum = 0
        res = float("-infinity")

        for num in nums:
            if cursum < 0:
                cursum = 0
            cursum += num
            res = max(res, cursum)
        
        return res

        

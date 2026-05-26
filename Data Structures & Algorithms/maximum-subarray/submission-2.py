class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum = 0
        answer = float("-infinity")

        for num in nums:
            cursum += num
            answer = max(answer, cursum)
            if cursum < 0:
                cursum = 0
        
        return answer
        


        

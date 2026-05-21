class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minsubarray, maxsubarray, answer = 1, 1, nums[0]

        for i in range(len(nums)):
            tmp = minsubarray * nums[i]
            minsubarray = min(nums[i] * minsubarray, nums[i] * maxsubarray, nums[i])
            maxsubarray = max(tmp, nums[i] * maxsubarray, nums[i])

            answer = max(answer, maxsubarray)
        
        return answer
            
        
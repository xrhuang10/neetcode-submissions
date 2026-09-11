class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minsubarray, maxsubarray, answer = 1, 1, nums[0]

        for i in range(len(nums)):
            tmp = minsubarray * nums[i]
            minsubarray = min(maxsubarray * nums[i], minsubarray * nums[i], nums[i])
            maxsubarray = max(maxsubarray * nums[i], tmp, nums[i])
            answer = max(maxsubarray, answer)
        
        return answer
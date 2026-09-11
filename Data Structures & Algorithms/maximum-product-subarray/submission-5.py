class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minsubarray = 1
        maxsubarray = 1
        answer = max(nums)

        for i in range(len(nums)):
            temp = minsubarray
            minsubarray = min(maxsubarray * nums[i], minsubarray * nums[i], nums[i])
            maxsubarray = max(temp*nums[i], maxsubarray*nums[i], nums[i])
            answer = max(answer, maxsubarray)
        
        return answer
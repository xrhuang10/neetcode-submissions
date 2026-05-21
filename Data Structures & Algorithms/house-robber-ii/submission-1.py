class Solution:
    def rob(self, nums: List[int]) -> int:
        one, two = 0, 0
        three, four = 0, 0

        if len(nums) <= 1:
            return nums[0]

        for i in range(1, len(nums)):
            temp = max(one + nums[i], two)
            one = two
            two = temp

        for j in range(len(nums) - 1):
            temp = max(three + nums[j], four)
            three = four
            four = temp
        
        return max(two, four)
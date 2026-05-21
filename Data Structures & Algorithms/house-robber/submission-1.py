class Solution:
    def rob(self, nums: List[int]) -> int:
        maximum = 0
        n = len(nums)
        cache = [0] * (n)
        if len(nums) <= 1:
            return nums[0]

        cache[0] = nums[0]
        cache[1] = nums[1]

        
        for i in range(2, n):
            cache[i] = max(cache[i - 2], cache[i - 3]) + nums[i]
            print(cache)

        return max(cache[-1], cache[-2])



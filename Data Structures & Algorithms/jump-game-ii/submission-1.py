class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        counter = 0
        farthest = nums[0]

        while r < len(nums) - 1:
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            
            l = r + 1
            r = farthest
            counter += 1
        return counter

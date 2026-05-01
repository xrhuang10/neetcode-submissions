class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        maximum = []

        for right in range(k, len(nums)+1):
            maximum.append(max(nums[left:right]))
            left+=1
        
        return maximum
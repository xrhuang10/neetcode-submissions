class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #001
        #010
        #011
        #000 need
        #not and

        #000
        #010
        #001 need
        #not xor
        n = len(nums)
        curr = n
        for i in range(len(nums)):
            curr = curr ^ i ^ nums[i]
        return curr
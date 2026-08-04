class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while l < r:
                if nums[l] + nums[r] + nums[i] == 0:
                    answer.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif nums[l] + nums[r] + nums[i] > 0:
                    r -= 1
                else:
                    l += 1
        
        return answer

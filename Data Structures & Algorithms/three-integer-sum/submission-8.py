class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        answer = []

        for anchor in range(len(nums)):
            

            if nums[anchor] > 0:
                break

            if anchor > 0 and nums[anchor] == nums[anchor - 1]:
                continue
            
            
        

            left = anchor + 1
            right = len(nums) - 1
           
            while left < right:
                
                
                if nums[left] + nums[right] == -1* nums[anchor]:
                    answer.append([nums[left], nums[anchor], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                elif nums[left] + nums[right] > -1* nums[anchor]:
                    right -= 1
                elif nums[left] + nums[right] < -1* nums[anchor]:
                    left += 1

        return answer


        

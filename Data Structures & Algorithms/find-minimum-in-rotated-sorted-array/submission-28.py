class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        answer = nums[0]

        while l <= r:
  
            m = l + (r-l)//2
            answer = min(answer, nums[m])
            
            if nums[r] < nums[m]:
                l = m + 1
            else:
                r = m - 1

        return answer

                

            


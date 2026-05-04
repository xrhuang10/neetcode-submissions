class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        answer = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                answer = min(answer, nums[l])
                break
                

            m = l + (r-l)//2
            answer = min(answer, nums[m])

            if nums[m] >= nums[r]:
                l = m + 1

            else:
                r = m - 1
        
        return answer
                

            


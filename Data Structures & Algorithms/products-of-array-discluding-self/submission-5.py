class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []

        for i in range(len(nums)):
            if prefix != []:
                prefix.append(nums[i - 1] * prefix[-1])
            else:
                prefix.append(1)
            
        
        for j in range(len(nums) - 1, -1, -1):
            if suffix != []:
                suffix.append(nums[j + 1] * suffix[-1])
            else:
                suffix.append(1)
        
        answer = []
        for i in range(len(suffix)):
            answer.append(prefix[i] * suffix[len(suffix) - i - 1])
        return answer

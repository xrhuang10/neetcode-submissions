class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        boolarray = [False] * len(nums)
        print(boolarray)

        def dfs(curr, boolarray, nums):
            if len(nums) == len(curr):
                res.append(curr.copy())
                return
            
            for i in range(len(nums)):
                if not boolarray[i]:
                    curr.append(nums[i])
                    boolarray[i] = True
                    dfs(curr, boolarray, nums)
                    curr.pop()
                    boolarray[i] = False
        
        dfs([], boolarray, nums)
        return res
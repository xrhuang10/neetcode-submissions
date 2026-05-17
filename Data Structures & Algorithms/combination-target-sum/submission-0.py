class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        valid_subset = []

        def dfs(i):
            if sum(valid_subset.copy()) > target or i >= len(nums):
                return
            elif sum(valid_subset.copy()) == target:
                res.append(valid_subset.copy())
                return
            
            valid_subset.append(nums[i])
            dfs(i)
            
            valid_subset.pop()
            dfs(i + 1)
        
        dfs(0)
    
        return res
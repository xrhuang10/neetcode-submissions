class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        def dfs(i, cur, total):
            if total == target:
                output.append(cur.copy())
                return
            
            elif total > target or i >= len(nums):
                return
            
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            cur.pop()
            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)
        return output

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        boolarray = [False] * len(nums)

        def backtrack(cur):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return

            for i in range(len(nums)):
                if not boolarray[i]:
                    cur.append(nums[i])
                    boolarray[i] = True
                    backtrack(cur)
                    cur.pop()
                    boolarray[i] = False

        
        backtrack([])
        return res

            
            
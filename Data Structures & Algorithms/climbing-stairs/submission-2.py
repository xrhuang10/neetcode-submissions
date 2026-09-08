class Solution:
    def climbStairs(self, n: int) -> int:

        steps = (n+1)*[1]
        for i in range(2, len(steps)):
            steps[i] = steps[i-1] + steps[i-2]
        
        return steps[-1]

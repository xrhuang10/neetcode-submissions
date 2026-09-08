class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        steps = [0]*(len(cost)+1) #each entry is cost at that step
        for i in range(2, len(steps)):
            steps[i] = min(cost[i-1] + steps[i-1], cost[i-2] + steps[i-2])
        
        return max(steps)


        
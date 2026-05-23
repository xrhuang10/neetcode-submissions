class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        answer = 0

        for r in range(1, len(prices)):
            if prices[r] > prices[l]:
                answer = max(answer, prices[r] - prices[l])
            else:
                l = r
        
        return answer
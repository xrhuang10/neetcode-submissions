class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        left, right = 0, 1

        while right < len(prices):
            
            if prices[right] < prices[left]:
                left = right
                
            else:
                maxprofit = max(maxprofit, prices[right] - prices[left])
                right += 1

        return maxprofit
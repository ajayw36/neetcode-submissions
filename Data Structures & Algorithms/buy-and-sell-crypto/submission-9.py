class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 0
        profit = prices[j] - prices[i]
        while j < len(prices):
            if prices[j] < prices[i]:
                i = j
            profit = max(profit, prices[j] - prices[i])
            j += 1
            
        
        return profit

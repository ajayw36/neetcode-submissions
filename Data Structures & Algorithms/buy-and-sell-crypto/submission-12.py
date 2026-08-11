class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxP = 0

        for sell in prices[1:]:
            maxP = max(sell - minBuy, maxP)
            if sell < minBuy:
                minBuy = sell
        
        return maxP